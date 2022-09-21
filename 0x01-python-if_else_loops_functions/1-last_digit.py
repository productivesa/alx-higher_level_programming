#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

def last_number1(n):
    temp = str(n)
    last = int(temp[len(temp)-1])
    
    if n < 0:
        return last * -1
    return last
def last_number(n):
    if n < 0:
        return -1 * ((-1 * n) % 10)
    return (n % 10)
last_num = last_number(number)

if last_num > 5:
    print(f"Last digit of {number} is {last_num} and is greater than 5")
elif last_num == 0:
    print(f"Last digit of {number} is {last_num} and is 0")
else:
    print(f"Last digit of {number} is {last_num} and is less than 6 and not 0")
