#### Bekräftelse att jag gjort rätt:
#### Björn ger exempel på hur man kryterar en fil:
#### Tänk binärt, I am a computer!

# with open("bild.png", "rb") as file:
#     data = file.read()

# with open("ny_bild.png", "wb") as new_file:
#     new_file.write(data)

import argparse

parser = argparse.ArgumentParser(description="beskrivning av verktyget")

parser.add_argument("name", help="Här anger du ditt namn")
parser.add_argument("age", type=int, help="Ange din ålder här")


parser.add_argument("-c", "--city", help="Ange din stad", default="Okänd stad")
# parser.add_argument("-v", "--verbose", action="store_true", help="Visar detaljerad info")   ###programmet ska skriva ut mer information om varje del
parser.add_argument("-m", "--mode", choices=["enkel", "detaljerad"], help="Välj läge")

args = parser.parse_args()

if args.mode == "detaljerad":
    print(f"Hej  {args.name}. Du är {args.age}. Du bor i {args.city}.")
else:
    print(f"Hej {args.name}")