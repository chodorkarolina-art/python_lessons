# Napisz skrypt, który wyświetli imiona i adresy e-mail wszystkich klientów z tabeli Klienci. (proste)

import sqlite3

def zadanie5():
    qr = """
    SELECT imie, email
    FROM Klienci
    """

    with sqlite3.connect('sklep.db') as conn:
        cursor = conn.cursor()
        return cursor.execute(qr).fetchall()


if __name__ == "__main__":
    klienci = zadanie5()

    for imie, email in klienci:
        print(f"{imie} - {email}")
    