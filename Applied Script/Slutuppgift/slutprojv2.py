import os
import argparse
from cryptography.fernet import Fernet

parser = argparse.ArgumentParser(description="""Krypteringsverktyg 5000
Änvändning:
                    py SCRIPT.py -f FILNAMN NYCKEL -m kryptera

                                 
Flaggor:
-c  --create_key    Skapa en ny krypteringsnyckel och spara den som en ny fil.
                                                                
-f  --files         Ange både filen du vill kryptera/dekryptera och nyckefilen i den givna ordningen.
                    Notera: Ange alltid filnamn först och sedan nyckelfil.
                                             
-o  --operation     Välj vilken funktion som ska användas.
                    "kryptera" för att kryptera den valda filen med nyckelfilen.
                    "dekryptera" för att dekryptera den valda filen med nyckelfilen.                      

                                 
Exempel på korrekta användningar:

Skapa ny nyckel:    py slutprojv2.py -c ny_nyckel.key

Kryptera en fil:    py slutprojv2.py -f testfil.txt test.key -o kryptera

Dekryptera en fil:  py slutprojv2.py -f testfil.txt test.key -o dekryptera""", 
epilog="Information finns ovan", formatter_class=argparse.RawDescriptionHelpFormatter)   


#### funktion för att skapa nyckel
def generate_key_mode(name_key_in_gkm):
    newkey = Fernet.generate_key()
    with open(name_key_in_gkm, "wb") as key_file:
        key_file.write(newkey)


#### funktion för att kryptera fil
def encrypt_and_store_info(file, key):
    with open(key, "rb") as key_file:
        key = key_file.read()                                                                               

    cipher_suite = Fernet(key)

    with open(file, "rb") as file_to_encrypt:                      
        content = file_to_encrypt.read()
        cipher_content = cipher_suite.encrypt(content)
        
        with open(file, "wb") as file_to_encrypt:
            file_to_encrypt.write(cipher_content)


#### funktion för att deryptera fil
def decrypt_and_store_info(file, key):
    with open(key, "rb") as key_file:
        key = key_file.read()

    cipher_suite = Fernet(key)

    with open(file, "rb") as file_to_decrypt:                      
        content = file_to_decrypt.read()
        cipher_content = cipher_suite.decrypt(content)
        
        with open(file, "wb") as file_to_decrypt:
            file_to_decrypt.write(cipher_content)


def main():

#### argument
    parser.add_argument("-c", "--create_key", metavar="Skapa ny nyckel", help="Skapa ny krypterinsnyckel")
    parser.add_argument("-f", "--files", metavar="Välj: FIL och välj: NYCKEL", nargs=2, type=str, help="Ange fil att kryptera/dekryptera och nyckelfil") 
    parser.add_argument("-o", "--operation", choices=["kryptera", "dekryptera"], help="Välj kryptering: kryptera eller dekryptera", type=str.lower)

    args = parser.parse_args()


####  if satser
    if args.create_key:

        if not os.path.exists(args.create_key):
            generate_key_mode(args.create_key)
            print(f"Nyckel {args.create_key} skapad")
        else:
            print(f"Nyckel {args.create_key} finns redan")


#### check av fil + kryptering eller dekryptering
    elif args.files and args.operation:

        if not os.path.exists(args.files[0]):
            print(f"Fil {args.files[0]} finns ej")
        if not os.path.exists(args.files[1]):
            print(f"Nyckelfil {args.files[1]} finns ej")
            return
        else:

            if args.operation == "kryptera":
                encrypt_and_store_info(args.files[0], args.files[1])
                print(f"Filen {args.files[0]} är krypterat")
                return
            if args.operation == "dekryptera":
                decrypt_and_store_info(args.files[0], args.files[1])
                print(f"Filen {args.files[0]} är dekrypterat") 
                return


#### felhantering
    elif args.files and not args.operation:
         print("Fel: Du behöver ange krypteringsläge '-o' och 'kryptera' eller 'dekryptera'") 

    elif args.operation and not args.files:
        print("Fel: Ange '-f' och 'fil att behandla' och 'nyckelfil'")    

if __name__ == "__main__":
    main()