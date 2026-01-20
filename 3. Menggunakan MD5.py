import hashlib

def md5_hash(data):
    return hashlib.md5(data.encode()).hexdigest()

result = md5_hash("Hello, World!")
print(f"MD5: {result}")
# Fungsi: Menghasilkan hash MD5 dari string input.
# Kondisi: Ketika Anda ingin melakukan checksum atau validasi data (perhatikan bahwa MD5 tidak dianggap aman).