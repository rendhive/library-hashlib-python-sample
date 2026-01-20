import hashlib

def save_hash(data, filename):
    hash_value = hashlib.sha256(data.encode()).hexdigest()
    with open(filename, 'w') as f:
        f.write(hash_value)

data = "Critical Data"
save_hash(data, "data_hash.txt")
print("Hash saved to data_hash.txt")
# Fungsi: Menyimpan hash ke dalam file untuk verifikasi di kemudian hari.
# Kondisi: Ketika Anda perlu membandingkan data dengan hash untuk keaslian.