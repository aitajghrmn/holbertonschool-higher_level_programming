#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

last = number % 10
if number < 0 and last != 0:
    last = last - 10

print("Last digit of {} is {} and".format(number, last), end=" ")

if last > 5:
    print("is greater than 5")
elif last == 0:
    print("is 0")
else:
    print("is less than 6 and not 0")

