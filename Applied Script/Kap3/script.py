## Filhanteringsverktyg ##
import os

def read_file(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            content = file.readlines()
            for line in content:
                print(line.strip())
    else:
        print("The file does not exist")

def create_file(filename):
    if not os.path.exists(filename):
        with open(filename, "w") as file:
            print(f"File was created: {filename}")
    else:
        print(f"File already exists: {filename}")

def append_file(filename, text):
    with open(filename, "a") as file:
        file.write(text + "\n")
    print("Text was added")

    
# Main program

while True:
    print("Menu: ")
    print("1. Read a file")
    print("2. Create a file")
    print("3. Append to file")
    print("4. Erase file")
    print("5. Exit")

    choice = input("Chose an option (1-5): ")

    if choice == "1":
        filename = input("Select file: ")
        read_file(filename)

    elif choice == "2":
        filename = input("Enter filename: ")
        create_file(filename)

    elif choice == "3":
        filename  = input("Enter filname: ")
        text = input("Text to add to file: ")
        append_file(filename, text)

    elif choice == "5":
        print("Exit programme")
        break

