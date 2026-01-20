import hashlib
import os

def hash_password_salt(password):
    salt = os.urandom(16)
    return salt.hex() + hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000).hex()

password = "MySecurePassword"
secure_hashed_password = hash_password_salt(password)
print(f"Secure Hashed Password: {secure_hashed_password}")
# Fungsi: Menghasilkan hashed password yang aman dengan salt.
# Kondisi: Ketika Anda ingin melindungi password dari serangan rainbow table.