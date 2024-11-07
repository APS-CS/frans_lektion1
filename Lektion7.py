## se cleopatra - tex för att kryptera mejl
## lösenord ska vara 15 tecken eller mer
## mfa 


# #### Lektion 7 FERNET #####


# #### Skapa nyckel ####
from cryptography.fernet import Fernet              ####importerar Key

# key = Fernet.generate_key()                         #### definerar variabel som anropar funktion i standard biblioteket som generar nyckel

# print(f"Generated key: {key.decode()}")             ####Visar bara vad som händer och anropar nyckeln som decodad med .decode


# with open("secret.key", "wb") as key_file:          #### w = öppna/skapa fil i bytes, b = skapar binär fil i byte objekt
#     key_file.write(key)

# print(f"Key is saved to file 'Secret.key'")


# #### Läsa nyckel ####
# with open("secret.key", "rb") as key_file:
#     key = key_file.read()

# print(f"Key is loaded: {key.decode()}")

# #### Går även att skriva in i terminalen och få fram det där #####
# #### type secret.key #####


######## Kryptera ett meddelande ########
print("Här krypterar vi:")

#### laddar nyckeln
with open("secret.key", "rb") as key_file:
    key = key_file.read()
print(f"Key is loaded: {key.decode()}")                     #### Bra med att lägga in printar för att veta vart/om koden går fel

#### skapar instans av nyckeln
cipher_suite = Fernet(key)
print("Fernet object is created and ready for encryption")

#### krypteringen av texten 

message = "This is a string with a secret message".encode() #### Funktionen encrypt finns i FERNET därav "odefinerad" funktion - Se nedre rad
cipher_text = cipher_suite.encrypt(message)                 #### får in texten och gör om till bytes 
print(f"Encrypted message: {cipher_text}")                  #### kontroll

#### spara texten till en fil

with open("encrypted_message.enc", "wb") as enc_file:
    enc_file.write(cipher_text)

print("Encrypted message is saved to file 'encrypted_message.enc'")
print("\n")

######## decrpytera
print("Här dekrypterar vi:")

with open("encrypted_message.enc", "rb") as enc_file:
    encrypted_message = enc_file.read()

print(f"Encrypted message is loaded: {encrypted_message}")

plain_text = cipher_suite.decrypt(encrypted_message)
print(f"Decrypted message: {plain_text.decode()}")


#### Uppgiften: det vi ska göra är att kryptera en fil ist för en message/sträng