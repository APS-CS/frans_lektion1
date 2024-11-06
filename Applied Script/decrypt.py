from cryptography.fernet import Fernet

with open("secret.key", "rb") as file:
    key = file.read()                                   ## informationen sparas i key variabeln

cipher_suite = Fernet(key)

with open("encrypted.enc", "rb") as file:
    encrypted_message = file.read()

plain_text = cipher_suite.decrypt(encrypted_message)
print(f"Dekrypterad text: {plain_text.decode()}")