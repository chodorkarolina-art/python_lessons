# Zadanie 1 – Stwórz tabelę książek
# Napisz skrypt, który połączy się z bazą biblioteka.db i stworzy w niej tabelę ksiazki. Tabela
# powinna mieć następujące kolumny:
# id (INTEGER, klucz główny)
# tytul (TEXT, nie może być pusty)
# autor (TEXT, nie może być pusty)
# rok_wydania (INTEGER)

import sqlite3

def stworz_tab_ksiazki():
    with sqlite3.connect('biblioteka.db') as conn:
        c = conn.cursor()
        
        c.execute('''
        CREATE TABLE IF NOT EXISTS ksiazki (
        id_ksiazka INTEGER PRIMARY KEY,
        tytul TEXT NOT NULL,
        autor TEXT NOT NULL,
        rok_wydania INTEGER
        )
        ''')
        # Zatwierdzamy zmiany w bazie danych
        conn.commit()
        
        print("Tabela 'ksiazki' została utworzona.")
    
stworz_tab_ksiazki()