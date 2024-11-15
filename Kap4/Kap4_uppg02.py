## Miniräknare
## Skapa en enkel miniräknare som kan utföra addition, subtraktion, multiplikation och division.
## Krav:
## ● Funktioner för varje matematiskt operation.
## ● Programmet ska ta in två tal från användaren och en operation som input.
## ● Hantera felaktig inmatning och division med 0.



#### Miniräknare 3000 ####

print("Välkommen till miniräknare 3000")


## Hantera felaktig inmatning och division med 0.
def numb_control(numb_check):
    if numb_check.isdigit():
        return True
    else:
        print(f"Bruh.. {numb_check} är inte en siffra..")
        return False

##Funktioner för varje matematiskt operation.
def add(a, b):
    return int(a) + int(b)

def subt(a, b):
    return int(a) - int(a)

def multi(a, b):
    return int(a) * int(a)

## Hantera felaktig inmatning och division med 0.
def div(a, b):
    if int(a) == int(0) or int(a) == int(0):
        print("Division med 0 funkar ej bram, programmet stängs nu")
        return False
    else:
        return int(a) / int(b)
    

while True:
    user_input1 = input("Mata in ditt första tal: ")
    input_check = numb_control(user_input1)
    if input_check:
        print(f"Ditt första tal är: {user_input1}")
        user_input2 = input("Mata in ditt andra tal: ")
        input_check2 = numb_control(user_input2)
        if input_check2:
            print(f"Ditt andra tal är: {user_input2}")
        else:
            print("Miniräknare 3000 blir ledsen och stängs pga felinmatning")
            break
    else:
        print("Miniräknare 3000 blir ledsen och stängs pga felinmatning")
        break

    operation_choice = input("Mata in din operation:\n+ = addition \n- = subtraktion \n* = multiplikation \n/ = division \n")
    if operation_choice == "+":
        add_res = add(user_input1, user_input2)
        print(f"{user_input1} + {user_input2} = {add_res}")
    
    elif operation_choice == "-":
        sub_res = subt(user_input1, user_input2)
        print(f"{user_input1} - {user_input2} = {sub_res}")

    elif operation_choice == "*":
        multi_res = multi(user_input1, user_input2)
        print(f"{user_input1} * {user_input2} = {multi_res}")
    
    elif operation_choice == "/":
        div_res = div(user_input1, user_input2)
        if div_res:
            print(f"{user_input1} / {user_input2} = {div_res}")
        else:
            break
    else:
        print(F"Fel operatoinsval: {operation_choice}. Miniräknare 3000 stängs av nu")
        break

    print("Tack och hej!")
    break