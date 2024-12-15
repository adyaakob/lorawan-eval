import firebase_admin
from firebase_admin import credentials, auth
from firebase_config import FIREBASE_CONFIG, create_user, verify_user, reset_password
import traceback
import sys
import time

def diagnose_firebase_setup():
    print("Firebase Diagnostic Information:")
    print("=" * 40)
    
    try:
        # Check service account file
        print("1. Service Account Verification:")
        service_account_path = 'firebase_service_account.json'
        cred = credentials.Certificate(service_account_path)
        print(f"   - Project ID: {cred.project_id}")
        print(f"   - Service Account Email: {cred.service_account_email}")
    except Exception as e:
        print("   - Service Account Verification FAILED:")
        print(traceback.format_exc())
    
    print("\n2. Firebase Configuration:")
    for key, value in FIREBASE_CONFIG.items():
        print(f"   - {key}: {value}")
    
    print("\n3. Authentication Providers:")
    try:
        # Attempt to list auth providers (if possible)
        providers = auth.list_providers()
        print("   - Providers:", providers)
    except Exception as e:
        print("   - Could not list providers:")
        print(traceback.format_exc())

def test_firebase_authentication():
    diagnose_firebase_setup()
    
    print("\n4. Authentication Tests:")
    # Test User Creation
    test_email = f"test_user_{int(time.time())}@example.com"
    test_password = "SecurePassword123!"

    try:
        # 1. Create User
        new_user = create_user(test_email, test_password)
        if new_user:
            print(f"   - User created successfully: {new_user.uid}")
        else:
            print("   - Failed to create user")
    except Exception as e:
        print("   - User creation error:")
        print(traceback.format_exc())

    try:
        # 2. Verify User
        verification_result = verify_user(test_email, test_password)
        if verification_result:
            print("   - User verification successful")
        else:
            print("   - User verification failed")
    except Exception as e:
        print("   - Verification error:")
        print(traceback.format_exc())

    try:
        # 3. Password Reset
        reset_result = reset_password(test_email)
        if reset_result:
            print("   - Password reset link generated")
        else:
            print("   - Password reset failed")
    except Exception as e:
        print("   - Password reset error:")
        print(traceback.format_exc())

if __name__ == "__main__":
    test_firebase_authentication()
