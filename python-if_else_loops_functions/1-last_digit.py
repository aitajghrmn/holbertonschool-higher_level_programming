#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10
if last > 5:
    print(last, "is greater than 5")
elif last == 0:
    print(last, "is 0")
elif (last < 6 && last != 0):
    print(last, "less than 6 and not 0")
