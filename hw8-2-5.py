# Author: MOG 12/9/21

def sum_of_numbers(my_list):
    sum = 0
    for x in my_list:
        if x % 2 != 0:
            break
        sum += x
    return(sum)

print(sum_of_numbers([2, 4, 6, 8, 9]) == 20)
print(sum_of_numbers([13, 12, 10]) == 0)
print(sum_of_numbers([14, 16, 32]) == 62)