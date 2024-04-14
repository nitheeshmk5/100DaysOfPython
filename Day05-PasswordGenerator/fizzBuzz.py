print("Welcome to FIZZBUZZ !!")

n = int(input("Enter n : "))
li = []

for i in range(1,n+1):
    if i%3 == 0 and i%5 == 0:
        i = "FIZZBUZZ"
        li.append(i)
    elif i%5 == 0:
        i = "BUZZ"
        li.append(i)
    elif i&3 ==0 :
        i = "FUZZ"
        li.append(i)
    else:
        li.append(i)
        
print(li)

