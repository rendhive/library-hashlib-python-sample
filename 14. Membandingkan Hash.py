import hashlib

def compare_hashes(data, hash_to_compare):
    return hashlib.sha256(data.encode()).hexdigest() == hash_to_compare

data = "Hello, World!"
hash_value = hashlib.sha256(data.encode()).hexdigest()
result = compare_hashes(data, hash_value)
print(f"Hashes match: {result}")
# Fungsi: Membandingkan hash dari data dengan hash yang disediakan.
# Kondisi: Ketika Anda ingin memverifikasi keaslian data menggunakan hash.