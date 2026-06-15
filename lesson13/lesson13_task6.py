# Napisz skrypt, który w nowej bazie uczelnia.db stworzy dwie tabele:
# studenci z kolumnami: id_studenta (klucz główny), imie (TEXT), nazwisko (TEXT).
# audytoria z kolumnami: id_audytorium (klucz główny), nazwa_budynku (TEXT),
# numer_sali (INTEGER).

import sqlite3

def utworz_baze():
    conn = sqlite3.connect("uczelnia.db")
    cursor = conn.cursor()

    # WAŻNE: włączenie kluczy obcych (SQLite domyślnie je ignoruje)
    cursor.execute("PRAGMA foreign_keys = ON")

    # Tabela studenci
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS studenci (
        id_studenta INTEGER PRIMARY KEY,
        imie TEXT,
        nazwisko TEXT
    )
    """)

    # Tabela audytoria
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS audytoria (
        id_audytorium INTEGER PRIMARY KEY,
        nazwa_budynku TEXT,
        numer_sali INTEGER
    )
    """)

    # Tabela relacyjna (N:M)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS przypisania (
        id_przypisania INTEGER PRIMARY KEY,
        id_studenta INTEGER,
        id_audytorium INTEGER,

        FOREIGN KEY (id_studenta)
            REFERENCES studenci(id_studenta),

        FOREIGN KEY (id_audytorium)
            REFERENCES audytoria(id_audytorium)
    )
    """)

    conn.commit()
    conn.close()

    print("Baza danych 'uczelnia.db' została utworzona.")


utworz_baze()