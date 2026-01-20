import hashlib

def verify_file_integrity(filepath, expected_hash):
    hash_md5 = hashlib.md5()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest() == expected_hash

# Ubah 'example.txt' dan '<expected_hash>' ke yang sesuai
if verify_file_integrity('example.txt', '<expected_hash>'):
    print("File integrity OK.")
else:
    print("File integrity failed.")
# Fungsi: Memverifikasi integritas file dengan hash yang diharapkan.
# Kondisi: Ketika Anda perlu memastikan file tidak diubah atau rusak.