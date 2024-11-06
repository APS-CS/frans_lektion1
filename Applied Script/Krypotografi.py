from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(f"Genererad nyckel: {key.decode()}")

