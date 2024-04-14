import random

n = int(input("Enter the total number of people : "))

randNum = random.randint(0,n-1)

li = []

for i in range(1,n+1):
    name = input(f"Enter the {i} name : ")
    li.append(name)

print(f"Today {li[randNum]} pays the bill !!")

