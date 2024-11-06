from cryptography.fernet import Fernet

with open("secret.key", "rb") as file:
    key = file.read()                                   ## informationen sparas i key variabeln

cipher_suite = Fernet(key)

message = "Här är mitt hemliga meddelande".encode()     ## encode = binärt format
cipher_text = cipher_suite.encrypt(message) 
print(f"Ciphertext: {cipher_text}")                     ## kör script -> nu är texten krypterat

with open("encrypted.enc", "wb") as file:               ## glöm inte att lägga til b efter w
    file.write(cipher_text)

with open("encrypted.enc", "rb") as file:
    encrypted_message = file.read()

plain_text = cipher_suite.decrypt(encrypted_message)
print(f"Dekrypterad text: {plain_text.decode()}")

#### Slutuppgift:
#### Skapa fil
#### redigera fil
#### kryptera/dekryptera fil
#### genom argparse i terminal:  py crypto.py fil.txt encrypt osv

