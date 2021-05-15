#This function goes through and compares 2 lists at the same time with the same length
def same_values(lst1, lst2):
  lst_same = []
  for i in range(len(lst1)):
    if lst1[i] == lst2[i]:
      lst_same.append(i)
  return lst_same

#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))
