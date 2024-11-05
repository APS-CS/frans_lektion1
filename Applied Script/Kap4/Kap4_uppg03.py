#### Inköpslista ####
## Skapa ett program som hanterar en inköpslista. 
## Programmet ska kunna:
## Lägga till, ta bort och visa alla varor till inköpslistan.
## Spara inköpslistan till en textfil (användaren får välja filnamn).

## Krav:
## Programmet ska ha en meny
## användaren kan välja att visa listan
## lägga till varor
## ta bort varor
## spara listan  
## avsluta.
##● Använd funktioner för att hantera menyval.


### Måste öppna inköpslista gång på gång
print("Välkommen till shoppinglista 3000 \n")
#interaktion med OS
import os

#meny funktioner

#Spara inköpslista
def create_file(filename):
    if not os.path.exists(filename):
        with open(filename + ".txt", "w") as listfile:
            print(f"Inköpslista {filename} skapades")
    else:
        print(f"Inköpslista {filename} finns redan")


#Visa inköpslista
def read_file(filename):
    if os.path.exists(filename):
        with open(filename, "r") as listfile:
            content = listfile.readlines()
            for line in content:
                print(line.strip())
    else:
        print(f"Finns ingen inköpslista med namn: {filename} ")


#Lägg till i inköpslista
def append_item(filename, text):
    with open(filename, "a") as listfile:
        listfile.write(" " + text + " " + "\n")
    print("Vara tillagd i inköpslista")


#ta bort från inköpslista
def remove_item():
    content = read_file()
    remove = " " + input("Välja vara som ska tas bort: ") + " "
    if remove in content:
        edited_content = content.replace("\n" + remove, "")
        save_content = (edited_content, "w")




#Avsluta


#Meny
while True:
    print("Huvudmeny")
    print("Val 1 -> Skapa inköpslista")
    print("Val 2 -> Visa/öppna inköpslista")
    print("Val 3 -> Lägg till vara i inköpslista")
    print("Val 4 -> Ta bort vara i inköpslista")
    print("Val 5 -> Avsluta")

    choice = input("Navigera genom att välja 1-5: ")

    if choice == "1":
        filename = input("Skapa inköpslista: ")
        create_file(filename)

    elif choice == "2":
        user_filename = input("Namn på inköpslista: ")
        osfilename = user_filename + ".txt"
        read_file(osfilename)

    elif choice == "3":
        user_filename = input("Välj inköpslista: ")
        osfilename = user_filename + ".txt"
        if os.path.exists(osfilename):
            text = input("Skriv in vara att lägga: ")
            append_item(osfilename, text)
        else:
            print(f"Lista med namn {user_filename} finns ej")
            False

    elif choice == "4":
        remove_item()

    elif choice == "5":
        print("Avslutar program")
        break