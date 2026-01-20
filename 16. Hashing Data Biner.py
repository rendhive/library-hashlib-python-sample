import hashlib

def hash_binary_data(data):
    return hashlib.sha256(data).hexdigest()

binary_data = b"Some binary data 12345"
result = hash_binary_data(binary_data)
print(f"Binary Hash: {result}")
# Fungsi: Menghasilkan hash untuk data biner.
# Kondisi: Ketika Anda perlu memproses file biner atau saat data sudah dalam bentuk biner