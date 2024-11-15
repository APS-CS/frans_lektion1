# ######### While loopar ##########

# x = 0
# while x < 5:
#     print(x)
#     x += 1


# x = 0
# while x < 10:
#     print(x)
#     if x == 5:
#         break
#     x += 1


# x = 0
# while x < 10:
#     x += 1
#     if x % 2 == 0:
#         continue
#     print(x)


# x = 0
# while x < 5:
#     print(x)
#     x += 1
# else:
#     print("Loopen avslutades")


# user_input = ("Ange ett kommando: ")
# print(user_input)


# while True:
#     user_input = input("Ange ett kommando: ")
#     if user_input == "exit":
#         break
#     elif user_input == "5":
#         print("Du skrev 5")
#         break
#     else:
#         print("Fel input, försök igen")


# ######### Logiska operatörer ##########

# a = True
# b = False

# print(a and b)
# print(a or b)
# print(not a, not b)


# x = 5
# print(1 < x < 10)
# print(1 < x and x < 10) ##samma som rad59 men längre


# age = int(input("Ange din ålder: "))
# if 18 <= age <= 65:
#     print("Du kan jobba")
# else:
#     print("Du kan inte jobba")


# file = open("example.txt" , "r")
# content = file.read()
# print(content)

# file.close()

# file = open("example.txt", "r")
# line = file.readline()
# while line:
#     print(line, end ="")
#     line = file.readline()
# file.close()


# file = open("example.txt", "r")
# lines = file.readlines()
# for line in lines:
#     print(line, end="")
# file.close()


# file = open("example.txt", "r")
# lines = file.read().splitlines()
# print(lines)
# file.close()


# file = open("example.txt", "w")
# file.write("Exempeltext \n")
# file.write("Nästa rad")
# file.close


# with open("example.txt", "r") as file:
#     content = file.read()
#     print(content)


# with open("output.txt", "w") as file:
#     file.write("Lite text \n")
#     file.write("Lite mer text")



# ################### Kapitel 4 ####################

# # List comprehension ##

# formel: [expression for item in interable]

# numbers = [1,2,3,4,5]
# squares = []
# for num in numbers:
#     squares.append(num ** 2)
# print(squares)


# squares = [num ** 2 for num in numbers] # samma som koden ovan fast kortare
# print(squares)


# numbers = [1,2,3,4,5,6,7,8,9]
# even_numbers = []
# for num in numbers:
#     if num % 2 == 0:
#         even_numbers.append(num)
# print(even_numbers)


# numbers = [1,2,3,4,5,6,7,8,9]
# even_numbers = [num for num in numbers if num % 2 == 0]
# print(even_numbers)


# numbers = [1,2,3,4,4,5]
# unique_squares = {num ** 2 for num in numbers}
# print (unique_squares)

# # dict comprehension - inte lika poppis ##

# fruits = ["apple", "cherry", "grape"]
# fruit_lengths = {fruit: len(fruit) for fruit in fruits}
# print (fruit_lengths)


# # Enumerate ##

# fruits = ["apple", "cherry", "grape"]
# for index, fruit in enumerate(fruits):
#     print(f"Index: {index}, Fruit: {fruit}")


# fruits = ("apple", "cherry", "grape")
# for index, fruit in enumerate(fruits):
#     print(f"Index: {index}, Fruit: {fruit}")


# matrix = [
#     [1,2,3],
#     [4,5,6,],
#     [7,8,9]
# ]

# for i, row in enumerate(matrix):
#     for j, value in enumerate(row):



# # zip ##

# name = ["Alice", "Bobbo", "Stefan"]
# age = [24,37,19]
# for namn, ålder in zip(name, age):
#     print(f"Namn: {namn}, Ålder: {ålder}")



# # input ##

# name = input("Ange ditt namn: ")
# print(name)


# # Funktioner ##

# #syntax:
# def function_name(paramterar):
#     #kod
#     return

# def greet(name):
#     return f"Hello, {name}"

# print("Test")
# print(greet("Bobbo"))


def add(a, b):
    return a + b

result = add(10, 25)
print(result)


# def greet(name="World"):
#     return f"Hello {name}"

# print(greet())
# print(greet("Bobbo"))


def add(a, b):
    return a + b

def add_square(a, b):
    sum = add(a, b)
    return sum * sum

# print(add_square(5, 2))



# # Logik och funktioner ##

# def categorize_age(age):
#     if age < 13:
#         return "Child"
#     elif age < 20:
#         return "Teenager"
#     elif age < 65:
#         return "Adult"
#     else:
#         return "Retiree"
    
# print(categorize_age(10))
# print(categorize_age(15))
# print(categorize_age(35))
# print(categorize_age(88))


# def add(a, b):
#     return a + b

# pair = (3, 5)
# result = add(*pair) #Vid tuple glöm inte stjärnan
# print(result)


# def make_power(exponent):
#     def power(x):
#         return x ** exponent
#     return power

# result = make_power(3)

# print(result(4))


