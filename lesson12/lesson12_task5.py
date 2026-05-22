# Napisz skrypt, który w nowej bazie uczelnia.db stworzy dwie tabele:
# studenci z kolumnami: id_studenta (klucz główny), imie (TEXT), nazwisko (TEXT).
# audytoria z kolumnami: id_audytorium (klucz główny), nazwa_budynku (TEXT),
# numer_sali (INTEGER).

import sqlite3

conn = sqlite3.connect("uczelnia.db")
cursor = conn.cursor()

def utworz_tabele():
    query_studenci = """--sql
    CREATE TABLE IF NOT EXISTS studenci (
        id_studenta INTEGER PRIMARY KEY, 
        imie TEXT,
        nazwisko TEXT
    )
    """
    
    query_audytoria = """--sql
    CREATE TABLE IF NOT EXISTS audytoria (
        id_audytorium INTEGER PRIMARY KEY,
        nazwa_budynku TEXT,
        numer_sali INTEGER
    )
    """
    
    query_przypisania = """--sql
    CREATE TABLE IF NOT EXISTS przypisania (
        id_przypisania INTEGER PRIMARY KEY,
        id_studenta INTEGER,
        id_audytorium INTEGER, 
   
    
    FOREIGN KEY (id_studenta)
        REFERENCES studenci(id_studenta),
        
     FOREIGN KEY (id_audytorium)
        REFERENCES audytoria(id_audytorium)
     )
    """
    
    cursor.execute(query_studenci)
    cursor.execute(query_audytoria)
    cursor.execute(query_przypisania)
    
    conn.commit()
    conn.close()
    
utworz_tabele()   