# Napisz skrypt, który wyświetli nazwy i ceny wszystkich produktów, których cena jest wyższa
# niż średnia cena wszystkich produktów w sklepie. Wykorzystaj podzapytanie.

import sqlite3

def zadanie6():

    qr = """--sql
    select 
        nazwa_produktu,
        cena 
    from Produkty   
    where cena > (select avg(cena) from Produkty)
    """
    
    with sqlite3.connect('sklep.db') as conn:
        cursor = conn.cursor()
        return cursor.execute(qr).fetchall()

if __name__ == "__main__":
    print(zadanie6())

