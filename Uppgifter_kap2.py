#uppgift 1
namn = " aNnA kaRlSsOn "

#V1
format_ord = namn.strip().title()
dela_ord = format_ord.split()

print(dela_ord[0]+"-"+dela_ord[1])

#V2
format_ord = namn.strip().title()
dela_ord = format_ord.split()
resultat = "-".join(dela_ord)

print(resultat)

#uppgift 2
order = ("bröd", "mjölk", "ägg", "smör", "ost", "yoghurt")

print(order[0:3])
print(order[-2:])
print(order[::2])

#uppgift 3
film_lista = ["Inception", "The Matrix", "Interstellar", "The Prestige"]

if len(film_lista) > 1:
    film_lista.append ("Memento")
    print(film_lista)

    for replacement in range(len(film_lista)):
        if film_lista[replacement] == "The Matrix":
            film_lista[replacement] = "The Lord of the Rings"
            print(film_lista)

if "The Prestige" in film_lista:
    film_lista.remove("The Prestige")
    print(film_lista)

if "The Dark Knight" != film_lista[2]:
    film_lista.insert(2, "The Dark Knight")
    print(film_lista)
