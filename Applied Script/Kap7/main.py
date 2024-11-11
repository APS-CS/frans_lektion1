# ######## Importera importerar hel modul ########

# import my_module

# print(my_module.greet("Bobbo"))
# print(my_module.add(10, 25))
# print(my_module.PI)

######## Importerar paket, alltså särskilda delar av en modul ########
from my_module import greet, add
print(greet("Bobbo"))
print(add(26, 33))