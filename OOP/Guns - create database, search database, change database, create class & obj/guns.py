import sqlite3

db = "guns.db"

class Gun():
    def __init__(self, serial_num,name,type,):
        self.serial_num = serial_num
        self.name = name
        self.type = type

conn = sqlite3.connect(db)
c = conn.cursor()

question = int(input(f"1)Unesite novo oruzije. \n2)Izmenite podatke o oruziju. \n3)Prikazite oruzije \n4)Prikazi sva oruzija \n5)Obrisite oruzije \n"))

if question == 1:
        
    request = (f""" 
        SELECT *
        FROM guns
        """)
    
    c.execute(request)
    result = c.fetchall()

    serial_num = len(result) + 1
    name = input("Unesite naziv oruzija: ")
    type = input("Unesite tip oruzija: ")
    new_gun = Gun(serial_num, name, type)

    c.execute(f""" 
        INSERT INTO guns \n
        VALUES({new_gun.serial_num},'{new_gun.name}','{new_gun.type}')
    """)
    
    conn.commit()
    c.close()
    print(f"Uspesno uneto oruzije sa serijskim brojem: {serial_num}")


elif question == 2:
   
    question = int(input("1)Zelim da izmenim ime. /n2)Zelim da izmenim tip.\n"))

    while question not in [1,2]:
        question = int(input("Pokusajte ponovo: "))
    
    if question == 1:

        serial_key = int(input("Unesite serijski broj oruzija: "))
            
        request = (f""" 
            SELECT *
            FROM guns
            WHERE serial_num = {serial_key}
        """)
        c.execute(request)
        result = c.fetchall()

        if len(result) > 0:
            new_value = input("Unesite novi naziv oruzija: ")
            request = (f"""
                UPDATE  guns
                SET name = '{new_value}'
                WHERE serial_num = {serial_key}
            """)
            c.execute(request)
            conn.commit()
            c.close
    

    if question == 2:

        serial_key = int(input("Unesite serijski broj oruzija: "))
            
        request = (f""" 
            SELECT *
            FROM guns
            WHERE serial_num = {serial_key}
        """)
        c.execute(request)
        result = c.fetchall()

        if len(result) > 0:
            new_value = input("Unesite novi tip oruzija: ")
            request = (f"""
                UPDATE  guns
                SET type = '{new_value}'
                WHERE serial_num = {serial_key}
            """)
            c.execute(request)
            conn.commit()
            c.close
    
        else:
            print("Oruzine sa ovim serijskim brojem ne postoji.")

elif question == 3:
    serial_key = int(input("Unesite serijski broj oruzija: "))
    
    request = (f""" 
        SELECT *
        FROM guns
        WHERE serial_num = {serial_key}
    """)
    c.execute(request)
    result = c.fetchall()
    c.close()

    print(f"-----------------")
    print(f"Serijski broj:  {result[0][0]}")
    print(f"Naziv oruzija:  {result[0][1]}")
    print(f"Tip oruzija:  {result[0][2]}")
    print(f"-----------------")

elif question == 4:

    request = (f""" 
        SELECT *
        FROM guns  
    """)
    c.execute(request)
    all_guns = c.fetchall()
    c.close()
    for i in all_guns:
        print(f"-----------------")
        print(f"Serijski broj:  {i[0]}")
        print(f"Naziv oruzija:  {i[1]}")
        print(f"Tip oruzija:  {i[2]}")
        print(f"-----------------")



elif question == 5:

    serial_key = int(input("Unesite serijski broj oruzija: "))
        
    request = (f""" 
        SELECT *
        FROM guns
        WHERE serial_num = {serial_key}
    """)
    c.execute(request)
    result = c.fetchall()
    
    if len(result) > 0:
        request = (f"""
            DELETE FROM guns
            WHERE serial_num = {serial_key}
        """)
        print(f"Uspesno je obrisano oruzje pod serijskim brojem {serial_key}")
        c.execute(request)
        conn.commit()
        c.close()
    
    
    else:
        print("Oruzine sa ovim serijskim brojem ne postoji.")

