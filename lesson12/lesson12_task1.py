# Napisz skrypt, który doda do tabeli ksiazki (stworzonej w zadaniu 1) trzy dowolne książki.
# Użyj metody executemany do dodania wszystkich książek za jednym razem.


import sqlite3

def dodaj_ksiazki(ksiazki: list[tuple[str, str, int]]):
    with sqlite3.connect('biblioteka.db') as conn:
        c = conn.cursor()
        c.executemany("INSERT INTO ksiazki(tytul, autor, rok_wydania) VALUES(?, ?, ?)", ksiazki)
        
        conn.commit()
        
        print("Ksiązki zostały dodane.")
        
lista_ksiazek = [
    ("Filary Ziemi", "Ken Follett", 1989),
    ("Prowadź swój pług przez kości umarłych", "Olga Tokarczuk", 2009),
    ("Komisarz Forst. Ekspozycja", "Remigiusz Mróz", 2015)
]

dodaj_ksiazki(lista_ksiazek)

with sqlite3.connect("biblioteka.db") as conn:
    c = conn.cursor()

    c.execute("SELECT * FROM ksiazki")

    wyniki = c.fetchall()

    print(wyniki)
    


# with sqlite3.connect("biblioteka.db") as conn:
#     c = conn.cursor()

#     # Usunięcie wszystkich rekordów
#     c.execute("DELETE FROM ksiazki")

#     lista_ksiazek = [
#         ("Filary Ziemi", "Ken Follett", 1989),
#         ("Prowadź swój pług przez kości umarłych", "Olga Tokarczuk", 2009),
#         ("Komisarz Forst. Ekspozycja", "Remigiusz Mróz", 2015)
#     ]

#     c.executemany(
#         "INSERT INTO ksiazki (tytul, autor, rok_wydania) VALUES (?, ?, ?)",
#         lista_ksiazek
#     )

#     conn.commit()

#     c.execute("SELECT * FROM ksiazki")

#     print(c.fetchall())