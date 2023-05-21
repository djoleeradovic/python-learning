import sqlite3

database = "flowers.db"

class Flowers():
    def __init__(self,name,color):
        self.name = name
        self.color = color

conn = sqlite3.connect(database)
c = conn.cursor()
"""
c.execute(f CREATE TABLE flowers(
        NAME TEXT,
        COLOR TEXT

"""
question = int(input(f"1)Zelim da unesem novi cvet. \n2)Zelim da vidim podatke o cvetu. \n3)Zelim da vidim podtke o svim cvetovima. \n"  ))

if question == 1:
    name = input("Unesite naziv cveta: ")
    color = input("Unesite boju cveta: ")

    new_flower = Flowers(name,color)

    c.execute(f"""
            INSERT INTO flowers \n
            VALUES('{new_flower.name}','{new_flower.color}')
    """)

    conn.commit()
    conn.close()
    print("Cvet je unet u bazu podataka.")

elif question == 2:
    name = input("Unesite ime cveta: ")
    request = f"""
        SELECT *
        FROM flowers
        WHERE NAME = '{name}'
    """

    c.execute(request)
    result = c.fetchall()
    conn.close()

    print(f"-----------------")
    print(f"Naziv: {result[0][0]}")
    print(f"Boja: {result[0][1]}")
    print(f"-----------------")

elif question == 3:

    requset = """
        SELECT *
        FROM flowers
    """ 
    c.execute(requset)
    all_flowers = c.fetchall()
    conn.close()

    for i in all_flowers:
        print(f"-----------------")
        print(f"Naziv: {i[0]}")
        print(f"Boja: {i[1]}")
        print(f"-----------------")
