from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_socketio import SocketIO, emit
from datetime import datetime
import os
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from functools import wraps
import json
from sqlalchemy import inspect, text
from estate_area_calculator import estates, estimate_estate_area

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lorawan_eval.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
socketio = SocketIO(app, cors_allowed_origins="*")
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Database Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    reports = db.relationship('EvaluationReport', backref='author', lazy=True)

class EvaluationReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    document_paths = db.Column(db.Text, nullable=True)  # JSON-serialized list of document paths
    photo_paths = db.Column(db.Text, nullable=True)    # JSON-serialized list of photo paths

class DeviceLocation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.String(50), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    battery_level = db.Column(db.Float)
    last_update = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    estate = db.Column(db.String(50))

class EvaluationTeam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    organization = db.Column(db.String(100), nullable=True)
    contact_email = db.Column(db.String(120), nullable=True)
    contact_phone = db.Column(db.String(20), nullable=True)
    team_type = db.Column(db.String(20), nullable=False)  # 'Internal' or 'External'

    def __repr__(self):
        return f'<EvaluationTeam {self.name} - {self.role} ({self.team_type})>'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Ensure database is created with all tables
with app.app_context():
    # First create all tables
    db.create_all()
    
    # Then attempt to add missing columns
    try:
        engine = db.engine
        
        def add_columns(table, column):
            """
            Attempt to add a column to an existing table if it doesn't exist
            """
            try:
                column_exists = False
                inspector = inspect(engine)
                columns = inspector.get_columns(table)
                for col in columns:
                    if col['name'] == column:
                        column_exists = True
                        break
                
                if not column_exists:
                    with engine.connect() as conn:
                        conn.execute(text(f'ALTER TABLE {table} ADD COLUMN {column} TEXT'))
                        conn.commit()
                        print(f"Added column {column} to {table}")
            except Exception as e:
                print(f"Error adding column {column}: {e}")
        
        # Add document_paths column if not exists
        add_columns('evaluation_report', 'document_paths')
        
        # Add photo_paths column if not exists
        add_columns('evaluation_report', 'photo_paths')
    except Exception as e:
        print(f"Migration error: {e}")
        db.session.rollback()

# Add file upload configuration
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'uploads')
ALLOWED_DOCUMENT_EXTENSIONS = {'pdf', 'doc', 'docx', 'txt', 'csv', 'xlsx'}
ALLOWED_IMAGE_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp'}

# Ensure upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB max upload size

# Add file extension validation functions
def allowed_document_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_DOCUMENT_EXTENSIONS

def allowed_image_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_IMAGE_EXTENSIONS

# Admin-only decorator
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.username != 'admin':
            flash('You do not have permission to access this page.', 'danger')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/evaluation-plan')
def evaluation_plan():
    return render_template('evaluation_plan.html')

@app.route('/evaluation-procedure')
def evaluation_procedure():
    return render_template('evaluation_procedure.html')

@app.route('/evaluation-report', methods=['GET', 'POST'])
def evaluation_report():
    # Fetch existing reports for display
    reports = EvaluationReport.query.order_by(EvaluationReport.date_created.desc()).all()

    # Only allow admin to submit new reports
    if current_user.is_authenticated and current_user.username == 'admin' and request.method == 'POST':
        try:
            # Extract form data
            report_data = {
                'title': request.form.get('report_title', 'Evaluation Report'),
                'start_date': request.form.get('startDate'),
                'end_date': request.form.get('endDate'),
                'equipment': request.form.get('equipment'),
                'estate': request.form.get('selectedEstate'),
                'summary': request.form.get('summaryTextarea'),
                'conclusion': json.dumps({
                    'lorawanRange': request.form.get('lorawanRangeConclusion'),
                    'gpsPerformance': request.form.get('gpsPerformanceConclusion'),
                    'devicePerformance': request.form.get('devicePerformanceConclusion'),
                    'cellularSignal': request.form.get('cellularSignalConclusion')
                }),
                'recommendations': request.form.get('recommendationTextarea'),
                'team': json.dumps({
                    'teqArmada': [
                        {
                            'name': request.form.get('teqArmadaName1'),
                            'position': request.form.get('teqArmadaPosition1'),
                            'contact': request.form.get('teqArmadaContact1')
                        }
                    ],
                    'sabahSoftwoods': [
                        {
                            'name': request.form.get('sabahSoftwoodsName1'),
                            'position': request.form.get('sabahSoftwoodsPosition1'),
                            'contact': request.form.get('sabahSoftwoodsContact1')
                        }
                    ]
                })
            }
            
            # Create new report
            new_report = EvaluationReport(
                title=report_data['title'],
                content=json.dumps(report_data),
                user_id=current_user.id
            )
            
            db.session.add(new_report)
            db.session.commit()
            
            # Handle file uploads
            documents = request.files.getlist('documents')
            photos = request.files.getlist('photos')
            
            # Process document uploads
            document_paths = []
            for doc in documents:
                if doc and allowed_document_file(doc.filename):
                    filename = secure_filename(f"doc_{new_report.id}_{doc.filename}")
                    filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'documents', filename)
                    os.makedirs(os.path.dirname(filepath), exist_ok=True)
                    doc.save(filepath)
                    document_paths.append(filepath)
            
            # Process photo uploads
            photo_paths = []
            for photo in photos:
                if photo and allowed_image_file(photo.filename):
                    filename = secure_filename(f"photo_{new_report.id}_{photo.filename}")
                    filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'photos', filename)
                    os.makedirs(os.path.dirname(filepath), exist_ok=True)
                    photo.save(filepath)
                    photo_paths.append(filepath)
            
            # Update report with file paths
            new_report.document_paths = json.dumps(document_paths)
            new_report.photo_paths = json.dumps(photo_paths)
            db.session.commit()
            
            flash('Evaluation report submitted successfully!', 'success')
            return redirect(url_for('evaluation_report'))
        
        except Exception as e:
            db.session.rollback()
            flash(f'Error submitting report: {str(e)}', 'danger')
    
    # Render the template with reports for all users
    return render_template('evaluation_report.html', reports=reports)

@app.route('/evaluation-checklist')
def evaluation_checklist():
    return render_template('evaluation_checklist.html')

@app.route('/pre-site-visit-checklist')
def pre_site_visit_checklist():
    return render_template('pre_site_visit_checklist.html')

@app.route('/evaluation-team', methods=['GET', 'POST'])
def evaluation_team():
    # Only admin can modify the team
    if request.method == 'POST':
        if not current_user.is_authenticated or current_user.username != 'admin':
            flash('Only admin can modify the evaluation team.', 'danger')
            return redirect(url_for('evaluation_team'))
        
        # Add new team member
        if 'action' not in request.form or request.form['action'] == 'add':
            name = request.form.get('name')
            role = request.form.get('role')
            contact_email = request.form.get('contact_email')
            contact_phone = request.form.get('contact_phone')
            team_type = request.form.get('team_type')
            
            if not all([name, role, team_type]):
                flash('Name, Role, and Team Type are required.', 'danger')
                return redirect(url_for('evaluation_team'))
            
            new_team_member = EvaluationTeam(
                name=name,
                role=role,
                contact_email=contact_email,
                contact_phone=contact_phone,
                team_type=team_type
            )
            
            try:
                db.session.add(new_team_member)
                db.session.commit()
                flash('Team member added successfully!', 'success')
            except Exception as e:
                db.session.rollback()
                flash(f'Error adding team member: {str(e)}', 'danger')
        
        # Edit existing team member
        elif request.form['action'] == 'edit':
            member_id = request.form.get('member_id')
            member = EvaluationTeam.query.get(member_id)
            
            if not member:
                flash('Team member not found.', 'danger')
                return redirect(url_for('evaluation_team'))
            
            member.name = request.form.get('name')
            member.role = request.form.get('role')
            member.contact_email = request.form.get('contact_email')
            member.contact_phone = request.form.get('contact_phone')
            member.team_type = request.form.get('team_type')
            
            try:
                db.session.commit()
                flash('Team member updated successfully!', 'success')
            except Exception as e:
                db.session.rollback()
                flash(f'Error updating team member: {str(e)}', 'danger')
        
        # Remove team member
        elif request.form['action'] == 'remove':
            member_id = request.form.get('member_id')
            member = EvaluationTeam.query.get(member_id)
            
            if not member:
                flash('Team member not found.', 'danger')
                return redirect(url_for('evaluation_team'))
            
            try:
                db.session.delete(member)
                db.session.commit()
                flash('Team member removed successfully!', 'success')
            except Exception as e:
                db.session.rollback()
                flash(f'Error removing team member: {str(e)}', 'danger')
        
        return redirect(url_for('evaluation_team'))
    
    # GET request: display team members
    internal_team = EvaluationTeam.query.filter_by(team_type='Internal').all()
    external_team = EvaluationTeam.query.filter_by(team_type='External').all()
    
    return render_template('evaluation_team.html', 
                           internal_team=internal_team, 
                           external_team=external_team)

@app.route('/map')
def map_view():
    estates = [
        {
            'name': 'Cenderamata Oil Palm Estate',
            'coords': [117.720694, 4.511972],
            'reported_size': 53,
            'officerInCharge': 'Jeffry Ahmad'
        },
        {
            'name': 'Dumpas Oil Palm Estate',
            'coords': [117.720694, 4.511972],
            'reported_size': 53,
            'officerInCharge': 'Jeffry Ahmad'
        },
        {
            'name': 'Sungai Indit Oil Palm Estate',
            'coords': [117.697833, 4.660639],
            'reported_size': 70,
            'officerInCharge': 'Jeffry Ahmad'
        },
        {
            'name': 'Banita Oil Palm Estate',
            'coords': [117.509333, 4.526500],
            'reported_size': 65,
            'officerInCharge': 'Jeffry Ahmad'
        },
        {
            'name': 'Kapilit Oil Palm Estate',
            'coords': [117.509333, 4.526500],
            'reported_size': 79,
            'officerInCharge': 'Jeffry Ahmad'
        },
        {
            'name': 'Sungai Tiagau Oil Palm Estate',
            'coords': [117.492083, 4.531611],
            'reported_size': 82,
            'officerInCharge': 'Jeffry Ahmad'
        },
        {
            'name': 'Mawang Oil Palm Estate',
            'coords': [117.483028, 4.556444],
            'reported_size': 83,
            'officerInCharge': 'Jeffry Ahmad'
        },
        {
            'name': 'Kumansi Oil Palm Estate',
            'coords': [117.449611, 4.478444],
            'reported_size': 91,
            'officerInCharge': 'Jeffry Ahmad'
        },
        {
            'name': 'Bukit Tukok Oil Palm Estate',
            'coords': [117.494528, 4.460528],
            'reported_size': 87,
            'officerInCharge': 'Jeffry Ahmad'
        }
    ]
    return render_template('map.html', estates=estates)

@app.route('/estate_areas')
def estate_areas():
    """
    Render a page showing estate area calculations
    """
    estate_calculations = []
    for estate in estates:
        result = estimate_estate_area(
            estate['coords'][1], 
            estate['coords'][0], 
            estate['reported_size']  # Changed from 'size' to 'reported_size'
        )
        estate_calculations.append({
            'name': estate['name'],
            'reported_size': estate['reported_size'],
            'estimated_area': result['estimated_area_ha'],
            'coordinates': estate['coords']
        })
    
    return render_template('estate_areas.html', estates=estate_calculations)

@app.route('/project_implementation_timeline')
def project_implementation_timeline():
    return render_template('project_implementation_timeline.html')

@app.route('/project_cost_estimation')
def project_cost_estimation():
    return render_template('project_cost_estimation.html')

@app.route('/api/update_location', methods=['POST'])
def update_location():
    try:
        data = request.json
        device_id = data.get('device_id')
        lat = float(data.get('latitude'))
        lon = float(data.get('longitude'))
        battery = data.get('battery_level')
        estate = data.get('estate')
        
        if not all([device_id, lat, lon]):
            return jsonify({'error': 'Missing required fields'}), 400
        
        location = DeviceLocation.query.filter_by(device_id=device_id).first()
        if location:
            location.latitude = lat
            location.longitude = lon
            location.battery_level = battery
            location.estate = estate
            location.last_update = datetime.utcnow()
        else:
            location = DeviceLocation(
                device_id=device_id,
                latitude=lat,
                longitude=lon,
                battery_level=battery,
                estate=estate
            )
            db.session.add(location)
        
        db.session.commit()
        
        # Emit the update to all connected clients
        socketio.emit('location_update', {
            'device_id': device_id,
            'latitude': lat,
            'longitude': lon,
            'battery_level': battery,
            'estate': estate,
            'last_update': datetime.utcnow().isoformat()
        })
        
        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/get_locations')
def get_locations():
    try:
        locations = DeviceLocation.query.all()
        return jsonify([{
            'device_id': loc.device_id,
            'latitude': loc.latitude,
            'longitude': loc.longitude,
            'battery_level': loc.battery_level,
            'estate': loc.estate,
            'last_update': loc.last_update.isoformat()
        } for loc in locations])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'danger')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        # Basic validation
        if not all([username, email, password, confirm_password]):
            flash('All fields are required', 'danger')
            return redirect(url_for('register'))
        
        if password != confirm_password:
            flash('Passwords do not match', 'danger')
            return redirect(url_for('register'))
        
        # Check if user already exists
        if User.query.filter_by(username=username).first():
            flash('Username already exists', 'danger')
            return redirect(url_for('register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already exists', 'danger')
            return redirect(url_for('register'))
        
        # Create new user
        hashed_password = generate_password_hash(password)
        new_user = User(
            username=username, 
            email=email, 
            password=hashed_password
        )
        
        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            flash(f'Registration error: {str(e)}', 'danger')
            return redirect(url_for('register'))
    
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

@app.route('/download/<path:filename>')
@login_required
@admin_required
def download_file(filename):
    try:
        return send_file(filename, as_attachment=True)
    except Exception as e:
        flash(f'Error downloading file: {str(e)}', 'danger')
        return redirect(url_for('evaluation_report'))

# Add an admin user creation script
def create_admin_user():
    with app.app_context():
        # Check if admin user already exists
        existing_admin = User.query.filter_by(username='admin').first()
        if not existing_admin:
            # Create admin user with a fixed password for testing
            admin_user = User(
                username='admin',
                email='admin@teqarmada.com',
                password=generate_password_hash('admin1234')
            )
            db.session.add(admin_user)
            db.session.commit()
            print("Admin user created successfully!")
        else:
            # Update existing admin user's password
            existing_admin.password = generate_password_hash('admin1234')
            db.session.commit()
            print("Admin user password updated!")

# Call this function when the app starts
create_admin_user()

if __name__ == '__main__':
    try:
        print("Starting server on http://localhost:5000")
        socketio.run(app, host='127.0.0.1', port=5000, debug=True, allow_unsafe_werkzeug=True)
    except Exception as e:
        print(f"Error starting server: {e}")
