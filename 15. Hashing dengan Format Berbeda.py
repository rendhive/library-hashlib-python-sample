import hashlib

def hash_with_format(data, algorithm):
    hasher = hashlib.new(algorithm)
    hasher.update(data.encode())
    return hasher.hexdigest()

result = hash_with_format("Hello, World!", "sha256")
print(f"Custom Hash: {result}")
# Fungsi: Menghasilkan hash dengan algoritma yang ditentukan pengguna.
# Kondisi: Ketika Anda perlu menentukan algoritma hashing secara dinamis.