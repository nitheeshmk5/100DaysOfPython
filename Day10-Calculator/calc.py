def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1 - n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

operators = {
    '+':add,
    '-':sub,
    '*':mul,
    '/':div
}

def calc():
    """It is used to calculate sum,difference,product,divition with two numbers"""
    num1 = float(input("Enter the number 1 : "))
    for i in operators:
        print(i)
    
    again = True
    while again:
        operator_symbol = input("Enter the operator : ")
        num2 = float(input("Enter another number : "))
        operation = operators[operator_symbol]
        res = operation(num1,num2)

        print(f"{num1} {operator_symbol} {num2} is {res}")

        if input(f"Type 'y' to continue calculating with {res}, or type 'n' to start a new calculation: ") == 'y':
            num1 = res
        else:
            again = False

calc()