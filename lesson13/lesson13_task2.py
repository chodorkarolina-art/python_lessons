# Oblicz i wyświetl łączną wartość wszystkich produktów z kategorii "Elektronika". 
# Użyj funkcji SUM() oraz klauzuli WHERE z JOIN.
import sqlite3

def zadanie3():

    qr = """--sql
    select sum(p.cena)
    from produkty as p
    join kategorie as k
        on p.id_kategorii = k.id_kategorii
    where k.nazwa_kategorii = 'Elektronika'
    """
    with sqlite3.connect('sklep.db') as conn:
        return conn.cursor().execute(qr).fetchone()[0]

if __name__ == "__main__":
    print(f"Suma cen produktów z kategorii Elektronika : {zadanie3()} zł.")
    