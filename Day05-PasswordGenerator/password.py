import random as rd

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to password generator !")
total_characters = int(input("Enter the total character : "))
with_numbers = input("incluing numbers [Y/N] : ").upper()
with_symbols = input("including symbols [Y/N] : ").upper()

password_list = []

if with_numbers == "Y":
    letters += numbers
if with_symbols == "Y":
    letters += symbols

for i in range(0,total_characters ):
    password_list.append(rd.choice(letters))

rd.shuffle(password_list)

password = "".join(password_list)

print(password)



