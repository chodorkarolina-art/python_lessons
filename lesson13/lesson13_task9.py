# Napisz skrypt, który dokona przypisań. 
# Dla każdego studenta z tabeli studenci dodaj wpis do tabeli przypisania, łącząc go z jednym z audytoriów.

import sqlite3

def dodaj_przypisania():
    conn = sqlite3.connect("uczelnia.db")
    cursor = conn.cursor()

    # pobranie ID studentów
    cursor.execute("SELECT id_studenta FROM studenci")
    studenci = cursor.fetchall()

    # pobranie ID audytoriów
    cursor.execute("SELECT id_audytorium FROM audytoria")
    audytoria = cursor.fetchall()

    przypisania = []

    for i, student in enumerate(studenci):
        id_studenta = student[0]
        id_audytorium = audytoria[i % len(audytoria)][0]

        przypisania.append((id_studenta, id_audytorium))

    cursor.executemany("""
        INSERT INTO przypisania (id_studenta, id_audytorium)
        VALUES (?, ?)
    """, przypisania)

    conn.commit()
    conn.close()

    print("Przypisania zostały dodane.")


dodaj_przypisania()