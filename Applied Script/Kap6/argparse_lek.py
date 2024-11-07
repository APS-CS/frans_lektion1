# #### adderare i terminal #####

# import argparse                         #### krav 1 - importera argparse

# parser = argparse.ArgumentParser()      #### krav 2 - använd 

#     #### positional arguments! Dessa måste skrivas i för att gå vidare
# parser.add_argument("greeting", help="Hälsning visas")
# parser.add_argument("-n", "--numbers", type=int, nargs=2, help="Skriv in nummer som ska adderas")
#     #### n = numbers kategori, type = typ av inmatning, nargs = number of arguments




# args = parser.parse_args()              #### krav 3 - nu kan man skriva ut pars

# # print(args)               #### printar alla argument som finns
# print(args.greeting)      #### skriver tillbaka användarens hälsning
# # print(args.numbers)       #### printar argument inom given kategori



# if args.numbers is not None:
#     print(f"{args.numbers[0]} + {args.numbers[1]}")
#     result = (args.numbers[0] + args.numbers[1])
#     print("Resultat: ", result)


import argparse

parser = argparse.ArgumentParser()

