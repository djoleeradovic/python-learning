#Kvadriranje
"""
x = int(input("Unesite broj x: "))
n = int(input("Unesite broj n: "))

sum = 0

for i in range(1,n+1):
    sum = sum + x**i

print("Sum: ",sum)
"""

#Faktorijal

x = int(input("Unesite broj: "))
f = 1
for i in range(x,0,-1):
    f = f* i

print(f)