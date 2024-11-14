import os
import argparse
from cryptography.fernet import Fernet

parser = argparse.ArgumentParser(description=r"""
 _  __                 _                      _    _
| |/ /_ __ _   _ _ __ | |_    __   _____ _ __| | _| |_ _   _  __ _                                                                                                                     
| ' /| '__| | | | '_ \| __|___\ \ / / _ \ '__| |/ / __| | | |/ _` |                                                                                                                    
| . \| |  | |_| | |_) | ||_____\ V /  __/ |  |   <| |_| |_| | (_| |                                                                                                                    
|_|\_\_|   \__, | .__/ \__|     \_/ \___|_|  |_|\_ \__|\__, |\__, |                                                                                                                    
           |___/|_|                                    |___/ |___/                                                                                                                     
 ____   ___   ___   ___
| ___| / _ \ / _ \ / _ \ 
|___ \| | | | | | | | | |
 ___) | |_| | |_| | |_| |
|____/ \___/ \___/ \___/


                                 
Änvändning:
                    py SCRIPT.py -f FILNAMN NYCKEL -e/d

                                 
Flaggor:
-c  --create_key    Skapa en ny krypteringsnyckel och spara den som en ny fil.
                                                          
-f  --files         Ange både filen du vill kryptera/dekryptera och nyckefilen i den givna ordningen.
                    Notera: Ange alltid filnamn först och sedan nyckelfil.
                                 
-e  --encrypt       Välj '-e' för att kryptera den valda filen med den valda nyckelfilen
                    Notera: En krypterad kopia med filtyp 'FILNAMN.FILTYP.enc' skapas i den aktuella sökvägen
                                 
-d  --decrypt       Välj '-d' för att dekryptera den valda filen med den valda nyckelfilen
                    Notera: En dekrypterad kopia med filanamn 'dekrypterad_FILNAMN.FILTYP' skapas i den aktuella sökvägen                    

                                 
Exempel på korrekta användningar:

Skapa ny nyckel:    py slutprojv2.py -c ny_nyckel.key

Kryptera en fil:    py slutprojv2.py -f testfil.txt test.key -e

Dekryptera en fil:  py slutprojv2.py -f testfil.txt test.key -d""", 
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
        
        encrypted_file = file + ".enc"
        with open(encrypted_file, "wb") as file_to_encrypt:
            file_to_encrypt.write(cipher_content)

#### funktion för att deryptera fil
def decrypt_and_store_info(file, key):
    with open(key, "rb") as key_file:
        key = key_file.read()

    cipher_suite = Fernet(key)

    with open(file, "rb") as file_to_decrypt:                      
        content = file_to_decrypt.read()
        cipher_content = cipher_suite.decrypt(content)
        
        decrypted_file = "dekrypterat_" + file.replace(".enc", "")
        with open(decrypted_file, "wb") as file_to_decrypt:
            file_to_decrypt.write(cipher_content)

def main():

#### argument
    parser.add_argument("-c", "--create_key", metavar="Skapa ny nyckel", help="Skapa ny krypterinsnyckel")
    parser.add_argument("-f", "--files", metavar="Välj: FIL och välj: NYCKEL", nargs=2, type=str, help="Ange fil att kryptera/dekryptera och nyckelfil") 

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-e", "--encrypt", action="store_true", help="Välj för kryptering")
    group.add_argument("-d", "--decrypt", action="store_true", help="Välj för dekryptering")

    args = parser.parse_args()

####  if satser
    if len(os.sys.argv) == 1:           ####fick hjälp av Yaraslau med kod rad 79-83
        parser.print_help()

    elif args.create_key:

        if not os.path.exists(args.create_key):
            generate_key_mode(args.create_key)
            print(f"Nyckel {args.create_key} skapad")
        else:
            print(f"Nyckel {args.create_key} finns redan")

#### check av fil + kryptering eller dekryptering
    elif args.files and args.decrypt or args.encrypt:
        if not os.path.exists(args.files[0]):
            print(f"Fil {args.files[0]} finns ej")
        elif not os.path.exists(args.files[1]):
            print(f"Nyckelfil {args.files[1]} finns ej")
            return
        
        else:
            if args.encrypt:
                encrypt_and_store_info(args.files[0], args.files[1])
                print(f"Filen {args.files[0]} är krypterat")
            elif args.decrypt:
                decrypt_and_store_info(args.files[0], args.files[1])
                print(f"Filen {args.files[0]} är dekrypterat") 

#### mer felhantering
    elif args.files and not args.encrypt or args.decrypt:
         print("Fel: Du behöver ange krypteringsläge '-e' eller '-d'") 

    elif args.encrypt or args.decrypt and not args.files:
        print("Fel: Ange '-f' och 'fil att behandla' och 'nyckelfil'")    

if __name__ == "__main__":
    main()