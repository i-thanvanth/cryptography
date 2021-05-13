import os
print("WELCOME TO T'S ASYMMETRIC KEY ENCRYPTION\DECRYPTION APP!")
#installing the required packages...
print("\nInstalling the required packages...","\n")
os.system('pip install pycryptodome')
from Crypto.PublicKey import RSA
def func():
    print("\n Choose one from the following options","\n 1) Create new private and public keys (ONLY USE IT THE FIRST TIME)","\n 2) Encrypt\Decrypt text files","\n 3) EXIT")
    option = int(input("Enter your option:"))
    if option == 1:
        private_key = RSA.generate(2048)
        f = open("pri_key.pem", "wb")
        f.write(private_key.export_key())
        f.close()
        f = open("pub_key.pem", "wb")
        f.write(private_key.publickey().export_key())
        f.close()
        func()
    elif option == 2:
        os.system("python encrypt_text.py")
    elif option == 3:
        print("Thanks for using T's app")
    return None
func()