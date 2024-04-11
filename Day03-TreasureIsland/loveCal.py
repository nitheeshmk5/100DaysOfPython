print("Welcome to love calculator ❤️")
name1 = input("Enter name 1 : ").lower()
name2 = input("Enter name 2 : ").lower()

loveName = name1 + name2
print(loveName)
t = loveName.count("t")
r = loveName.count("r")
u = loveName.count("u")
e = loveName.count("e")

true = t + r  + u + e
if true > 9:        # important to add
    true = 9

l = loveName.count("l")
o = loveName.count("o")
v = loveName.count("v")
e = loveName.count("e")

love = l + o + v + e

if love > 9:
    love = 9


loveMarks = int(str(true) + str(love))

if loveMarks < 30:
    print(f"Love more , Your love score is {loveMarks} ❤️")
elif loveMarks < 60:
    print(f"Good love , Your love score is {loveMarks} ❤️")
elif loveMarks < 80:
    print(f"Strong love , Your love score is {loveMarks} ❤️")
else:
    print(f"Hi Romeo and Julet !! , Your love score is {loveMarks} ❤️")
    