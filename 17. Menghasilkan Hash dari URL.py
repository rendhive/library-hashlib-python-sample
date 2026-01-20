import hashlib

def generate_url_hash(url):
    return hashlib.sha256(url.encode()).hexdigest()

url = "https://www.example.com"
url_hash = generate_url_hash(url)
print(f"URL Hash: {url_hash}")
# Fungsi: Menghasilkan hash dari URL untuk identifikasi atau penyimpanan.
# Kondisi: Ketika Anda perlu menyimpan representasi hash dari URL untuk akses cepat.