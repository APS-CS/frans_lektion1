from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(f"Genererad nyckel: {key.decode()}")

with open("secret.key", "wb") as file:
    file.write(key)