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
    parser.add_argument("-f", "--files", metavar="Välj: FIL", type=str, help="Ange fil att kryptera/dekryptera") 
    parser.add_argument("-k", "--key", metavar="Välj: NYCKEL", type=str, help="Ange nyckelfil för kryptera/dekryptera fil") 

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-e", "--encrypt", action="store_true", help="Välj för kryptering")
    group.add_argument("-d", "--decrypt", action="store_true", help="Välj för dekryptering")

    args = parser.parse_args()

####  if satser
    if len(os.sys.argv) == 1:           ####fick hjälp av Yaraslau med kod rad 79-83
        parser.print_help()

    if args.create_key:

        if not os.path.exists(args.create_key):
            generate_key_mode(args.create_key)
            print(f"Nyckel {args.create_key} skapad")
        else:
            print(f"Nyckel {args.create_key} finns redan")

#### check av fil
    if args.files and (args.decrypt or args.encrypt):
        if not os.path.exists(args.files):
            print(f"Fil {args.files}finns ej")
            return

        print("kommer det hit fil?")
        excisting_file = args.files

    else:
        print("Fel: ingen nyckel angiven")
        return


#### check av nyckel
    if args.key and (args.decrypt or args.encrypt):
        if not os.path.exists(args.key):
            print(f"Nyckelfil {args.key + " "}finns ej")
            return

        print("kommer det hit nyckel?")
        excisting_key = args.key

    else:
        print("Fel: ingen fil angiven'")
             

#### Kryptering/dekryptering
    if args.encrypt:
            encrypt_and_store_info(excisting_file, excisting_key)
            print(f"Filen {excisting_file} är krypterat")

    if  args.decrypt:
        decrypt_and_store_info(excisting_file, excisting_key)
        print(f"Filen {excisting_file} är dekrypterat") 

    elif args.files and args.key and not args.encrypt or args.decrypt:
            print("Fel: Du behöver ange krypteringsläge '-e' eller '-d'") 



if __name__ == "__main__":
    main()