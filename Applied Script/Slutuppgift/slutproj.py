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
import pyfiglet

##importera argparse
import argparse
parser = argparse.ArgumentParser(description="Krypteringsverktyg 5000", epilog="EPILOG TEXT, EPILOG TEXT, EPILOG TEXT")   

##importera Fernet
from cryptography.fernet import Fernet


#### funktion för at skapa nyckel
def generate_key_mode():                                                  ####funktionen skapar ny nykel.. hur använda en nyckel som är redan skapad?
    newkey = Fernet.generate_key()
    print("Nyckel skapat i RAM - great success! \n")                            ####Bekräftelse

    with open("crypto_key.key", "wb") as key_file:                              ####Förvald crypto_key.key
        key_file.write(newkey)
        print("Nyckel skapat i fil - great success! \n")                        ####Bekräftelse


#### funktion för att kryptera fil
def encrypt_and_store_info():
    with open("crypto_key.key", "rb") as key_file:
        key = key_file.read()                                                    #### öppnar förvald crypto_key.key                            
        print("Nyckel öppnat i RAM - success! KRYPTERING")                       #### Bekräftelse

    cipher_suite = Fernet(key)

    with open("testfil.py", "rb") as file_to_encrypt:                      
        content = file_to_encrypt.read()
        cipher_content = cipher_suite.encrypt(content)
        
        with open("testfil.py", "wb") as file_to_encrypt:                        #### måste skriva över, går inte att använda rb+
            file_to_encrypt.write(cipher_content)                                #### pröva sen med att anävnda rb+ är det plain text + cipher text som ligger i filen då?
            print(f"Innehåll i fil: testfil.py är krypterad - GREAT SUCCESS \n")


#### funktion för att deryptera fil
def decrypt_and_store_info():
    with open("crypto_key.key", "rb") as key_file:
        key = key_file.read()
        print("Nyckel öppnat i RAM - success! DEKRYPTERING \n")

    cipher_suite = Fernet(key)

    with open("testfil.py", "rb") as file_to_decrypt:                      
        content = file_to_decrypt.read()
        cipher_content = cipher_suite.decrypt(content)
        
        with open("testfil.py", "wb") as file_to_decrypt:                        #### Pröva copy pasta ovan men byter ut variabler och funktioner
            file_to_decrypt.write(cipher_content)
            print(f"Innehåll i fil: testfil.py är dekrypterad - GREAT SUCCESS \n")


#### Dags att bygga args :D

parser.add_argument("-c", "--create_key", action="store_true", help="Skapa krypteringsnyckel")

parser.add_argument("-e", "--encrypt_file", action="store_true", help="Filen krypteras")

parser.add_argument("-d", "--decrypt_file", action="store_true", help="Filen dekrypteras")

args = parser.parse_args()          #### tsm argparse.ArgumentParser aktiverar argsparse I guess

if args.create_key:
    print("generate_key_mode()- MODE AKTIVERAD\n")
    generate_key_mode()
    print("Ny nyckel skapad - Programmet stängs")
    
elif args.encrypt_file:
    print("encrypt_and_store_inf()- MODE AKTIVERAD\n")
    encrypt_and_store_info()
    print("Krypterat - Programmet stängs")

elif args.decrypt_file:
    print("decrypt_and_store_info()- MODE AKTIVERAD\n")
    decrypt_and_store_info()
    print("Dekrypterat - Programmet stängs")