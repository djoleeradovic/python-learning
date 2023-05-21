import sqlite3

database = "cars.db"

# Definisanje Klase
class Cars():
    def __init__(self,name,color,type,year):  #Konstruktor
        self.name = name #atribut
        self.color = color #atribut
        self.type = type #atribut
        self.year = year #atribut

# Povezivanje na bazu podataka
conn = sqlite3.connect(database) #konektor

c = conn.cursor() # kursor koristimo za sve promene koje izvravamo u bazi podataka

# Kreiranje tabele u bazi podataka
conn.execute("""CREATE TABLE cars(
        NAME TEXT,
        COLOR TEXT,
        TYPE TEXT,
        YEAR INT);""") 


c.close()
# Omogucanje korisniku unos podataka
name = input("Unesite naziv automobila: ")
color = input("Unesite boju automobila: ")
type = input("Unesite tip automobila: ")
year = int(input("Unesite godiste automobila: "))

# Stvaranje objekta pomocu unetih podataka
new_car = Cars(name,color,type,year)

# Upisivanje podataka u bazu podataka
conn.execute(f"""
    INSERT INTO cars(name,color,type,year) \n
    VALUES ('{new_car.name}','{new_car.color}','{new_car.type}',{new_car.year})
""")

conn.commit()
conn.close()
print("Uspesno je unet automobil")
