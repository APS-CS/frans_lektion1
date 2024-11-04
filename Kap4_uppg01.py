#   # Multiplikationstabellen
#   # Skapa ett program som genererar och skriver ut en multiplikationstabell för
#   # ett tal som användaren matar in.

#    # Krav:
#    # ● En funktion för att skapa en multiplikationstabell.
#    # ● Programmet ska fråga användaren vilket tal som ska multipliceras och till vilket maxvärde.
#    # ● En funktion för att kontrollera om den inmatade strängen bara innehåller siffror. Använd exempelvis funktionen isdigit()
#    # ● Skriv ut tabellen


#### Tabell v1 #####

# def numb_control(x):
#     if x.isdigit() == True:
#         return True
#     else:
#         print("Felaktig värde - Ange en siffra mellan 0 - 9")


# def multplicate_factors(a, b):
#     if -1 < a < 10 and -1 < b < 10:
#         return a * b
#     else:
#         print("Felaktig gränsvärde - Ange en siffror mellan 0 - 9")


# while True:
#     factor1 = input("Ange en siffra mellan 0 - 9 F1: ")
#     if numb_control(factor1):
#         factor2 = input("Ange en siffra mellan 0 - 9 F2: ")
#         if numb_control(factor2):
#             product = multplicate_factors(int(factor1), int(factor2))  
#             print(product)


#### Tabell v1.6 #####
print("Välkommen till multiplikationens värld.. 0 - 9" "\n")

def numb_control(x):
    if x.isdigit() == True:
        if -1 < int(x) < 10:
            return True
        else:
            print(f"Fel gränsvärde: {x} - Siffran ska vara mellan 0 - 9")
    else:
        print(f"Felaktig värde: {x} - Ange en SIFFRA mellan 0 - 9")


def multplicate_factors(a, b):
    return a * b



while True:
    factor1 = input("Ange första faktorn, siffra mellan 0 - 9: ")
    if numb_control(factor1):
        factor2 = input("Ange andra faktorn, siffra mellan 0 - 9: ")
        if numb_control(factor2):
            product = multplicate_factors(int(factor1), int(factor2))  
            print(f"Produkten är: {product}")
            break