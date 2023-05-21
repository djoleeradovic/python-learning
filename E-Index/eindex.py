import os 
import json
import qrcode

database = "students.json"


# Provera postojanja baze podataka i kreiranje nove ukoliko ne postoji.
if os.path.exists(database):
    with open(database, "r") as f:
        data = json.load(f)
else:
    data = {}

# Definisanje funkcije za kreiranje novog korisnika uz proveru da li korisnik vec postoji.
def new_user(id,name,last_name,jmbg,module):

    id = str(len(data) + 1)

    data[id]={
    "name":name,
    "last_name":last_name,
    "jmbg":jmbg,
    "module":module
    }

    qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_M,
    box_size = 10,
    border = 1
            )

    qr.add_data(f"Ime: {name} \nPrezime: {last_name} \nJMBG: {jmbg} \nSmer: {module}")
    qr.make(fit= True)

    graph = qr.make_image(fill_color = "black", back_color = "white")
    graph.save(f"qrcode{id}.png")


    print("Napravili ste novi index! Vas index: ",id)
# Dodavanje korisnika u bazu podataka
    with open(database, "w") as f:
        json.dump(data,f,indent=4)

# Definisanje prikaza podtaka vec postojecek korisnika.
def existing_user(id):
    if id in data:
        print("Ime: ", data[id]["name"]),
        print("Prezime: ", data[id]["last_name"]),
        date_of_bird(data[id]["jmbg"]),
        sex(data[id]["jmbg"]),
        location(data[id]["jmbg"]),
        print("Smer: ", data[id]["module"])
                 
    else:
        print("Index ne postoji!")
# Definisanje funkcije za izdvajanje datuma rodjenja iz JMBG.
def date_of_bird(jmbg):
    day = jmbg[0:2]
    month = jmbg[2:4]
    year = "2"+jmbg[4:7]
    date = day+ "." + month +"." + year
    print(f"Datum rodjenja: {date}")


# Definisanje funkcije za odredjivanje pola iz JMBG.
def sex(jmbg):
    if int(jmbg[9])<5:
        print(f"Pol: Musko")
    else:
        print(f"Pol: Zensko")

# Definisanje funckije za odredjivanje mesta rodjenja iz JBMG.
def location(jmbg):
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

# Upit za korisina da li zeli da se prijavi na vec postojeci index ili zeli novi.

while True:
    question = input(f"1)Prijavi se""\n""2)Napravi nov nalog""\n""3)Exit""\n")
    while question not in["1","2","3"]:
        question = input(f"1)Prijavi se""\n""2)Napravi nov nalog""\n""3)Exit""\n")

    if question == "1":
        id = input("Unesite broj vaseg indeksa: ")
        print("--------------------------")
        user = existing_user(id)
        print(user)
        print("--------------------------")

    elif question == "2":
        name = input("Unesite vase ime: ")
        last_name = input("Unesite vase prezime: ")
        jmbg = input("Unesite vase jmbg: ")
        module = input("Unesite vas smer: ")
        new_user(id,name,last_name,jmbg,module)
       
    elif question == "3":
        break



        
