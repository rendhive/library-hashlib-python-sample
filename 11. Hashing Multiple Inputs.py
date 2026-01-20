import hashlib

def hash_multiple_strings(strings):
    combined = ''.join(strings)
    return hashlib.sha256(combined.encode()).hexdigest()

inputs = ["Hello", "World", "2023"]
result = hash_multiple_strings(inputs)
print(f"Combined Hash: {result}")
# Fungsi: Menghasilkan hash untuk kombinasi dari beberapa string.
# Kondisi: Ketika Anda perlu membuat hash berdasarkan beberapa input yang digabungkan.