for row in range(5):
    for col in range(5):
        if col == 2 or row == 2:
            print('*',end=" ")
        else:print(" ",end=" ")
    print()
    