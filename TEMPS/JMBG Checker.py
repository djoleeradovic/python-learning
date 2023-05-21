def jmbg_passed():
    print("JMBG Passed")
def jmbg_error():
    print("Error 404")

def check():
    while True:
        jmbg = (input("Unesite JMBG: "))
        if len(jmbg) != 13:
            jmbg_error()
            continue
        elif not jmbg.isdecimal():
            jmbg_error()
            continue
        else:
            return jmbg

def test():
    sum = 7 * int(jmbg[0]) + 6* int(jmbg[1]) + 5 * int(jmbg[2]) + 4*int(jmbg[3]) + 3 * int(jmbg[4]) + 2 * int(jmbg[5]) + 7 * int(jmbg[6]) + 6 * int(jmbg[7]) + 5 * int(jmbg[8]) + 4 * int(jmbg[9]) + 3 * int(jmbg[10]) + 2 * int(jmbg[11])
    rest = sum%11
    return rest

def date_of_bird():
    if int(jmbg[9]) == 9:
        print(int(jmbg[0]),int(jmbg[1]),".",int(jmbg[2]),int(jmbg[3]),".","1",int(jmbg[4]),int(jmbg[5]),int(jmbg[6]))
    else:
        print(int(jmbg[0]),int(jmbg[1]),".",int(jmbg[2]),int(jmbg[3]),".","2",int(jmbg[4]),int(jmbg[5]),int(jmbg[6]))


def location():
    if int(jmbg[7]) == 0:
        print("Stranac")
    elif int(jmbg[7]) == 1:
        print("Bosna i Hercegovina")
    elif int(jmbg[7]) == 2:
        print("Crna Gora")
    elif int(jmbg[7]) == 3:
        print("Hrvatska")
    elif int(jmbg[7]) == 4:
        print("Severna Makedonija")
    elif int(jmbg[7]) == 5:
        print("Slovenija")
    elif int(jmbg[7]) == 6:
        print("Privremeni boravak")
    elif int(jmbg[7]) == 7:
        print("Centralna Srbija")
    elif int(jmbg[7]) == 8:
        print("AP Vojvodina")
    else:
        print("AP Kosovo")

def sex():
    if int(jmbg[9])<5:
        print("Male")
    else:
        print("Woman")


#-------------------------------------------#



jmbg = check()

rest = test()

if rest == 0:
   jmbg_passed() if int(jmbg[12]) ==0 else jmbg_error()

if rest == 1:
    jmbg_error()

if rest>1:
    jmbg_passed() if int(jmbg[12]) == 11- rest else jmbg_error()
      
date_of_bird()  
location()
sex()
        



