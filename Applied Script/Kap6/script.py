import argparse
######### argparse ########
##argparse låter en ta argument i kommandotolken

##exempel som gavs:
##python crypto.py fil.text -mode encrypt

# parser = argparse.ArgumentParser(description="Mitt krypterngsverktyg")

# parser.add_argument("name", help="Ange ditt namn") ##helpavsnitt när använder vill veta vad som ska göras

# args = parser.parse_args()

# print(f"Hej {args.name}")

## #PS C:\AppliedScript\Applied Script\Kap6> python script.py
## usage: script.py [-h] name

## script.py: error: the following arguments are required: name


## PS C:\AppliedScript\Applied Script\Kap6> python script.py --help
## usage: script.py [-h] name

## Mitt krypterngsverktyg

## positional arguments:
## usage: script.py [-h] name

## Mitt krypterngsverktyg

## usage: script.py [-h] name

## usage: script.py [-h] name

## usage: script.py [-h] name
## usage: script.py [-h] name
## usage: script.py [-h] name

## Mitt krypterngsverktyg

## positional arguments:
##   name        Ange ditt name

## options:
##   -h, --help  show this help message and exit

## PS C:\AppliedScript\Applied Script\Kap6> python script.py Amper 
## Hej Amper 

# parser = argparse.ArgumentParser(description="Mitt krypterngsverktyg")

# parser.add_argument("name", help="Ange ditt namn") ##helpavsnitt när använder vill veta vad som ska göras
# parser.add_argument("age", type=int, help="Ange din ålder")

# parser.add_argument("-v", "--verbose", action="store_true", help="Visa mer information") ## - = flagga!, inte obligatoriska argument

# args = parser.parse_args()

# if args.verbose:
#     print(f"Hej {args.name}, din ålder: {args.age}")
# else:
#     print(f"Hej {args.name}")

# PS C:\AppliedScript\Applied Script\Kap6> python script.py       
# usage: script.py [-h] [-v] name age
# script.py: error: the following arguments are required: name, age

# PS C:\AppliedScript\Applied Script\Kap6> python script.py Amper 
# usage: script.py [-h] [-v] name age
# script.py: error: the following arguments are required: age

# PS C:\AppliedScript\Applied Script\Kap6> python script.py Amper 18
# Hej Amper

# PS C:\AppliedScript\Applied Script\Kap6> python script.py Amper -v
# usage: script.py [-h] [-v] name age
# script.py: error: the following arguments are required: age

# PS C:\AppliedScript\Applied Script\Kap6> python script.py Amper 18 -v
# Hej Amper, din ålder: 18

parser = argparse.ArgumentParser(description="Mitt krypterngsverktyg")

parser.add_argument("name", help="Ange ditt namn") ##helpavsnitt när använder vill veta vad som ska göras
parser.add_argument("age", type=int, help="Ange din ålder")

parser.add_argument("-v", "--verbose", action="store_true", help="Visa mer information") ## - = flagga!, inte obligatoriska argument

args = parser.parse_args()

if args.verbose:
    print(f"Hej {args.name}, din ålder: {args.age}")
else:
    print(f"Hej {args.name}")

input