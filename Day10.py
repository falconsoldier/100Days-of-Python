def add(n, m):
    return n+m
def subtract(n, m):
    return n-m
def multiply(n, m):
    return n*m
def divide(n, m):
    try:
        ans = n/m
    except ZeroDivisionError:
        m = float(input("You cannot divide by zero, please select a different number: "))
        return divide(n,m)
    return [ans, n, m]

def calc():
    n1b = True
    n2b = True
    nob = True

    ops = {'+': add, '-': subtract, '*': multiply, '/': divide}
    print("Hello There, this is a lazy calculator app")
    print("It will take two numbers and do something with them")
    while n1b:
        try:
            num = float(input("What's the first number? "))
            n1b = False
        except ValueError:
            print("You need to enter a number")
    for x in ops:
        print(x)
    while nob:
        opsin = input("Pick an operation: ")
        if opsin not in ops:
            print("Please pick a valid operation")
        else:
            nob = False
    while n2b:
        try:
            num2 = float(input("What is the second number? "))
            n2b = False
        except ValueError:
            print("Please select a number")
    calcf = ops[opsin]
    ans = calcf(num, num2)
    print(f"{ans[1]} {opsin} {ans[2]} = {ans[0]}")







calc()