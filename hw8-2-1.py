# Author: MOG 12/9/21

def count_odds(my_list):
    odds = 0
    for x in my_list:
        if x % 2 != 0:
            odds += 1
    return odds

print(count_odds([1, 2, 3, 4, 5, 6]) == 3)
print(count_odds([1, 3, 5, 7, 9]) == 5)
print(count_odds([2, 4, 6, 8, 10]) == 0)