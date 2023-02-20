from sys import argv
from json import dump, load

data=load(open("feeds/data.json", "r"))
arguments={}

def pop():
    data.pop()
    print(data)
    with open("feeds/data.json", "w") as feed:
        dump(data, feed)

def push():
    if argv[2] == "":
        print("Usage: dctl push <daily_income>")
        exit(1)
    data.append(int(argv[2]))
    print(data)
    
    with open("feeds/data.json", "w") as feed:
        dump(data, feed)

def _list():
    for i in range(0, len(data)):
        print("Day {}: ${}".format(i, data[i]))

arguments = {"push": push, "pop": pop, "list": _list}

try:
    if argv[1] not in arguments.keys():
        print("Usage: dctl [push, pop, list] <daily_income>")
        exit(1)

except IndexError:
     print("Usage: dctl [push, pop, list] <daily_income>")
     exit(1)
    
arguments[argv[1]]()
