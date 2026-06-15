# Zadanie 4 – Średnia cena książki
# Napisz zapytanie, które obliczy średnią cenę produktów w kategorii "Książki". Użyj AVG().

import sqlite3

def zadanie4():
    
    qr = """--sql
    select avg(p.cena)
    from produkty as p
    join kategorie as k
        on p.id_kategorii = k.id_kategorii
    where k.nazwa_kategorii = 'Książki'
    """    
    with sqlite3.connect('sklep.db') as conn:
        return conn.cursor().execute(qr).fetchone()[0]
    
if __name__ == "__main__":
    print(f"Średnia cena produktów z kategorii Książka to: {zadanie4()} zł")
       