######## Installera PIP ######## - KAPITEL 5

##fungerar för att installera ett paket med funktionaliteter

## pyfiglet - skämtpaket med fonts

# import pyfiglet

# # 


# ## colorama - färgad font i terminal
# # kommando som man inte bara vet, utan får kolla upp

from colorama import init, Fore, Back, Style

# init()
# print(Fore.RED + "Den här texten är röd")
# print(Fore.GREEN + "Den här texten är grön")

# # print(Back.RED + "Röd bakgrund") #måste avsluta formateringen annars forsätter skiten att gälla
# print(Back.RED + "Röd bakgrund" + Style.RESET_ALL)

# print(Fore.RED + "Warning: Error")

import pyfiglet
ascii_art = pyfiglet.figlet_format("Krypt-verktyg 5000")
print(Back.WHITE + Fore.RED + ascii_art + Style.RESET_ALL)


######## OOP ######## - KAPITEL 6

## Input validering ##

# user_input = input("Skriv något: ")
# print(user_input)

# while True:
#     user_input = input("Ange ett nummer: ")
#     if user_input.isdigit():
#         user_number = int(user_input)
#         print(f"Du angav {user_number}")
#     else:
#         print("Ogiltig input")


## Try, except ##

# try:
#     user_input = input("Ange ett nummer: ")
#     user_number = int(user_input)
#     print(f"Du angav {user_number}")
# except ValueError:
#     print("Ogiltig input")


# valid_options = ["ja", "nej", "kanske"]
# user_input = input("Vill du sova?: ").lower()

# if user_input in valid_options:
#     print(f"Du valde {user_input}")
# else:
#     print("Jag förstår inte, försök igen")


#### OOP - Objektorienterad programmering #####

# class Car:
#     wheels = 4

#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year


# car1 = Car("Volvo", "240", 1985)
# car2 = Car("Honda", "Civic", 2017)

# print(car1.make)
# print(car1.model)
# print(car1.year)

# print(car2.make)
# print(car2.model)
# print(car2.year)

# print(car1.wheels)
# print(car2.wheels)




# class Car:
#     wheels = 4

#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
    
#     def description(self):       ##Kallas för metoder men funkar som funktioner
#         return f"{self.year}, {self.make}, {self.model}"

# car1 = Car("Volvo", "240", 1985)

# print(car1.description())


# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         pass

# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} says Woof"
    
# class Cat(Animal):
#     def speak(self):
#         return f"{self.name} says Meow"

# dog = Dog("Tarzan")
# cat = Cat("Maya")

# print(dog.speak())
# print(cat.speak())


# class Animal:                ##föräldrarklassen
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         pass

# class Dog(Animal):          
#     def __init__(self, name, breed, colour):  
#         super().__init__(name)              ##super använder en metod från föräldrarklassen
#         self.breed = breed                  ##super ersätter allt skit innanför Animal
#         self.colour = colour

#     def speak(self):
#         return f"{self.name} says Woof"


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"My name is: {self.name}, I am {self.age} old"


# person1 = Person("Bobbo", 37)
# print(person1)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __repr__ (self):            ##Gör i princip samma sak, tar bort formtateringar
#         return f"My name is: {self.name}, I am {self.age} old"


# person1 = Person("Bobbo", 37)
# print(person1)


# class StringReversed(str):
#     def reverse(self):
#         return self[::-1]

# my_string = StringReversed("Hello")
# print(my_string.reverse())

#### överkurs ####
# class DefaultDic(dict):  ##ärver från alla dict klasser
#     def __init__(self, default_value):
#        super().__init__()
#        self.default_value = default_value

#     def __getitem__(self, key):
#         return super().get(key, self.default_value)
   
# my_dict = DefaultDic(0)
# print(my_dict["missing_key"])
# my_dict["random"] = 10
# print(my_dict["random"])


######## Kryptering ########

## se Kryptografi.py