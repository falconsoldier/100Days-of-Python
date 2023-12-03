def add(n, m):
    return n+m
def subtract(n, m):
    return n-m
def multiply(n, m):
    return n*m
def divide(n, m):
    return n/m



def calc():
    ops = {'+': add, '-': subtract, '*': multiply, '/': divide}
    print("Hello There, this is a lazy calculator app")
    print("It will take two numbers and do something with them")
    num = float(input("What's the first number? "))

    for x in ops:
        print(x)
    opsin = input("Pick an operation: ")
    num2 = float(input("What is the second number? "))
    calcf = ops[opsin]
    ans = calcf(num, num2)
    print(f"{num} {opsin} {num2} = {ans}")







calc()