import json

SAVED = "list.json"

def load_data(filepath):
    try:
        with open(filepath,"r") as f:
            data = json.load(f)
            return data
    except:
        return {}

def add_task(filepath,data):
    with open(filepath,"w") as f:
        json.dump(data,f)

data = load_data(SAVED)
while True:
    answer = input(f"Hi User, choose option:\n1)Add Task\n2)Remove Task\n3)List Tasks\n") 
    while answer not in["1","2","3","q"]:
        answer = input(f"Hi User, choose option:\n1)Add Task\n2)Remove Task\n3)List Tasks\n")
    else:
        if answer == "1":
            key = input("Enter a task: ")
            date = input("Enter a due date: ")
            data[key] = date
            add_task(SAVED,data)
            print(f"Succesfuly added task '{key}'!")

        elif answer == "2":
            key = input("Enter a key: ")
            if key in data:
                data.__delitem__(key)
                add_task(SAVED,data)
                print(f"Succesfuly deleted task '{key}'!")
            else:
                print("Key does not exist!")

        elif answer == "3":
            for i,j in data.items():
                print(f"Task: {i}")
                print(f"Due Date: {j}")
                print("-------------------------")

        elif answer == "q":
            break
