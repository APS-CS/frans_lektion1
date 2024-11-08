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
## skapa funktion för att kryptera
## skapa funktion för att dekryptera


#### FRÅGOR: Hur göra om flera filer? Krypera med bara en nyckel? Skapa en ny nyckel varje gång? Kan det bli dubbelkryp?
#### FRÅGOR: vad händer med plaintext och enc fil? Ta vi bort? ersätter hela filen? är den redan krypterad?

#### Argparse
## Det ska vara argparse som tar in fil i skripten krypterar/dekrypterar

## 1. Krypera
## 1a. Ange fil -> Bekräftelse
## 1a. Ange fil -> Fil redan kryperad?

## 2. Dekryptera
## 2a. Ange fil -> Bekräftelse
## 2a. Ange fil -> Fil redan kryperad? 

## 3. Skapa nyckel -> Bekräftelse


#### FRÅGOR: Hur ange filnamn som ska de/krypteras? 


#### Om tid finns: 
## skapa (i skripten) funktion för felmeddelande, tex om filen redan är krypterad eller om filen redan av avkrypterad
## köra skripten och skapa ny nyckel


################ Ain't nuttin but to do it!! ################
## impertera os åtkomst
import os

##importera argparse
import argparse
parser = argparse.ArgumentParser()   

##importera Fernet
from cryptography.fernet import Fernet

#### funktion för at skapa nyckel
def generate_key_mode(newkey):                                          ####funktionen skapar ny nykel.. hur använda en nyckel som är redan skapad?
    newkey = Fernet.generate_key()
    print("Nyckel skapat i RAM - great success! \n")                    ####Bekräftelse

    with open("crypto_key.key", "wb") as key_file:                      ####Förvald crypto_key.key
        key_file.write(newkey)
        print("Nyckel skapat i fil - great success! \n")                ####Bekräftelse


#### funktion för att kryptera fil
def encrypt_and_store_file(filename):
    with open("crypto_key.key", "rb") as key_file:
        key = key_file.read()                                               #### öppnar förvald crypto_key.key                            
        print("Nyckel öppnat i RAM - great success! \n")                    #### Bekräftelse

    cipher_suite = Fernet(key)

#### HÄR MÅSTE VI VÄLJA ANGIVEN FIL OCH LÄSA AV INNEHÅLLET
#### Det är innehållet alltså bytes som krypteras inte skalet!

filename = os.path.exists("testfil")

cipher_suite = Fernet(key)

with open("filename", "rb") as file_to_encrypt:
    content = file_to_encrypt.read()
    cipher_content = cipher_suite.encrypt(content)
    cipher_content.write("filename", "wb")                     
    print(f"Innehåll i fil: {filename} är krypterad")