# Napisz skrypt, który pobierze i wyświetli w konsoli wszystkie książki (wszystkie kolumny) z tabeli ksiazki.

import sqlite3

def pokaz_ksiazki():
    with sqlite3.connect('biblioteka.db') as conn:
        c = conn.cursor()
        
        c.execute("SELECT * FROM ksiazki")
        
        ksiazki = c.fetchall()

        for ksiazka in ksiazki:
            print(ksiazka)

pokaz_ksiazki()