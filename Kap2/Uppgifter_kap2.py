# #######################################uppgift 1#######################################
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

# #######################################uppgift 2#######################################

# order = ("bröd", "mjölk", "ägg", "smör", "ost", "yoghurt")

# print(order[0:3])
# print(order[-2:])
# print(order[::2])

# #######################################uppgift 3#######################################
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




# ##########################uppgift 4##########################

# for key, value in data.items():
#     print("key:")
#     print(key)
#     print("value:")
#     print(value)
#     print(" ")

# data = {
# "studenter": [
# ("Alice", {"ålder": 25, "ämnen": ("Matematik", "Fysik"), "aktiv": True}),
# ("Bob", {"ålder": 22, "ämnen": ("Biologi",), "aktiv": False}),
# ("Charlie", {"ålder": 23, "ämnen": ("Matematik", "Biologi"), "aktiv": True}),
# ("Diana", {"ålder": 24, "ämnen": ("Fysik",), "aktiv": False}),
# ("Eve", {"ålder": 21, "ämnen": ("Matematik", "Fysik", "Biologi"), "aktiv":
# True}),
# ],
# "kurser": {
# "Matematik": {"studenter": {"Alice", "Charlie", "Eve"}},
# "Fysik": {"studenter": {"Alice", "Diana", "Eve"}},
# "Biologi": {"studenter": {"Bob", "Charlie", "Eve"}},
# }
# }
#¤

##Extrahera en tuple med namn på alla aktiva studenter (de vars "aktiv"-status är True).





##kom på att man kan göra om dikrekt efter "=" tecknet didrekt till tuple


# namnlista = tuple()'

# tuple_namnlista = tuple(aktiv_student[0] for aktiv_student in data["studenter"] if aktiv_student[1]["aktiv"])
# print(tuple_namnlista)


## *nytt_värde* for *variabler* in *iterable* if *villkor*
## aktiva_studenter = tuple(namn for namn, dict etc
### nytt blad##


# ##chatgpt
# tuple_namnlista = tuple(
#     namn 
#     for namn, studentinfo in data["studenter"] 
#     if studentinfo["aktiv"]
#     )

# # print(tuple_namnlista)

# ##Skapa ett set med alla unika ämnen som de aktiva studenterna studerar.
# ##använde chatgpts logik och funkar bra
# topic_set = set(
#     unika_ämnen
#     for namn, studentinfo in data["studenter"]
#     if namn in tuple_namnlista
#     for unika_ämnen in studentinfo["ämnen"]
#     )

# print(topic_set)

##Skapa en ordbok där nycklarna är kursnamnen och värdena är antalet aktiva studenter som är inskrivna i respektive kurs.

# tuple_dict = tuple(
#     studenterikurs
#     for studenterna, namnen in data["kurser"].items()
#     for studenterikurs in namnen["studenter"]
# )
# print(tuple_dict) ##skriver ut alla namn från alla kurser

# print(data.get("kurser"),[1])

# tuple_antalkursdelt = data["kurser"].get("Matematik")

# kurser = data["kurser"].keys()
# antal_studenter = len(data["kurser"].values())

# tuple_antalkursdelt = tuple( 
#     antal_studenter 
#     for kurs1, kurs2, kurs3 in data["kurser"]
#     for antal_studenter in kurs1.len(["studenter"]))
# print(tuple_antalkursdelt)

# print(f" Här kommer kurserna och antal studenter {kurser}: {antal_studenter} ")


##försök 1
# mattestudenterlista = studenterokurser["Matematik"]
# matttestudenter = mattestudenterlista.get("studenter")

# values = studenterokurser.values()
# for studenter_lista in values:
#     for stud in matttestudenter:
#         print(stud)

##försök 2
# studenterokurser = data["kurser"]



# keys = studenterokurser.keys()
# values = studenterokurser.values()

# for ämne in keys:
#     print(ämne)
    
# for studentlista in values:
#     for enskilda_studenter in studentlista.values():
#         print(len(enskilda_studenter))

# dict = {}


# dict_kursostud = {}
# dict_kursostud[ämne] = len(enskilda_studenter)

# print(dict_kursostud)

# dict_studokurs = {
#     ämne: len(enskilda_studenter),
# }
# for dict_studokurs1 in ämne, len(enskilda_studenter):
#     print(dict_studokurs1)

# for x, y in dict_kursostud.items():
#   print(f"Kurs: {x} , Kursdeltagare: {y}")

##paus på den här uppgf...
##lördagmorgon

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
    "Matematik": {
        "studenter": {
            "Alice", "Charlie", "Eve"
            }
            },
    "Fysik": {
        "studenter": {
             "Alice", "Diana", "Eve"
             }
             },
    "Biologi": {
        "studenter": {
            "Bob", "Charlie", "Eve"
            }
            },
}
}
# #första listan - fick jobbet gjort..
namnlista = []

for aktiv_student in data["studenter"]:
    if aktiv_student[1]["aktiv"] == True:
        namnlista.append((aktiv_student[0]))

tuple_namnlista = tuple(namnlista)    
print(f"Aktiva studenter: {tuple_namnlista}")


# tuple_namnlista = tuple(
#     namn 
#     for namn, studentinfo in data["studenter"] 
#    if studentinfo["aktiv"])
# print(tuple_namnlista)


topic_set = set(
    unika_ämnen
    for namn, studentinfo in data["studenter"]
    if namn in tuple_namnlista
    for unika_ämnen in studentinfo["ämnen"]
    )
print(f"Ämnen: {topic_set}")


dict_courseandstudents = {}

dict_courseandstudents["Matematik"] = ((len(data["kurser"]["Matematik"]["studenter"])))
dict_courseandstudents["Fysik"] = ((len(data["kurser"]["Fysik"]["studenter"])))
dict_courseandstudents["Biologi"] = ((len(data["kurser"]["Biologi"]["studenter"])))
 
for key, value in dict_courseandstudents.items():
    print(f"Kurs: {key}, antal studenter: {value}")