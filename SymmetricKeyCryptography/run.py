import os
print("WELCOME TO T'S SYMMETRIC KEY ENCRYPTION\DECRYPTION APP!")
#installing the required packages...
print("\nInstalling the required packages...","\n")
os.system('pip install pycryptodome')
from Crypto.Random import get_random_bytes
def func():
    print("\n Choose one from the following options","\n 1) Create new public key (ONLY USE IT THE FIRST TIME)","\n 2) Encrypt\Decrypt text files","\n 3) EXIT")
    option = int(input("Enter your option:"))
    if option == 1:
        key = get_random_bytes(32)
        print("The key is: ", key,"\n The key will be stored in a file called key.pem")
        f = open("key.pem", "wb")
        f.write(key)
        f.close()        
        func()
    elif option == 2:
        os.system("python encrypt_text.py")
    elif option == 3:
        print("Thanks for using T's app")
    return None
func()