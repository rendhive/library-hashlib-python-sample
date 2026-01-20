import hashlib

def hash_file(filename):
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# Ubah 'example.txt' ke nama file yang ingin diuji
print(f"MD5 Hash of the file: {hash_file('example.txt')}")
# Fungsi: Menghasilkan hash untuk konten file.
# Kondisi: Ketika Anda perlu memverifikasi integritas dan keaslian file.