# ----------------- MODULES ------------------------
# A module is a collection of Python declarations intended broadly to be used as a tool.
# Modules are also often referred to as “libraries” or “packages” — 
# (a package is really a directory that holds a collection of modules.)

#Ex: from module_name import object_name
# Or import object_name

# Using a package manager (like conda or pip3), 
#you can install any modules available on the Python Package Index

#------------------- M = RANDOM ------------------------
# random  allows you to generate numbers or select items at random.
#random.choice() which takes a list as an argument and returns a number from the list
#random.randint() which takes two numbers as arguments and generates a random number between the two numbers you passed in
#random.sample() that takes a range and a number as its arguments.It will return the specified number of random numbers from that range.
import random

random_list = []

#Turn the empty list into a list comprehension that uses 
#random.randint() to generate a random integer between 1 
#and 100 (inclusive) for each number in range(101).

random_list = [random.randint(1,100) for i in range(101)]
randomer_number = random.choice(random_list)


#------------------- M = DECIMAL ------------------------
from decimal import Decimal as ds

suma_decimal_ds = ds('2.4') + ds('3.8')
suma_decimal = 2.4 + 3.8

print(suma_decimal_ds, suma_decimal)
