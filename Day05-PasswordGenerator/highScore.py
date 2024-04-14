n = int(input("Enter the total number of subjects you have : "))
i = 0
marks = []
while i < n:
    mark = float(input(f"Enter the subject{i+1} mark : "))
    marks.append(mark)
    i += 1

high_score = 0

for i in marks:
    if i > high_score:
        high_score = i

print(f"The highest score is {high_score}")