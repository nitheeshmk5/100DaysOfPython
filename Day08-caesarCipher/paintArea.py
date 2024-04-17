import math

height = float(input("Enter height : "))
width = float(input("Enter width : "))
coverage = float(input("Enter total coverage : "))

def area(h,w,c):
    a = (h * w)/c
    print(f"You need {math.ceil(a)} cans")


area(height,width,coverage)