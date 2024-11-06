######## 3. Password spraying ######## Samma som Felicia
## Ladda ner password_spraying.py från uppgiftsmaterial.
## Kontrollera om någon utav lösenorden i password_list matchar lösenordet för en
## user i user_credentials
## Skriv resultatet till fil (och i konsolen) med varje lösenord per user och om det
## lyckades eller inte.
## Exempel:
## user1: 123456 -> failed
## user1: Welcome123 -> failed

## loopa om något i lista är lika med något i filen
## loopa igenom filen
## om True eller false så skriv ut i terminal
## om true eller false skriv till ny fil


# #### som förra uppgiften skriver bara ut raderna som träffar lösenorden i listan men inte övriga #####
# with open("password_spraying.py", "r") as dictfile:
#             content = dictfile.readlines()
#             password_list = ["Password123", "123456", "Welcome123", "Guest1234", "password"]
#             for line in content:
#                     for password in password_list:
#                         if password in line:
#                             print(f"{line.strip()} -> Great hack success")



# with open("password_spraying.py", "r") as dictfile:
#     dict_inpasswordspraypy = dictfile.readlines()
#     password_list = ["Password123", "123456", "Welcome123", "Guest1234", "password"] 
#     for line in dict_inpasswordspraypy:
#         print(f"{line} - \n"


######## 3. Password spraying ########
## Ladda ner password_spraying.py från uppgiftsmaterial.
## Kontrollera om någon utav lösenorden i password_list matchar lösenordet för en
## user i user_credentials
## Skriv resultatet till fil (och i konsolen) med varje lösenord per user och om det
## lyckades eller inte.
## Exempel:
## user1: 123456 -> failed
## user1: Welcome123 -> failed

## loopa om något i lista är lika med något i filen
## loopa igenom filen
## om True eller false så skriv ut i terminal
## om true eller false skriv till ny fil


# Lista över användarnamn och deras korrekta lösenord
user_credentials = {
    "user1": "Password123",
    "admin": "Admin@2023",
    "user2": "Welcome123",
    "guest": "Guest1234"
}

password_list = ["Password123", "123456", "Welcome123", "Guest1234", "password"] 


for data in user_credentials.items():
    for password in password_list:
        if password in data:
            print(f"{data} -> Great success")
        else:
            print(f"{data} -> failed")
            break