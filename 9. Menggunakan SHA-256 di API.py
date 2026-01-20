import hashlib

def generate_api_key(user_id):
    return hashlib.sha256(user_id.encode()).hexdigest()

user_id = "user1234"
api_key = generate_api_key(user_id)
print(f"API Key: {api_key}")
# Fungsi: Menghasilkan kunci API unik berdasarkan ID pengguna.
# Kondisi: Ketika Anda perlu membuat kunci API yang aman untuk akses pengguna.