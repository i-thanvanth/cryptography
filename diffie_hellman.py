import os
print("INSTALLING THE REQUIRED PACKAGES!","\n--------------------------------") 
os.system("pip install sympy") #FOR GENERATING PSEUDORANDOM PRIME NUMBERS
os.system("pip install pycryptodome")
print("\n--------------------------------")
import sympy
import random 
generator = sympy.randprime(100,200)
mod = sympy.randprime(random.getrandbits(500),random.getrandbits(512))
print("\n--------------------------------","\nThe generator is: ", generator,"\n the mod value is: ", mod,"\n--------------------------------")
a_private = random.getrandbits(512)
a_public = pow(generator, a_private, mod)
print("\n--------------------------------","Generating the public keys from A's and B's private keys","\nA's public key is: ", a_public)
b_private = random.getrandbits(512)
b_public = pow(generator, b_private, mod)
print("B's public key is: ", b_public,"\n--------------------------------")
a_sharedKey = pow(b_public, a_private, mod)
b_sharedKey = pow(a_public, b_private, mod)
print("\n--------------------------------","\nA's shared key is: ", a_sharedKey)
print("B's shared key is: ", b_sharedKey,"\n--------------------------------")
print("\n NOW A AND B BOTH HAVE THE SAME SHARED KEY WITHOUT ACTUALLY SHARING THEIR PRIVATE KEYS IN THE PUBLIC")
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
nonce = get_random_bytes(15)
cipher = AES.new(bytes(str(a_sharedKey)[0:32],'utf-8'),AES.MODE_EAX,nonce=nonce)
print("\n--------------------------------")
message = bytes(input("Enter a string to help T demonstrate the encryption and decryption after the key exchange: "),'utf-8')
print("\n Encrypting the key with the A's shared key...")
ciphertext = cipher.encrypt(message)
print("\n the ciphertext is:", ciphertext)
print("\n Decrypting the key with B's shared key...")
decryptor = AES.new(bytes(str(b_sharedKey)[0:32],'utf-8'),AES.MODE_EAX,nonce=nonce)
decrypted_text = decryptor.decrypt(ciphertext)
print("\nthe decrypted text is:", decrypted_text.decode())



