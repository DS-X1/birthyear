import argparse

parser = argparse.ArgumentParser(
    prog = "birthyear",
    usage = "use: [options] year age",
    description = "Calculates the years someone with a specific age was born.",
    epilog = ("""This is my first command-line python program!"""))

parser.add_argument('year', type=int, help="current year / year of death")
parser.add_argument('age', type=int, help="current age / age at death")
parser.add_argument('-c','--custom_name',help="person's name")
parser.add_argument('-x',help="display one year (earliest)",action="store_true",
                        default=False)

args = parser.parse_args()

year = args.year
age = args.age
birth = year - age

# Check if you only want one year
if args.x:
    birth_string = f"in {birth}."
else:
    birth_string = f"between {birth} and {birth+1}."

# Check if custom name was given
if args.custom_name:
    print(f"{args.custom_name} was born {birth_string}")
else:
    print(f"{year}\nYou were born {birth_string}")