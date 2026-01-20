import hashlib

def sha3_hash(data):
    return hashlib.sha3_256(data.encode()).hexdigest()

result = sha3_hash("Hello, World!")
print(f"SHA-3: {result}")
# Fungsi: Menghasilkan hash SHA-3 dari string input.
# Kondisi: Ketika Anda membutuhkan algoritma hashing yang lebih baru daripada SHA-2.