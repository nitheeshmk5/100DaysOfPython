import pandas

#TODO 1. Create a dictionary in this format:

di = pandas.read_csv('nato.csv')
nato = {row.letter : row.code for (index,row) in di.iterrows()}
#print(nato)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter word : ").upper()
li = []
for i in word:
    li.append(nato[i])

print(li)
