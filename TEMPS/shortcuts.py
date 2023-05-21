#Unpacking

tup = (1,2,3,4,5)

lst = [1,2,3,4,5]

string = "hello"

dic = {"a":1,"b":2}

cords = [4,5,4]

x,y,z = cords



#Multiple Assignment

width, height = 400,500


#Comprehensions
x = [i for i in range(100) if i %2==0]
y = [[0 for _ in range(10)] for _ in range(10)]
z = (i for i in "hello")
s = "hello"
j = {char: s.count(char) for char in set(s)}


#Object Multiplication

x = "hello" *5

#Inline/Ternary Condition

x = 1 if 2>3 else 0


#Zip
num = ["1","2","3"]
key = ["A","B","C"]
for x,y in zip(num,key):
    pass

#*args and **kwargs

def func1(arg1,arg2,arg3):
    print(arg1,arg2,arg3)
def func2(arg1=None,arg2=None,arg3=None):
    print(arg1,arg2,arg3)

args = [2,3,4]
kwargs = {"arg2":3,"arg1":2,"arg3":4}

#For Else & While Else
search = [1,2,3,4,5]
target = 3

#for element in search:
#    if element == target:
#        print("I found!")
#        break
#else:
#    print("I didnt found!")

#Sort by Key

lst = [[1,2],[3,4],[2,3]]
lst.sort(key=lambda x:x[1])

# Itertools

import itertools

num = [1,2,0,4,5]
key = ["A","B","C","D","E"]
sum_list = itertools.accumulate(num)

chain_list = itertools.chain(num,key)

compressed_list = itertools.compress(key,num)
print(list(compressed_list))