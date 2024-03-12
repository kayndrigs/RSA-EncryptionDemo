import random
import math

def is_prime(number):
    if number < 2:
        return False
    for i in range (2, number // 2 + 1):
        if number % i == 0:
            return False
    return True

def generate_prime(min_value, max_value):
    prime = random.randint(min_value, max_value)
    while not is_prime(prime):
        prime = random.randint(min_value, max_value)
    return prime

def mod_inverse(e, phi):
    for d in range(3, phi):
        if (d * e) % phi == 1:
            return d
    raise ValueError('Modular inverse does not exist')

p, q = generate_prime(1000, 5000), generate_prime(1000, 5000)

while p == q:
    q = generate_prime(1000, 5000)
    
n = p * q

phi_n = (p - 1) * (q - 1)

e = random.randint(3, phi_n-1)

while math.gcd(e, phi_n) != 1:
    e = random.randint(3, phi_n-1)
    
d = mod_inverse(e, phi_n)


print("Public Key: ", e)
print("Private Key: ", d)
print("Modulus: ", n)
print("Phi of n: ", phi_n)
print("p: ", p)
print("q: ", q)

message = "Hello World"

message_encoded = [ord(char) for char in message]
# (m ^ e) mod n = c
ciphertext = [pow(char, e, n) for char in message_encoded]

message_encoded = [pow(char, d, n) for char in ciphertext]
message = "".join(chr(ch) for ch in message_encoded)

print(message)