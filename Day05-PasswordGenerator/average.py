n = int(input("Number of students : "))
heights = input("Enter the heights of the people : ").split()

h = []
for i in heights:
    i = int(i)
    h.append(i)

total_height = sum(h)
print(f"The average height of the students is : {round(total_height/n , 2)}")