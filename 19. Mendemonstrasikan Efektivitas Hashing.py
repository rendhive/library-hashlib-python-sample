import hashlib

def demonstrate_hashing(input_string):
    print(f"Original: {input_string}")
    print(f"MD5: {hashlib.md5(input_string.encode()).hexdigest()}")
    print(f"SHA-1: {hashlib.sha1(input_string.encode()).hexdigest()}")
    print(f"SHA-256: {hashlib.sha256(input_string.encode()).hexdigest()}")

demonstrate_hashing("demonstration")
# Fungsi: Demo untuk menunjukkan perbedaan hasil hashing dari beragam algoritma.
# Kondisi: Ketika Anda ingin memahami bagaimana hashing berfungsi dengan data asli.