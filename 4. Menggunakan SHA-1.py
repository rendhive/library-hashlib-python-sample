import hashlib

def sha1_hash(data):
    return hashlib.sha1(data.encode()).hexdigest()

result = sha1_hash("Hello, World!")
print(f"SHA-1: {result}")
# Fungsi: Menghasilkan hash SHA-1 dari string input.
# Kondisi: Ketika Anda ingin menggunakan algoritma hashing yang lebih aman dibandingkan MD5, tetapi tidak sepenuhnya aman.