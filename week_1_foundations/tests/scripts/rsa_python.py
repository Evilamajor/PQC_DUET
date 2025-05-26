import random
from math import gcd

# --- Step 1: Check for Primality (Naive) ---
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# --- Step 2: Generate Small Random Prime (for testing) ---
def generate_prime(start=100, end=300):
    while True:
        p = random.randint(start, end)
        if is_prime(p):
            return p

# --- Step 3: Extended Euclidean Algorithm ---
def modinv(a, m):
    r1, r2 = a, m
    t1, t2 = 1, 0
    while r2 != 0:
        q = r1 // r2
        r1, r2 = r2, r1 - q * r2
        t1, t2 = t2, t1 - q * t2
    return t1 % m

# --- Step 4: Key Generation ---
def generate_keys():
    p = generate_prime()
    q = generate_prime()
    while q == p:
        q = generate_prime()
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    if gcd(e, phi) != 1:
        e = 3
        while gcd(e, phi) != 1:
            e += 2
    d = modinv(e, phi)
    return (n, e), (n, d)

# --- Step 5: Encrypt & Decrypt ---
def encrypt(m, public_key):
    n, e = public_key
    return pow(m, e, n)

def decrypt(c, private_key):
    n, d = private_key
    return pow(c, d, n)

# --- Demo ---
if __name__ == "__main__":
    pub, priv = generate_keys()
    message = 42
    print("Public Key:", pub)
    print("Private Key:", priv)

    cipher = encrypt(message, pub)
    print("Encrypted:", cipher)

    decrypted = decrypt(cipher, priv)
    print("Decrypted:", decrypted)


