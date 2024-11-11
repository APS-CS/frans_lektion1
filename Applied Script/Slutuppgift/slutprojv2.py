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

# parser.add_argument("-e", "--encrypt_file", action="store_true", help="Kommando för att kryptera fil")

# parser.add_argument("-d", "--decrypt_file", action="store_true", help="Kommando för att dekryptera fil")


parser.add_argument("-c", "--create_key", metavar="Ny krypteringsnyckel", help="Skapa ny krypterinsnyckel")

parser.add_argument("-k", "--key_choice", metavar="Krypteringsnyckel", help="Nyckel att använda")

parser.add_argument("-f", "--file_to_modify", metavar="Fil", type=str, help="Fil att behandla") 

parser.add_argument("-m", "--crypmode", metavar="Välj funktion", choices=["kryptera", "dekryptera"], help="Välj <kryptera> eller <dekryptera> för behandling av fil", type=str.lower)


args = parser.parse_args()



#### If-satserna

if args.create_key:
    print("generate_key_mode()- MODE AKTIVERAD\n")                                  #### Bekräftelse
    # name_key = input("Skapa nyckel: ")
    
    if not os.path.exists(args.create_key):
        generate_key_mode(args.create_key)
        print(f"Nyckel {args.create_key} skapad")                               #### Bekräftelse
    else:
        print(f"Nyckel {args.create_key} finns redan")


if args.key_choice:
    print("chose_key_mode()- MODE AKTIVERAD\n")                                  #### Bekräftelse
    if os.path.exists(args.key_choice):
        key = args.key_choice
        print(f"Nyckel finns: {args.key_choice}")
    else:
        print(f"Fil {args.key_choice} finns ej")
        exit()
        print("Programmet stängs")                                        #### Bekräftelse




if args.crypmode == "kryptera" and args.file_to_modify:
    print("Encrypt_and_store_info()- MODE AKTIVERAD\n")                             #### Bekräftelse

    if not os.path.exists(args.file_to_modify):
        print(f"Fil {args.file_to_modify} finns ej")
    else:
        # key = input("Välj nyckel:")
        encrypt_and_store_info(args.file_to_modify, key)
        print("Filen är krypterat")                                        #### Bekräftelse      
    


if args.crypmode == "dekryptera"  and args.file_to_modify:
    print("Decrypt_and_store_info()- MODE AKTIVERAD\n")                             #### Bekräftelse

    if not os.path.exists(args.file_to_modify):
        print(f"Fil {args.file_to_modify} finns ej")
        
    else:
        # key = input("Välj nyckel:")
        decrypt_and_store_info(args.file_to_modify, key)
        print("Filen är dekrypterat")                                        #### Bekräftelse
