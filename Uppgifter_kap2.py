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

