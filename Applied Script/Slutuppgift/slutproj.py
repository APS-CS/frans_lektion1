######## Projekt Frans Schartaus ########

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

#### Engna anteckningar:
## skapa skript som gör krypteringsprocedur, ha samma fil som avkrypterar
## Det ska vara argparse som tar in fil i skripten och kör bestämd kommando.

#### Om tid finns: 
## skapa (i skripten) funktion för felmeddelande, tex om filen redan är krypterad eller om filen redan av avkrypterad
## köra skripten och skapa ny nyckel

##importera argparse
import argparse
parser = argparse.ArgumentParser()   

##importera Fernet
from cryptography.fernet import Fernet

key = Fernet.generate_key()
print("Nyckel skapat - great success!")

with open("crypto_key.key", "wb") as cf:
    ck.write(key)



# ## öppnar med nyckeln
# with open("crypto_key.key", "wb") as file:
#     key = file.read()

# cipher_suite = Fernet(key)