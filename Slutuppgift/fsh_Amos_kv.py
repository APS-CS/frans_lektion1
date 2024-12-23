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
                    py SCRIPT.py -f FILNAMN -k NYCKEL -e/d

                                 
Flaggor:
-c  --create_key    Skapa en ny krypteringsnyckel och spara den som en ny fil.
                                                          
-f  --files         Ange filen du vill kryptera/dekryptera.
                    Notera: Krypterar inte '.enc'.filer och dekrypterar inte annat än '.enc' filer.
                                 
-e  --encrypt       Välj '-e' för att kryptera den valda filen med den valda nyckelfilen
                    Notera: En krypterad kopia med filtyp 'FILNAMN.FILTYP.enc' skapas i den aktuella sökvägen.
                                 
-d  --decrypt       Välj '-d' för att dekryptera den valda filen med den valda nyckelfilen.
                    Notera: En dekrypterad kopia med filanamn 'dekrypterad_FILNAMN.FILTYP' skapas i den aktuella sökvägen.
                                                   
-k  --key           Ange nyckelfilen du vill använda för att kryptera/dekryptera.

                                 
Exempel på korrekta användningar:

Skapa ny nyckel:    py fsh_Amos_kv.py -c ny_nyckel.key

Kryptera en fil:    py fsh_Amos_kv.py -f testfil.txt -k test.key -e

Dekryptera en fil:  py fsh_Amos_kv.py -f testfil.txt -k test.key -d""", 
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
    parser.add_argument("-c", "--create_key", metavar="Skapa ny nyckel", help="Skapa ny krypterinsnyckel.")
    parser.add_argument("-f", "--file", metavar="Välj: FIL ", type=str, help="Ange fil att kryptera/dekryptera.") 
    parser.add_argument("-k", "--key", metavar="Välj: NYCKEL ", type=str, help="Ange nyckelfil för kryptera/dekryptera fil.") 

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-e", "--encrypt", action="store_true", help="Välj för kryptering.")
    group.add_argument("-d", "--decrypt", action="store_true", help="Välj för dekryptering.")

    args = parser.parse_args()

####  if satser
    if len(os.sys.argv) == 1:           ####fick hjälp av Yaraslau med kod rad 98-100
        parser.print_help()
        return

    if args.create_key:
        if not os.path.exists(args.create_key):
            generate_key_mode(args.create_key)
            print(f"Nyckel {args.create_key} skapad.")
        else:
            print(f"Nyckel {args.create_key} finns redan.")

#### kontroll
    if (args.file and args.key) and not (args.encrypt or args.decrypt):
        print("Fel: Du behöver ange krypteringsläge '-e' eller '-d'.")
        return

#### check av fil
    if args.file and (args.decrypt or args.encrypt):
        if not os.path.exists(args.file):
            print(f"Fil {args.file}finns ej.")
            return
        excisting_file = args.file
    else:
        print("Fel: ingen fil angiven. Ange '-f' och fil.")
        return

#### check av nyckel
    if args.key and (args.decrypt or args.encrypt):
        if not os.path.exists(args.key):
            print(f"Nyckelfil {args.key}finns ej.")
            return
        excisting_key = args.key
    else:
        print("Fel: ingen nyckel angiven. Ange '-k' och nyckelfil.")
        return
             
#### Kryptering/dekryptering
    if args.encrypt:
        if excisting_file.endswith(".enc"):
            print(f"Filen {excisting_file} är redan krypterat.")
        else:
            encrypt_and_store_info(excisting_file, excisting_key)
            print(f"Filen {excisting_file} är krypterat.")
        
    if  args.decrypt:
        if not excisting_file.endswith(".enc"):
            print(f"Filen {excisting_file} är redan dekrypterat.")
        else:
            decrypt_and_store_info(excisting_file, excisting_key)
            print(f"Filen {excisting_file} är dekrypterat.")




if __name__ == "__main__":
    main()