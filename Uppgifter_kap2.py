# ##uppgift 1
# namn = " aNnA kaRlSsOn "

# ##V1
# format_ord = namn.strip().title()
# dela_ord = format_ord.split()

# print(dela_ord[0]+"-"+dela_ord[1])

# ##V2
# format_ord = namn.strip().title()
# dela_ord = format_ord.split()
# resultat = "-".join(dela_ord)

# print(resultat)

# ##uppgift 2
# order = ("bröd", "mjölk", "ägg", "smör", "ost", "yoghurt")

# print(order[0:3])
# print(order[-2:])
# print(order[::2])

# ##uppgift 3
# film_lista = ["Inception", "The Matrix", "Interstellar", "The Prestige"]

# if len(film_lista) > 1:
#     film_lista.append ("Memento")
#     #print(film_lista)

# for replacement in range(len(film_lista)):
#     if film_lista[replacement] == "The Matrix":
#         film_lista[replacement] = "The Lord of the Rings"
#         #print(film_lista)

# if "The Prestige" in film_lista:
#     film_lista.remove("The Prestige")
#     #print(film_lista)

# if "The Dark Knight" != film_lista[2]:
#     film_lista.insert(2, "The Dark Knight")
#     print(film_lista)


##uppgift 4##
data = {
"studenter": [
("Alice", {"ålder": 25, "ämnen": ("Matematik", "Fysik"), "aktiv": True}),
("Bob", {"ålder": 22, "ämnen": ("Biologi",), "aktiv": False}),
("Charlie", {"ålder": 23, "ämnen": ("Matematik", "Biologi"), "aktiv": True}),
("Diana", {"ålder": 24, "ämnen": ("Fysik",), "aktiv": False}),
("Eve", {"ålder": 21, "ämnen": ("Matematik", "Fysik", "Biologi"), "aktiv":
True}),
],
"kurser": {
"Matematik": {"studenter": {"Alice", "Charlie", "Eve"}},
"Fysik": {"studenter": {"Alice", "Diana", "Eve"}},
"Biologi": {"studenter": {"Bob", "Charlie", "Eve"}},
}
}

#Extrahera en tuple med namn på alla aktiva studenter (de vars "aktiv"-status är True).

#aktiv == True
#print(type(data)) #dict

# print(data.items()) #allt kommer fram!
# print(data.get("studenter"))

