# Author: MOG 12/9/21

def letter_count(word,letter):
    count = word.count(letter)
    return count

print(letter_count("cat", "t") == 1)
print(letter_count("apple", "p") == 2)
print(letter_count("supercalifragilisticexpialidocious", "i") == 7)
