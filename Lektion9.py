#### kör Fedora workstation - OS för att lära sig PENTEST grejer
### lär dig powershell
### UUID kolla! https://www.uuidgenerator.net/

################ shutil ################
# import shutil


# #### Exempel ####
# shutil.copy(r"c:/AppliedScript/a.key", r"c:/AppliedScript/Applied Script/Slutuppgift/a.key.bak")
# print("File has been copied")


# #### kopierar över metadata tex när filen skapades ####
# shutil.copy2("a.key", "a.key.bak")

# #### ta bort katalog
# shutil.rmtree("test")
# print("Folder deleted")

# #### kopiera katalog - tex 
# shutil.copytree("test", r"c:/AppliedScript/test2")
# print("Catalog copied")

# #### 
# shutil.chown()  #### kolla upp


# #### flytta på kataloger
# shutil.move("c:/appliedscript/test2/test", "c:/appliedscript")
# print("Mapp flyttad")


# #### skapar backup och flyttar itll vald mapp
# shutil.make_archive("backup", "zip", "C:\AppliedScript\test")  ## blir fel kolla upp!
# print("backup flyttad")


################ Pathlib ################

from pathlib import Path

# p = Path(r"C:\AppliedScript\backup")

# p = Path.home() / "c:" / "AppliedScript" / "test"

# print(p)

# p = Path.cwd() / "c:" / "appliedscript" / "test" / "test.text"
# dest = Path.cwd() / "c:" / "appliedscript" / "test2"

# print(p)


file_path = p / "test2"
if file_path.suffix == ".txt":
    print("Detta är en textfil")

