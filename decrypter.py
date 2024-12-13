import os
import pyaes

def decrypter(dir):
    for item in os.listdir(dir):
        itempath = os.path.join(dir, item)

        if os.path.isdir(itempath):
            decrypter(itempath)
        elif os.path.isfile(itempath) and itempath.endswith(".desafioransomware"):
            with open(itempath, "rb") as file:
                file_data = file.read()

            key = b"desafioransomware"
            aes = pyaes.AESModeOfOperationCTR(key)

            decrypt_data = aes.decrypt(file_data)

            os.remove(itempath)
 
            newfile = itempath.replace(".desafioransomware", "")
            with open(newfile, "wb") as new_file:
                new_file.write(decrypt_data)

if __name__ == "__main__":
    dir = "./"
    decrypter(dir)
