def leapYear(year):
    """This function takes an year as input and returns true if the
    given year is leap year otherwise it returns false"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
yr = int(input("Enter the year : "))
mon = int(input("Enter month (1-12) : ")) 

#checking conditions
while mon > 12 or mon < 1:
    mon = int(input("Enter month (1-12) : "))

mon = mon - 1
leap = leapYear(2000)

days = [31,28,31,30,31,30,31,31,30,31,30,31]

if leap == True:
    days[1] = 29
    print("Its a leap year")

print(f"The number of days in {mon+1}th month in the year {yr} is {days[mon]}")