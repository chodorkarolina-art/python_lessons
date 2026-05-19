# Napisz skrypt, który wyświetli imiona i adresy e-mail wszystkich klientów z tabeli Klienci. (proste)

import sqlite3

def zadanie5():
    
    qr = """--sql
    select 
        klienci.imie,
        klienci.email
    from klienci
    """
    
    with sqlite3.connect('sklep.db') as conn:
        cursor = conn.cursor()
        return cursor.execute(qr).fetchall()

if __name__ == "__main__":
    print(zadanie5())
    