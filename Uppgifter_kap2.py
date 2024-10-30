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

    if "The Matrix" in film_lista:
        # film_lista = film_lista.replace("The Matrix", "Lord of the Rings")
        film_lista(["The Matrix"]) = "Lord of the Rings"
        print(film_lista)
