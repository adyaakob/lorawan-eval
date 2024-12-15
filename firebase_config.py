import firebase_admin
from firebase_admin import credentials, firestore, auth
import pyrebase
import os
import traceback

# Verbose logging for configuration
print("Firebase Configuration Initialization:")
print(f"Current Working Directory: {os.getcwd()}")
print(f"Service Account Path: {os.path.abspath('firebase_service_account.json')}")

try:
    # Initialize Firebase Admin SDK with absolute path
    service_account_path = os.path.abspath('firebase_service_account.json')
    cred = credentials.Certificate(service_account_path)
    
    # Print service account details for verification
    print(f"Service Account Project ID: {cred.project_id}")
    
    # Initialize Firebase app with project ID
    firebase_admin.initialize_app(cred, {
        'projectId': 'lorawan-eval'
    })

    # Initialize Firestore
    db = firestore.client()
    print("Firestore client initialized successfully.")

except Exception as e:
    print("Error initializing Firebase Admin SDK:")
    print(traceback.format_exc())
    raise

# Web App Configuration (for client-side)
FIREBASE_CONFIG = {
    'apiKey': "AIzaSyBZm1pC1yrjGAa3H1_DoACkfUuhJ71jlSc",
    'authDomain': "lorawan-eval.firebaseapp.com",
    'projectId': "lorawan-eval",
    'storageBucket': "lorawan-eval.appspot.com",
    'messagingSenderId': "867493020541",
    'appId': "1:867493020541:web:8bcc9eab3495f36be54214",
    'measurementId': "G-SLE8MEKHSM",
    'databaseURL': "https://lorawan-eval-default-rtdb.firebaseio.com/"
}

# Initialize Pyrebase for additional auth methods
try:
    pyrebase_app = pyrebase.initialize_app(FIREBASE_CONFIG)
    pyrebase_auth = pyrebase_app.auth()
    print("Pyrebase initialized successfully.")
except Exception as e:
    print("Error initializing Pyrebase:")
    print(traceback.format_exc())
    raise

def get_firestore_client():
    return db

def create_user(email, password):
    """Create a new user in Firebase Authentication"""
    try:
        # Create user with Firebase Admin SDK
        user = auth.create_user(
            email=email,
            password=password
        )
        
        # Optional: Commented out Firestore user creation
        # user_ref = db.collection('users').document(user.uid)
        # user_ref.set({
        #     'email': email,
        #     'created_at': firestore.SERVER_TIMESTAMP,
        #     'active': True
        # })
        
        print(f"User created successfully: {user.uid}")
        return user
    except Exception as e:
        print("Detailed error creating user:")
        print(traceback.format_exc())
        return None

def verify_user(email, password):
    """Verify user credentials using Pyrebase"""
    try:
        # Use Pyrebase for more robust authentication
        user = pyrebase_auth.sign_in_with_email_and_password(email, password)
        print("User verified successfully")
        return user is not None
    except Exception as e:
        print("Detailed authentication error:")
        print(traceback.format_exc())
        return False

def reset_password(email):
    """Send password reset email"""
    try:
        # Generate password reset link using Firebase Admin SDK
        reset_link = auth.generate_password_reset_link(email)
        print(f"Password reset link generated: {reset_link}")
        return True
    except Exception as e:
        print("Detailed password reset error:")
        print(traceback.format_exc())
        return False

def get_user_by_email(email):
    """Retrieve Firebase user by email"""
    try:
        user = auth.get_user_by_email(email)
        return user
    except Exception as e:
        print(f"User retrieval error for {email}:")
        print(traceback.format_exc())
        return None
