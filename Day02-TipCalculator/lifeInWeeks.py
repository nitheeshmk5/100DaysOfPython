age = int(input("Enter you age : "))

# 52 weeks a year , total 4680 weeks for 90years

livedWeeks = age * 52
balanceWeeks = 4680 - livedWeeks

print(f"You have {balanceWeeks} weeks balance to live !!")

'''
also 
balanceAge = 90 - age
balanceWeeks = balanceAge * 52
'''