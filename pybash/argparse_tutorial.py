import argparse

"""
1. The --help or -h option is the only one we get for free.
2. If we don't set default for value, they get None by default


python argparse_tutorial.py 10 -v 100 -m 2 -ccc -n
"""

parser = argparse.ArgumentParser(description="Tutorial for argparse")

# positional arguments:
parser.add_argument("echo", help="Echo the string you use here.") # positional argument, treated as str by default
parser.add_argument("square", help="type a number here to get its square.", type=int)

# optional arguments:
parser.add_argument("-v", "--verbosity", help="increase output verbosity", action="store_true") # action=store_true make this a flag, rather than requiring a value
parser.add_argument("-m", "--message_type", help="the type of messages", type=int, choices=[0, 1, 2], default=0) # restricting accepted inputs
parser.add_argument("-c", "--count", help="Count type - similar to how CPython handles its own verbose. E.g.: -ccc", action="count", default=0)  

group = parser.add_mutually_exclusive_group() # use when two arguments are mutually exclusive
group.add_argument("-p", "--positive", action="store_true", help="return positive square")
group.add_argument("-n", "--negative", action="store_true", help="add negative sign to share")


args = parser.parse_args()
square = args.square**2
if args.negative:
    square = -square
elif args.positive:
    pass
else:
    print("neither -n nor -p was given. Default to positive.")
    
    
if args.verbosity:
    print(f"verbosity: square of input {args.square} is {square}\n")

msgType = args.message_type

if msgType == 1:
    print(f"Selecting msgType {msgType}\n")
elif msgType == 2:
    print(f"Selecting even more verbose msgType {msgType}\n")


args = parser.parse_args()

print(args.echo) # args.echo is part of the magic done for free
print(f"-c or --count value: {args.count}\n")

