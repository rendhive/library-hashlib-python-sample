import hashlib

def sha256_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

result = sha256_hash("Hello, World!")
print(f"SHA-256: {result}")
# Fungsi: Menghasilkan hash SHA-256 dari string input.
# Kondisi: Ketika Anda ingin menghasilkan hash yang kuat untuk keamanan data.