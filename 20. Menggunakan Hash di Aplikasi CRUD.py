import hashlib

def create_entry(data):
    entry_hash = hashlib.sha256(data.encode()).hexdigest()
    return {"data": data, "hash": entry_hash}

entry = create_entry("User data")
print(f"Entry: {entry}")
# Fungsi: Menghasilkan dan menyimpan hash saat membuat entri data baru.
# Kondisi: Ketika Anda perlu memastikan integritas data dalam operasi CRUD.