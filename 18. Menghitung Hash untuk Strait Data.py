import hashlib

def calculate_hash(plaintext):
    return hashlib.sha1(plaintext.encode()).hexdigest()

text = "Plain text data"
hash_value = calculate_hash(text)
print(f"SHA-1 Hash of plaintext: {hash_value}")
# Fungsi: Menghitung hash dari data teks biasa.
# Kondisi: Saat Anda perlu menandai dan memvalidasi teks krusial.