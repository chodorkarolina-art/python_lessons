# Napisz skrypt, który pobierze i wyświetli tylko te książki z tabeli ksiazki, 
# które zostały napisane przez Twojego ulubionego autora.

import sqlite3

ULUBIONY_AUTOR = "Ken Follett"


def pokaz_ksiazki_autora(autor: str) -> None:
    with sqlite3.connect("biblioteka.db") as conn:
        c = conn.cursor()

        c.execute(
            "SELECT * FROM ksiazki WHERE autor = ?",
            (autor,)
        )

        ksiazki = c.fetchall()

        if not ksiazki:
            print("Brak książek tego autora.")
            return

        print(f"Książki autora: {autor}")
        print("-" * 40)

        for ksiazka in ksiazki:
            print(ksiazka)


# uruchomienie
pokaz_ksiazki_autora(ULUBIONY_AUTOR)