## se cleopatra - tex för att kryptera mejl
## lösenord ska vara 15 tecken eller mer
## mfa 


# #### Lektion 7 FERNET #####


# #### Skapa nyckel ####
# from cryptography.fernet import Fernet              ####importerar Key

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
# #### cat secret.key #####


