# Napisz zapytanie, które wyświetli nazwę każdej kategorii
# oraz liczbę produktów należących do tej kategorii. 
# Użyj JOIN, COUNT() oraz GROUP BY.

import sqlite3

def zadanie8():
    qr = """
    SELECT k.nazwa_kategorii,
           COUNT(p.id_produktu)
    FROM Kategorie k
    JOIN Produkty p ON k.id_kategorii = p.id_kategorii
    GROUP BY k.id_kategorii
    """

    with sqlite3.connect('sklep.db') as conn:
        cursor = conn.cursor()
        return cursor.execute(qr).fetchall()


if __name__ == "__main__":
    wyniki = zadanie8()

    for nazwa, liczba in wyniki:
        print(f"{nazwa}: {liczba} produktów")