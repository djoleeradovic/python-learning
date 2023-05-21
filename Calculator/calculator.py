def sum(x,y):
    return x+y
def substract(x,y):
    return x-y
def prod(x,y):
    return x*y
def divide(x,y):
    return x/y

x = int(input("Type num: "))
y = int(input("Type num: "))
op = input("Type operator: ")

while op not in["+","-","*","/"]:
    op = input("Type operator: ")

if op == "+":
    print(sum(x,y))
elif op == "-":
    print(substract(x,y))
elif op == "*":
    print(prod(x,y))
elif op == "/":
    print(divide(x,y))