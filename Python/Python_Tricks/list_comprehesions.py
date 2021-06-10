import random

numbers = [2, -1, 79, 33, -45]

doubled_1 = []
for number in numbers:
  doubled_1.append(number * 2)
print(doubled_1) 




doubled_2 = [num * 2 for num in numbers]
print(doubled_2)

#-------------------------------With conditionals----------------------------------------#
only_negative_doubled = []
 
for num in numbers:
  if num < 0: 
    only_negative_doubled.append(num * 2)
 print(only_negative_doubled)   

    
negative_doubled = [num * 2 for num in numbers if num < 0]
print(negative_doubled)

#-------------------------------Random list---------------------------------------------#

random_list = []
random_list = [random.randint(1,100) for i in range(101)]
