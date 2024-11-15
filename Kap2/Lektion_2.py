#strängar = immutable
#str = "Hello"
#str[0] = "Hello"
#får felmeddelande

#str = "Hello"
#new_str = "h" + str[1:]
#print(new_str)
#woho!

# str = "Python"
# new_str = str [:2] + "T" + str[3:]
# print(new_str)
# första delen av strängen utan t + T + sista delen av strängen

# age = 37
# result = "I am" + age + " years old"
# print(result)
# funkar ej

# age = 37
# result = "I am " + str(age) + " years old"
# print(result)
# funkar

# words = ["Hello", "Wolrd", "Python"]
# result = " " .join(words)
# print(result)

# str = "Hello world"
# print(str.upper())
# print(str.lower())

# str = " hello world "
# print(str.capitalize())
# print(str.title())
# print(str.strip())
# print(str.lstrip()) #tar bort mellanrummet i början
# print(str.rstrip()) #tar bort mellanrummet i slutet

# str = "apple,banana,cherry"
# fruit = str.split(",") #använd , som divider
# print(fruit)

# str = "one,two,three,four"
# str = str.split(",", 2)
# print(str)

# words = "I like apples"
# print(words.replace("apples","melons"))

# words = "Hello world"
# print(words.find("world"))

# name = "Bobbo"
# age = 37
# print(f"My name is {name} and I am {age}")

# empty_list = []

# my_list = ["apple", 42, True, 3.14]

# print(my_list[1])

# my_list = ["apple", 42, True, 3.14]

# print(my_list[-2])

# my_list = ["apple", 42, True, 3.14]

# my_list[3] = "melon"

# numbers = [1,2,3,4,5]
# # numbers[1:4] = [29,30,40]
# numbers.append(6)
# print(numbers)





# numbers = [1,2,3,4,5]

# numbers.insert(2, "hej")
# print(numbers)

# fruits = ["apple", "banana", "melon", "cherry"]
# fruits.remove("melon")
# print(fruits)

# deleted = fruits.pop(2)
# print(f"We removed {deleted} in our lists: {fruits}")

# fruits.pop()
# print(fruits)

# del fruits
# print(fruits)

# fruits.clear()
# print(fruits)

# fruits = ["apple", "banana", "melon", "cherry", "pear"]
# numbers = [2,7,4,5,1]

# numbers.sort()
# print(numbers)

# fruits = ["apple", "banana", "melon", "cherry", "pear"]

# fruits.sort(key=len)
# print(fruits)

# print(len(fruits))

# numbers = [2,7,4,5,1]

# print(sum(numbers))

##dictionaries är mutable ##

# empty_dict = {}

person = {"name": "Bobbo", "age": 37, "city": "Linköping"}

print(person["name"])
print(person.get("name"))
print(person.get("proffession", "Unknown")) ##skriver ut unknown om värdet inte finns

person["age"] = 26
print(person)

person["profession"] = "Hacker" ##Lägger till en nyckel och värde i dictionarien
print(person)

age = person.pop("age")
print(age)
print(person)

person = {"name": "Bobbo", "age": 37, "city": "Linköping"}
del person["name"]
print(person)

person["profession"] = "Hacker" 
print(person)

key, value = person.popitem()
print(key, value)
print(person)

# person = {"name": "Bobbo", "age": 37, "city": "Linköping"}

# person.clear
# print(person)

# keys = person.keys()
# print(keys)

# values = person.values()
# print(values)

# tuples = person.items()
# print(tuples)

## Tuples ##

# empty = ()

# small_tuple = (5,)

# fruits = ("apple", "melon", "cherry")

# fruits = "apple", "melon", "cherry"
# print(fruits)
# print(type(fruits))

# fruits = "apple", "melon", "cherry"
# print(fruits[0])
# print(fruits[-1])

# print(fruits[1:4])

# fruits = "apple", "melon", "cherry"
# fruits_list = list(fruits)
# fruits_list[1] = "banana"
# fruits = tuple(fruits_list)
# print(fruits)

# fruits = ("apple", "melon", "cherry")
# fruit1, fruit2, fruit3 = fruits
# print(fruit1)
# print(fruit2)
# print(fruit3)

# fruits = ("apple", "melon", "cherry", "banana", "grape")
# fruit1, fruit2, *rest = fruits
# print(fruit1)
# print(fruit2)
# print(rest)

# numbers = fruits.count("melon")
# print(numbers)

# index = fruits.index("banana")
# print(index)

## SETS ##

# empty_set = set()

# fruits = {"apple", "banana", "cherry", "apple"}
# print(fruits)
# print(fruits[0]) ## Funkar ej med sets

# fruits.add("grape")
# print(fruits)

# fruits.update(["orange", "mango"])

# fruits.discard("cherry")
# print(fruits)

# element = fruits.pop()
# print(element)
# print(fruits)

# fruits.clear()
# print(fruits)

# set1 = {1,2,3}
# set2 = {3,4,5}

# union_set = set1 | set2
# union_set = set1.union(set2) #ger samma som ovan

# print(union_set)

# intersection_set = set1 & set2
# print(intersection_set)

# difference_set  = set1 - set2
# print(difference_set)

# symmetric_set = set1 ^ set2
# print(symmetric_set)

# frozen_fruits = frozenset(["apple", "orange", "grape"])
# print(frozen_fruits)

