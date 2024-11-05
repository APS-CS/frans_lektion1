######## *args **kwargs ########

# ##Syntax##
# def function_name(*args):
#     for arg in args:
#         print(arg)

# function_name(1,1,1,1,1,1,1,1,1,1,1)


## args ##
# def print_info(name, *args):
#     print(f"Name: {name}")
#     for arg in args:
#         print(arg)

# print_info("Alice", 30, "Stockholm", "Frans, 1, 15")


## kwargs ##
# def function_name(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# function_name(name='Alice', age=30, city='Stockholm')

# def print_all(*args, **kwargs):
#     for arg in args:
#         print(arg)
#     for key, value in kwargs.items():
#         print(f"k{key}: {value}")
# print_all(1, 2, 3, name='Alice', age=30, city='Stockholm')


# def sum_numbers(*args):
#     return sum(args)
# print(sum_numbers(1, 2, 3, 4))


# def build_profile(**kwargs):
#     return kwargs
# profile = build_profile(name="Ali", age=30, job="Stockholm")
# print(profile)


# def display_info(*args, **kwargs):
#     for arg in args:
#         print(arg)
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# display_info(1,2,3,4, name="Ali", age=37, job="Göteborg")


# 'def calculate(operation, *args, **kwargs):
#     if operation == "add":
#         return sum(args)
#     elif operation == "subtract":
#         results = args[0]
#         for num in args[1:]:
#             results -= num
#         return results
#     elif operation == "multiply":
#         results = 1
#         for num in args:
#             results *= num
#         return results
#     elif operation == "divide":
#         results = args[0]
#         try: 
#             for num in args[1:]:
#                 results /= num
#         except ZeroDivisionError:
#             return "Can't divide by zero"
#         return results
#     else:
#         return "Unkown operation"

# print(calculate("add", 1, 2, 3, 4))
# print(calculate("subtract", 10, 2, 3))
# print(calculate("multiply", 2, 3, 4))
# print(calculate("divide", 10, 2, 5))
# print(calculate("divide", 1, 0 , 5))

######## lambda ########
##lambda arguments: expression

# add = lambda x, y: x + y
# print(add(2, 3))

# def add(x, y):      #gör samma som ovan
#     return x + y    #gör samma som ovan


# def apply_func(f, x, y):
#     return f(x, y)

# result = apply_func(lambda a, b: a * b, 4, 5)
# print(result)


######## map #########
##map(function, iterable)

##Syntax:
## def square(x):
##    return x * x

# numbers = [1, 2, 3, 4, 5]
# squared_numbers = list(map(square, numbers))  ##square appliceras på samtliga numbers
# print(squared_numbers)


# numbers = [1,2,3,4,5]
# squared_numbers = list(map(lambda x: x * x, numbers))   ## samma som ovan fast med lambda
# print(squared_numbers)


######## filter ########
## Syntax: 
## filter(function, iterable)


# def is_even(x):
#     return x % 2 == 0

# numbers = [1,2,3,4,5,6]
# even_numbers = list(filter(is_even, numbers))  ## filter funktionen kör is_even på alla numbers
# print(even_numbers)


# numbers = [1,2,3,4,5,6]
# even_numbers = list(filter(lambda x : x % 2 == 0, numbers))  ## samma exempel fast med lambda
# print(even_numbers)


######## scope - alltså lager i Python ########

# def check_number(num):
#     if num > 0:
#         if num % 2 == 0:
#             print(f"{num} is a positive even number")
#         else:
#             print(f"{num} is a positive odd number")
#     else:
#         if num == 0:
#             print(f"{num} is 0")
#         else:
#             print(f"{num} is a negative number")

# check_number(10)
# check_number(-5)


# def print_matrix(matrix):
#     for row in matrix:
#         for element in row:
#             print(element, end=" ")
#         print()
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print_matrix(matrix)


######## locala och globala ########

# def my_function():
#     local_var = 10
#     print(local_var)

# my_function()   ##Harmoni, local_var skrivs ut
# print(local_var)  ## det är innanför den lokala scopen alltså funktionen i det här fallet och får felkod

# global_var = 20         ##utanför lokala och är alltså global

# def my_function():
#     print(global_var)

# my_function()
# print(global_var)       ##notera att global_var åtkomlig för alla, 
#                         ##alltså ska känsliga variabler läggas i lokala så det inte är lättåtkomlig


######## scopes alltså lager ########

# def outer_function():
#     outer_var = "yttre"

#     def inner_function():
#         inner_var = "inre"
#         print(outer_var)
#         print(inner_var)

#     inner_function()
#     # print(inner_var)  ## skapar error för att det är utanför inner_function

# outer_function()


######## built in scope ########

# x = 10

# def modify_global():
#     global x  ##Global säger att funktionen är global och kan nås överallt
#     x = 20

# modify_global()
# print(x)


def outer_function():
    x = "outer"

    def inner_function():
        nonlocal x
        x = "inre"
        print(x)
    inner_function()
    print(x)
    
outer_function()