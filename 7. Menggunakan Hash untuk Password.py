import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

password = "MySecretPassword"
hashed_password = hash_password(password)
print(f"Hashed Password: {hashed_password}")
# Fungsi: Menghasilkan hash untuk password pengguna.
# Kondisi: Ketika menyimpan password dan ingin menjaga keamanan data pengguna.