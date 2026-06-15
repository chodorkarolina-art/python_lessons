# Oblicz i wyświetl łączną wartość wszystkich produktów z kategorii "Elektronika". 
# Użyj funkcji SUM() oraz klauzuli WHERE z JOIN.
import sqlite3

def zadanie3():
    qr = """
    SELECT SUM(p.cena)
    FROM Produkty AS p
    JOIN Kategorie AS k
        ON p.id_kategorii = k.id_kategorii
    WHERE k.nazwa_kategorii = 'Elektronika'
    """

    with sqlite3.connect('sklep.db') as conn:
        cursor = conn.cursor()
        wynik = cursor.execute(qr).fetchone()[0]
        return wynik


if __name__ == "__main__":
    suma = zadanie3()

    print(f"Suma cen produktów z kategorii Elektronika: {suma} zł")
    