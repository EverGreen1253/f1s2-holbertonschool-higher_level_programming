#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10

if number < 0:
    last = (10 - last) * -1

front = f"Last digit of {number} is {last}"

if last > 5:
    print(f"{front} and is greater than 5")
elif last < 6 and last != 0:
    print(f"{front} and is less than 6 and not 0")
else:
    print(f"{front} and is zero")
