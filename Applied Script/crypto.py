with open("secret.key", "r") as file:
    key = file.read()

print(f"Nyckel laddad: {key}")