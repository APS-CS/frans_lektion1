################ Projekt Frans Schartaus ################

## Skapa ett verktyg som kan:

## Generera och spara en krypteringsnyckel. > SE ENCRPYT.PY

## Kryptera en given fil med hjälp av en symmetrisk nyckel. 

## Dekryptera en krypterad fil med rätt nyckel.

## Använd cryptography-biblioteket (Fernet rekommenderas) 

## Använd argparsebiblioteket för att ta argument

## Krav:
## Implementera ett skript som använder argparse för att hantera
## kommandoradsalternativ och utför följande funktioner:

## Generera en symmetrisk nyckel och spara den i en fil.

## Kryptera en fil med en befintlig nyckel.

## Dekryptera en krypterad fil och återställa originalet.

################ Plan för uppgiften ################

#### Fernet
## skapa skript som gör krypteringsprocedur, ha samma fil som avkrypterar

## skapa funktion för att skapar nyckel - CHECK
## skapa funktion för att kryptera - CHECK
## skapa funktion för att dekryptera - CHECK


#### FRÅGOR och SVAR: vad händer med plaintext och enc fil? Ta vi bort? ersätter hela filen? är den redan krypterad? - Svar: Ja, du krypterar bytes och därmed innehåll, det är inte en åtkomst till fil du blockarar utan klar läsning av innehåll

#### FRÅGOR och SVAR: Kan det bli dubbelkryp? - Ja! Inga problem om samma krypnyckel används, problem om man kopierar över med ny kryp men har inte var den gamla

#### FRÅGOR: Hur göra om flera filer? Krypera med bara en nyckel? Skapa en ny nyckel varje gång? Svar: Problem kommer upp! gör commit på det

#### Argparse
## Det ska vara argparse som tar in fil i skripten krypterar/dekrypterar

## 1. Krypera - CHECK
## 1a. Ange fil -> Bekräftelse
## 1a. Ange fil -> Fil redan kryperad?

## 2. Dekryptera - CHECK
## 2a. Ange fil -> Bekräftelse
## 2a. Ange fil -> Fil redan kryperad? 

## 3. Skapa nyckel - CHECK 
## 3a. Få Bekräftelse 


#### FRÅGOR: Hur ange filnamn som ska de/krypteras? 


#### Om tid finns: 
## skapa (i skripten) funktion för felmeddelande, tex om filen redan är krypterad eller om filen redan av avkrypterad
## köra skripten och skapa ny nyckel


################ Ain't nuttin but to do it!! ################
## impertera os åtkomst
import os

##importera argparse
import argparse
parser = argparse.ArgumentParser(description="Krypteringsverktyg 5000", epilog="EPILOG TEXT, EPILOG TEXT, EPILOG TEXT")   

##importera Fernet
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

parser.add_argument("-c", "--create_key", action="store_true", help="Skapa krypteringsnyckel")

parser.add_argument("-e", "--encrypt_file", action="store_true", help="kommando att kryptera fil")

parser.add_argument("-d", "--decrypt_file", action="store_true", help="Filen dekrypteras")

parser.add_argument("-f", "--file_to_modify", type=str, help="Ange fil") 

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




# elif args.filename:
#     filename_to_store = args.filename
#     open(filename_to_store, "w")
#     print(f"Fil {filename_to_store} skapad")
