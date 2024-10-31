# x = 10
# if x > 5:
#     print("x is greater than 5")

# if x > 15:
#     print("X is greater than 15")

# if condition1:

# elif condition2:

# x = 10
# if x > 15:
#     print("X is greater than 15")

# elif x > 5:
#     print("X is greater than 5")

# x = 3
# if x > 15:
#     print("x is greater than 15")
# elif x > 5:
#     print ("x is greater than 5")
# else:
#     print("x is less than 5")

# x = 20
# if x > 10:
#     print("Above ten")
#     if x > 20:
#         print ("and also above 20!")
#     else:
#         print("but not above 20.")

# x = 7
# y = 10
# if x > 5 and y < 15:
#     print("Both conditions are True")

# def check_a():
#     print("Kontrollerar a")
#     return False

# def check_b():
#     print("Kontrollerar b")
#     return True

# if check_a() and check_b():
#     print("Båda är sann")
# else:
#     print("Minst en är falsk")

# results = värde_om_sant if villkor else värde_om falskt

# ##se nedan för komplicerad kod - det ska vara lätt!
# x = 5
# parity = "even" if x % 2 == 0 else "odd"
# print(f"number är {parity}")
# ##se ovan för komplicerad kod - det ska vara lätt!

# a = b = c = 10

# if a == b == c:
#     print("Alla är lika")

# x = -1
# if x > 0:
#     print ("x is positive")
# else:
#     pass

##Error handling - felhantering

# number = input("type a number: ")

# if number.isdigit():
#     number = int(number)
#     print(f"Your typed a number {number}")
# else:
#     print("That's not a number")


# ## FÖR Komplexa uttryck

# x = 5
# y = 10
# z = 15

# if (x < y and y < z) or x == z:
#     print("True")


## funktioner och IF -satser

# def max_value(a, b):
#     if a > b:
#         return a
#     else:
#         return b
    
# biggest = max_value(10, 20)
# print(f"The biggest value is {biggest}")
      

## Loopar
# en for loop kan gå igenom element i tex en lista eller sträng i ordning och göra en handling

# for variabel in iterable: #variabel är en tillfällig variabel, bör döpas till något identifierar

# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits: #tillfällig variabel = fruit
#     print(fruit)

##Tuple unpacking
# person = ("Alice", 30, "Stockholm")
# name, age, city = person
# print(name)
# print(age)
# print(city)

# people = [("Alice", 30 , "Stockholm"), ("Bob", 25, "Göteborg"), ("Charlie", 35, "Malmö")]
# for name, age, city in people:
#     print(f"Namn: {name}, Ålder: {age}, Stad: {city}")

# person = {"name": "Alice", "age": 30, "city": "Stockholm"}
# for key, value in person.items(): #med items så ireterar vi över båda keys och values! Använden den mer!!!
#     print(f"{key}: {value}")

