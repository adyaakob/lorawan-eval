from app import app, db, User
from werkzeug.security import generate_password_hash

with app.app_context():
    # Check if admin already exists
    existing_admin = User.query.filter_by(username='admin').first()
    if existing_admin:
        print("Admin user already exists!")
    else:
        # Create admin user
        admin_password = 'TEQAdmin2024!'
        admin_user = User(
            username='admin', 
            email='admin@teqarmada.com', 
            password=generate_password_hash(admin_password)
        )
        db.session.add(admin_user)
        db.session.commit()
        print(f"Admin user created with username: admin")
        print(f"Admin password: {admin_password}")
