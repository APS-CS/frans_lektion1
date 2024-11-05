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
# print("Välkommen till multiplikationens värld.. 0 - 9" "\n")

# def numb_control(x):
#     if x.isdigit():
#         if -1 < int(x) < 10:
#             return True
#         else:
#             print(f"Fel gränsvärde: {x} - Siffran ska vara mellan 0 - 9")
#     else:
#         print(f"Felaktig värde: {x} - Ange en SIFFRA mellan 0 - 9")


# def multplicate_factors(a, b):
#     return a * b


# while True:
#     factor1 = input("Ange första faktorn, siffra mellan 0 - 9: ")
#     if numb_control(factor1):
#         factor2 = input("Ange andra faktorn, siffra mellan 0 - 9: ")
#         if numb_control(factor2):
#             product = multplicate_factors(int(factor1), int(factor2))  
#             print(f"Produkten är: {product}")
#             break


### missförståt uppgiften... får göra tabell 2.0 ####

### Tabell v2 #####

print("Välkommen till Multiplikationstabellen 3000 \n")

#en funktion att kotrollera om det är siffror

def numb_control(numb_check):
    if numb_check.isdigit():
        return True
    else:
        print(f"Bruh.. {numb_check} är fel.. plz välj en siffra")

#en funktion att skapa multitabell


def multitabell(a):
   for faktor2 in range(int(1),int(max_value)):
            resultat = int(faktor2)*int(faktor))
            while resultat < max_value
            print(faktor, " x ", faktor2, " = ", int(faktor2)*int(faktor))


# inputen

while True:
    faktor = input("Skriv in siffran du vill multiplicera: ")
    input_check = numb_control(faktor)
    if input_check:
        max_value = input("Skriv in produktmaxvärde: ")
        input_check2 = numb_control(max_value)
        if input_check2 and faktor <= max_value:
            multitabell(faktor)
        else:
            print("Maxvärdet måste vara högre än siffran du vill multiplicera, Gör om gör rätt!")
