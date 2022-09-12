import json
import random

# Loads the dictionary from JSON
elements = {}
with open('elements.json', 'r') as e:
    elements = json.load(e)

# Public variables
length = len(elements["elements"])
prev = []

# Opposite (if 1, return 0 and vice versa)
def opposite(num):
    if num == 0:
        return 1
    else:
        return 0

# MAIN LOOP
if __name__ == "__main__":
    while True:
        num = random.randint(0,1)
        numop = random.randint(0,length-1)
        while numop in prev:
            numop = random.randint(0, length-1)
        prev.append(numop)

        # Easy access to element name, type, and symbol
        name = elements["elements"][numop]["name"]
        type = elements["elements"][numop]["type"]
        sym = elements["elements"][numop]["symbol"]

        # Inputs answer and checks the answer given
        if num == 0:
            ans = input('{}: '.format(elements["elements"][numop]["name"]))
            if ans == "{sym} {type}".format(sym=sym, type=type):
                print("Correct")
            else:
                print("Incorrect, the answer is {sym} {type}".format(sym=sym, type=type))
                prev.remove(numop)
        else:
            ans = input('{}: '.format(elements["elements"][numop]["symbol"]))
            if ans == "{name} {type}".format(name=name, type=type):
                print("Correct")
            else:
                print("Incorrect, the answer is {name} {type}".format(name=name, type=type))
                prev.remove(numop)
