#Enhanced Doctor Login System 
import hashlib
import os
import binascii

# Doctor Database (Hash Map: Username → Security Data)
doctors_db = {
    # Format: {username: {"hash": "...", "salt": "...", "name": "...", "access": ["records", "labs"]}}
    "dr_grey": {
        "hash": "e9a2...",  # Will generate below
        "salt": "b6f3...",  # Will generate below
        "name": "Meredith Grey",
        "access": ["patient_records", "surgery_schedule"]
    }
}

# Generate secure credentials for Dr. Grey
password = "SeattleGrace1!".encode()
salt = os.urandom(16)  # Random 16-byte salt
dk = hashlib.pbkdf2_hmac('sha256', password, salt, 100000)  # Key stretching

# Update database
doctors_db["dr_grey"]["salt"] = binascii.hexlify(salt).decode()
doctors_db["dr_grey"]["hash"] = binascii.hexlify(dk).decode()

def authenticate_doctor(username: str, password: str) -> bool:
    """Verify doctor credentials using PBKDF2-HMAC-SHA256"""
    if username not in doctors_db:
        return False
    
    # Retrieve stored security data
    stored_salt = binascii.unhexlify(doctors_db[username]["salt"].encode())
    stored_hash = doctors_db[username]["hash"]
    
    # Hash the attempt with stored salt
    attempt_dk = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode(),
        stored_salt,
        100000
    )
    
    # Constant-time comparison to prevent timing attacks
    return binascii.hexlify(attempt_dk).decode() == stored_hash

def doctor_login():
    """Hospital login interface"""
    print("🏥 MEDICAL PORTAL AUTHENTICATION")
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    
    if authenticate_doctor(username, password):
        doctor = doctors_db[username]
        print(f"\n🔓 ACCESS GRANTED: Welcome Dr. {doctor['name']}")
        print(f"🩺 Privileges: {', '.join(doctor['access'])}")
        return True
    else:
        print("\n❌ ACCESS DENIED: Invalid credentials")
        return False

# Simulate login attempt
if __name__ == "__main__":
    doctor_login()