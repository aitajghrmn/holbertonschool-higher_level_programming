#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number = -number
last = number % 10
print("Last digit of", number, "is", last, "and", end=" ")
if last > 5:
    print("is greater than 5")
elif last == 0:
    print("is 0")
elif (last < 6 and last != 0):
    print("is less than 6 and not 0")
