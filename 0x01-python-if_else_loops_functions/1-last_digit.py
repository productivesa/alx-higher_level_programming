#!/usr/bin/python3
import random
number = random.randint(-10000,10000)

def lastnumber1(n):
    temp = str(n)
    last = int(temp)[len(temp)-1])
    if n < 0:
        return last * -1
    return last
def lastnumber(n):
    if n < 0:
        return -1 * ((-1 * n) % 10)
    return (n % 10)
finalnumber = lastnumber(number)
if finalnumber > 5:
    print(f"Last digit of {number} is {finalnumber} and is greater than 5")
elif finalnumber == 0:
    print(f"Last digit of {number} is {finalnumber} and is 0")
else:
    print(f"Last digit of {number} is {finalnumber} and is less than 6 and not 0")
