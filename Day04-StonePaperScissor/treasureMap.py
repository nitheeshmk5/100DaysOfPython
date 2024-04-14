import random as rd

line1 = [" ", " ", " "]
line2 = [" ", " ", " "]
line3 = [" ", " ", " "]
map = [line1, line2 , line3]
print("Hide the treasure on some X position (3x3) ")
pos = input().lower()

letter = pos[0]
letters = ['a','b','c']
letter_index = letters.index(letter)

number_index = int(pos[1]) - 1

map[letter_index][number_index] = '🪙'

print("Hided the Treasure on : ")
print(f"{line1}\n{line2}\n{line3}")
