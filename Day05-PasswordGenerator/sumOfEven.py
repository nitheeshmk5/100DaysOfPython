n = int(input("Enter n : "))
li = [x for x in range(0,n+1,2)]

total = 0
for i in li:
    total += i

print(f"Even numbers are : {li}")
print(f"Their sum is {total}")