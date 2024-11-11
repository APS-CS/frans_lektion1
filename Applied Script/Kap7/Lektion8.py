#### Bekräftelse att jag gjort rätt:
#### Björn ger exempel på hur man kryterar en fil:
#### Tänk binärt, I am a computer!

# with open("bild.png", "rb") as file:
#     data = file.read()

# with open("ny_bild.png", "wb") as new_file:
#     new_file.write(data)

# import argparse

# parser = argparse.ArgumentParser(description="beskrivning av verktyget")

# parser.add_argument("name", help="Här anger du ditt namn")
# parser.add_argument("age", type=int, help="Ange din ålder här")


# parser.add_argument("-c", "--city", help="Ange din stad", default="Okänd stad")
# # parser.add_argument("-v", "--verbose", action="store_true", help="Visar detaljerad info")   ###programmet ska skriva ut mer information om varje del
# parser.add_argument("-m", "--mode", choices=["enkel", "detaljerad"], help="Välj läge", type=str.lower)

# args = parser.parse_args()

# if args.mode == "detaljerad":
#     print(f"Hej  {args.name}. Du är {args.age}. Du bor i {args.city}.")
# else:
#     print(f"Hej {args.name}")


######### Kapitel 7 ##########

######## Moduler och paket ########
#### se: math_script och my_package

# #### Felhantering ####
# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("Fel: Division med noll är inte tillåtet")
# else:
#     print(f"Resultat: {result}")
# finally:
#     print(f"Slut på try excep")


# try:
#     with open("exampel.txt", "r") as file:
#         content = file.read()
# except FileNotFoundError:
#     print("Fel: Filen finns inte!")
# except Exception as e:                  #### den här plockar alla exceptions!
#     print(f"Fel: {e}")
# else:
#     kryptera(content)



#### OS-modulen ####

import os

# os.chdir("c:\\")

# cwd = os.getcwd()                       #### current working directory
# print(cwd)

# os.mkdir("test_folder")                   #### skapar katalog
# os.rmdir("test_folder")                   #### tar bort katalog


#### felhantering os

# if os.path.exists("example.txt"):
#     print("Filen existerar")
#     os.remove("example.txt")                #### tar bort filer
# else:
#     print("Filen existerar inte")


# file_info = os.stat("bild.png")                   #### kan få fett mkt info om filen
# print(f"Filstorket: {file_info.st_size}")         #### exempel

# os.system("dir")                                  #### var försiktig!



# #### hitta bland olika OS

# filepath = os.path.join("math_script","main.py")                     ####funktionalietet mellan olika os-system

# print(filepath)

# with open(filepath, "r") as file:                                   ##### nu kan den hitta bland olika os-system
    # kod



#### 

# import platform

# if os.name == "nt":
#     print("Windows!")
#     os.system("dir")
# else:
#     print("Unix!")
#     os.system("ls")

# print(f"Plattform: {platform.system()}")




from pathlib import Path