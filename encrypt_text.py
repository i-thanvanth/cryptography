from Crypto.PublicKey import RSA
print("Choose from the following...","\n")
pr_key = RSA.import_key(open('pri_key.pem', 'r').read())
pu_key = RSA.import_key(open('pub_key.pem', 'r').read())
print("The pr key is: ",pr_key.exportKey(),"\n The pu key is: ", pu_key.exportKey())

