# Napisz skrypt, który pobierze i wyświetli tylko te książki z tabeli ksiazki, 
# które zostały napisane przez Twojego ulubionego autora.

import sqlite3

ULUBIONY_AUTOR = "Ken Follett"

def pokaz_autora_ksiazki(autor):
    with sqlite3.connect('biblioteka.db') as conn:
        c = conn.cursor()
        
        c.execute("SELECT * FROM ksiazki WHERE autor = ?", (autor,))
        
        ksiazki = c.fetchall()
        
        for ksiazka in ksiazki:
            print(ksiazka)
            
            
pokaz_autora_ksiazki(ULUBIONY_AUTOR)   