# Napisz skrypt, który doda do tabeli ksiazki (stworzonej w zadaniu 1) trzy dowolne książki.
# Użyj metody executemany do dodania wszystkich książek za jednym razem.


import sqlite3

def dodaj_ksiazki(ksiazki: list[tuple[str, str, int]]) -> None:
    with sqlite3.connect("biblioteka.db") as conn:
        c = conn.cursor()

        c.executemany(
            """
            INSERT INTO ksiazki (tytul, autor, rok_wydania)
            VALUES (?, ?, ?)
            """,
            ksiazki
        )

        conn.commit()
        print("Książki zostały dodane.")


def pokaz_ksiazki() -> None:
    with sqlite3.connect("biblioteka.db") as conn:
        c = conn.cursor()

        c.execute("SELECT * FROM ksiazki")
        wyniki = c.fetchall()

        for ksiazka in wyniki:
            print(ksiazka)


# dane testowe
lista_ksiazek = [
    ("Filary Ziemi", "Ken Follett", 1989),
    ("Prowadź swój pług przez kości umarłych", "Olga Tokarczuk", 2009),
    ("Komisarz Forst. Ekspozycja", "Remigiusz Mróz", 2015)
]

# wykonanie
dodaj_ksiazki(lista_ksiazek)
pokaz_ksiazki()
    