# ######## Importera importerar hel modul ########

# import my_module

# print(my_module.greet("Bobbo"))
# print(my_module.add(10, 25))
# print(my_module.PI)



# ######## Importerar paket, alltså särskilda delar av en modul ########
# from my_module import greet, add
# print(greet("Bobbo"))
# print(add(26, 33))



# #### fler importer samtidigt
# from my_package import module1, module2

# print(module1.function1())
# print(module2.function2())



# ######## Main och name ######## 

# __main__ ####special variabel för att skripten ska veta om den ska köras eller importeras
#### gör att onödig kod inte körs

# __name__  ####special variabel för att skripten ska veta om den ska köras eller importera
# #### om script importeras blir det name


def main():
    #Mitt program
    print("Hej då")

if __name__ == "__main__":              #### om programmet blir importerad så blir det name
    main()

