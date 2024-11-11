import os

import argparse
parser = argparse.ArgumentParser(description="Krypteringsverktyg \n 5000", epilog="EPILOG TEXT, EPILOG TEXT, EPILOG TEXT")   

from cryptography.fernet import Fernet


#### funktion för att skapa nyckel
def generate_key_mode(name_key_in_gkm):                                                #### funktionen skapar ny nykel.. hur använda en nyckel som är redan skapad?
    newkey = Fernet.generate_key()
    print(f"Nyckel {newkey} skapat i RAM - great success! \n")                            #### Bekräftelse
    with open(name_key_in_gkm, "wb") as key_file:                                      #### kan nu spara ny nyckel
        key_file.write(newkey)
        print("Nyckel skapat i fil - great success! \n")                        #### Bekräftelse


#### funktion för att kryptera fil
def encrypt_and_store_info(file, key):
    with open(key, "rb") as key_file:                                       #### Öppnar med vald nyckel
        key = key_file.read()                                                                               
        print(f"Nyckel {key} öppnat i RAM - success! KRYPTERING")           #### Bekräftelse

    cipher_suite = Fernet(key)

    with open(file, "rb") as file_to_encrypt:                      
        content = file_to_encrypt.read()
        cipher_content = cipher_suite.encrypt(content)
        
        with open(file, "wb") as file_to_encrypt:                           #### måste skriva över, går inte att använda rb+
            file_to_encrypt.write(cipher_content)                                   #### pröva sen med att anävnda rb+ är det plain text + cipher text som ligger i filen då?
            print(f"Innehåll i fil {file} är krypterad - GREAT SUCCESS \n")    #### Bekräftelse


#### funktion för att deryptera fil
def decrypt_and_store_info(file, key):
    with open(key, "rb") as key_file:
        key = key_file.read()
        print(f"Nyckel {key} öppnat i RAM - success! DEKRYPTERING \n")         #### Bekräftelse

    cipher_suite = Fernet(key)

    with open(file, "rb") as file_to_decrypt:                      
        content = file_to_decrypt.read()
        cipher_content = cipher_suite.decrypt(content)
        
        with open(file, "wb") as file_to_decrypt:                           #### Pröva copy pasta ovan men byter ut variabler och funktioner
            file_to_decrypt.write(cipher_content)
            print(f"Innehåll i fil: {file} är dekrypterad - GREAT SUCCESS \n")  #### Bekräftelse



#### Dags att bygga args :D
#### lektion 2024-11-11 - allt ska göras via argsparse

parser.add_argument("-c", "--create_key", action="store_true", help="Kommando för att ska ny krypterinsnyckel")

parser.add_argument("-e", "--encrypt_file", action="store_true", help="Kommando för att kryptera fil")

parser.add_argument("-d", "--decrypt_file", action="store_true", help="Kommando för att dekryptera fil")

parser.add_argument("-f", "--file_to_modify", metavar="Fil att behandla", type=str, help="Kommando för att välja fil att behandla") 

parser.add_argument("-en", "--action", metavar="Välj att kryptera", type="str", )

args = parser.parse_args()          #### tsm argparse.ArgumentParser aktiverar argsparse I guess



#### If-satserna

if args.create_key:
    print("generate_key_mode()- MODE AKTIVERAD\n")                                  #### Bekräftelse
    name_key = input("Skapa nyckel: ")
    
    if not os.path.exists(name_key):
        generate_key_mode(name_key)

        print(f"Nyckel {name_key} skapad - Programmet stängs")                               #### Bekräftelse
    else:
        print(f"Nyckel {name_key} finns redan - Programmet stängs")  
    


if args.encrypt_file and args.file_to_modify:
    print("Encrypt_and_store_info()- MODE AKTIVERAD\n")                             #### Bekräftelse

    if not os.path.exists(args.file_to_modify):
        print(f"Fil {args.file_to_modify} finns ej")
        
    else:
        key = input("Välj nyckel:")
        encrypt_and_store_info(args.file_to_modify, key)
        print("Filen är krypterat - Programmet stängs")                                        #### Bekräftelse      
    
    print("Programmet stängs")                                        #### Bekräftelse




if args.decrypt_file and args.file_to_modify:
    print("Decrypt_and_store_info()- MODE AKTIVERAD\n")                             #### Bekräftelse

    if not os.path.exists(args.file_to_modify):
        print(f"Fil {args.file_to_modify} finns ej")
        
    else:
        key = input("Välj nyckel:")
        decrypt_and_store_info(args.file_to_modify, key)
        print("Filen är dekrypterat - Programmet stängs")                                        #### Bekräftelse

    print("Programmet stängs")
