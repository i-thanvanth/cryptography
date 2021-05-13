from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
key = open('key.pem', 'rb').read()
nonce = get_random_bytes(15)
def func():
    print("\n\n Choose from the following...","\n 1) Encrypt text","\n 2) Decrypt text","\n 3) EXIT")
    option=int(input("Enter your option:"))
    if option == 1:
        cipher = AES.new(key, AES.MODE_EAX, nonce = nonce)
        message = bytes(input("ENTER THE STRING TO BE ENCRYPTED: "),'utf-8')
        encrypted_text = cipher.encrypt(message)
        print("\n",encrypted_text)
        f = open("encrypted_text.txt", "wb")
        f.write(encrypted_text)
        f.close()
        print(" The encrypted text will be written in a text file called encrypted_text.txt \n USE THE PUBLIC KEY TO ENCRYPT THE FILES","\n SEND THE PRIVATE KEY 'ONLY TO THE RECIPIENTS' ")
        func()
    if option == 2:
        decrypt = AES.new(key, AES.MODE_EAX, nonce = nonce)
        f = open(input("Enter the path of the file with the encrypted text: "), "rb")
        encrypted_text=f.read()
        f.close()
        decrypted_text = decrypt.decrypt(encrypted_text)
        print("\nThe decrypted message is: ",str(decrypted_text))
        func()
    if option == 3:
        print("Thanks for using this app!")
func()
