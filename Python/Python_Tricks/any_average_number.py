#This function can get any average value from an indefinite list of number
def any_average_number(lst):
    total_input = len(lst)
    sum_input = 0
    for sum in lst:
        sum_input += sum
    percentage = sum_input/total_input
    return percentage
print(any_average_number([5,7,6,8]))
