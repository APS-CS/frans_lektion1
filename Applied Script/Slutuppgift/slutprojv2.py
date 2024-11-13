import os
import argparse
from cryptography.fernet import Fernet

parser = argparse.ArgumentParser(description="Krypteringsverktyg 5000. exempel inmatning: -f [filnamn] [nyckel] -m VÄLJ [kryptera] ELLER [dekryptera].", epilog="Information i ovan description")   


#### funktion för att skapa nyckel
def generate_key_mode(name_key_in_gkm):
    newkey = Fernet.generate_key()
    print(f"Nyckel {newkey} skapat i RAM - great success! \n")                            #### Bekräftelse
    with open(name_key_in_gkm, "wb") as key_file:
        key_file.write(newkey)
        print("Nyckel skapat i fil - great success! \n")                        #### Bekräftelse


#### funktion för att kryptera fil
def encrypt_and_store_info(file, key):
    with open(key, "rb") as key_file:
        key = key_file.read()                                                                               
        print(f"Nyckel {key} öppnat i RAM - success! KRYPTERING")           #### Bekräftelse

    cipher_suite = Fernet(key)

    with open(file, "rb") as file_to_encrypt:                      
        content = file_to_encrypt.read()
        cipher_content = cipher_suite.encrypt(content)
        
        with open(file, "wb") as file_to_encrypt:
            file_to_encrypt.write(cipher_content)
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
        
        with open(file, "wb") as file_to_decrypt:
            file_to_decrypt.write(cipher_content)
            print(f"Innehåll i fil: {file} är dekrypterad - GREAT SUCCESS \n")  #### Bekräftelse



def main():

#### argument
    parser.add_argument("-c", "--create_key", metavar="Skapa ny nyckel", help="Skapa ny krypterinsnyckel")
    parser.add_argument("-f", "--files", metavar="Välj: FIL och välj: NYCKEL", nargs=2, type=str, help="Ange fil att kryptera/dekryptera och nyckelfil") 
    parser.add_argument("-o", "--operation", choices=["kryptera", "dekryptera"], help="Välj kryptering: kryptera eller dekryptera", type=str.lower)

    args = parser.parse_args()



####  if satser
    if args.create_key:
        print("generate_key_mode()- MODE AKTIVERAD\n")                                  #### Bekräftelse

        if not os.path.exists(args.create_key):
            generate_key_mode(args.create_key)
            print(f"Nyckel {args.create_key} skapad")                               #### Bekräftelse
        else:
            print(f"Nyckel {args.create_key} finns redan")


#### check av fil + kryptering eller dekryptering
    elif args.files and args.operation:
        print("fil hantering- MODE AKTIVERAD\n")                             #### Bekräftelse

        if not os.path.exists(args.files[0]):
            print(f"Fil {args.files[0]} finns ej")
            return
        if not os.path.exists(args.files[1]):
            print(f"Nyckelfil {args.files[1]} finns ej")
            return
        else:
            print("Crypt MODE AKTIVERAD\n")                             #### Bekräftelse
            if args.operation == "kryptera":
                encrypt_and_store_info(args.files[0], args.files[1])
                print("Filen är krypterat")                                        #### Bekräftelse
                return
            if args.operation == "dekryptera":
                decrypt_and_store_info(args.files[0], args.files[1])
                print("Filen är dekrypterat") 
                return


#### felhantering
    elif args.files and not args.operation:
         print("Fel: Du behöver ange krypteringsläge '-o' och 'kryptera' eller 'dekryptera'") 

    elif args.operation and not args.files:
        print("Fel: Ange '-f' och 'fil att behandla' och 'nyckelfil'")    



if __name__ == "__main__":
    main()