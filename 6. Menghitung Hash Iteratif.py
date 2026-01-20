import hashlib

def iterative_hash(data, iterations):
    hash_value = data.encode()
    for _ in range(iterations):
        hash_value = hashlib.sha256(hash_value).digest()
    return hash_value.hex()

result = iterative_hash("Hello, World!", 1000)
print(f"Iterative SHA-256: {result}")
# Fungsi: Menghasilkan hash dengan iterasi untuk keamanan yang lebih baik.
# Kondisi: Ketika Anda ingin meningkatkan keamanan dengan melakukan hashing berulang kali.