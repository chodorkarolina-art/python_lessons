# Napisz skrypt, który wypełni tabele studenci i audytoria przykładowymi danymi. 
# Dodaj co najmniej 4 studentów i 3 audytoria.

import sqlite3

def dodaj_dane():
    conn = sqlite3.connect("uczelnia.db")
    cursor = conn.cursor()

    studenci = [
        ("Antoni", "Nowak"),
        ("Katarzyna", "Śliwka"),
        ("Piotr", "Góral"),
        ("Anna", "Zając")
    ]

    audytoria = [
        ("A", 101),
        ("B", 202),
        ("C", 53)
    ]

    cursor.executemany(
        "INSERT INTO studenci (imie, nazwisko) VALUES (?, ?)",
        studenci
    )

    cursor.executemany(
        "INSERT INTO audytoria (nazwa_budynku, numer_sali) VALUES (?, ?)",
        audytoria
    )

    conn.commit()
    conn.close()

    print("Dane zostały dodane do uczelnia.db")


dodaj_dane()    