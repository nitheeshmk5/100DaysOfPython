#file1 = 1,2,3,4,5
#file2 = 3,4,5,6,7

with open('file1.txt') as file1:
    f1 = file1.readlines()

with open('file2.txt') as file2:
    f2 = file2.readlines()

ans = [int(x) for x in f1 if x in f2]
print(ans)

