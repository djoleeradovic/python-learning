import random

lenght = int(input("Input lenght of passowrd: "))

num = "1234567890"
lower = "qwertyuiopasdfghjklzxcvbnm"
upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
symbol = "!@#$%^^&*()"
all = num + lower + upper + symbol

new_pass = random.sample(all,lenght)

print("".join(new_pass))

with open("pass.txt","a") as f:
    f.write("".join(new_pass))
    f.close()
