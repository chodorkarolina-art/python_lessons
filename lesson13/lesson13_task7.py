# Napisz zapytanie, które wyświetli nazwę każdej kategorii
# oraz liczbę produktów należących do tej kategorii. 
# Użyj JOIN, COUNT() oraz GROUP BY.

import sqlite3

def zadanie8():
    qr = """---sql
    select 
        kategorie.nazwa_kategorii,
        count(produkty.id_produktu)
    from kategorie
    inner join produkty
        on kategorie.id_kategorii = produkty.id_kategorii
    group by kategorie.nazwa_kategorii
    """
    
    with sqlite3.connect('sklep.db') as conn:
        cursor = conn.cursor()
        return cursor.execute(qr).fetchall()

if __name__ == "__main__":
    print(zadanie8())