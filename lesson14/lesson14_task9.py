# Napisz w Pythonie funkcję znajdz_produkty_w_kategorii(nazwa_kategorii), która przyjmuje
# jako argument nazwę kategorii i zwraca listę krotek (nazwa_produktu, cena) dla wszystkich produktów w tej kategorii.

import sqlite3

def znajdz_produkty_w_kategorii(nazwa_kategorii):
    
    qr = """--sql
    select 
        produkty.nazwa_produktu,
        produkty.cena
    from produkty
    inner join kategorie
        on produkty.id_kategorii = kategorie.id_kategorii
    where kategorie.nazwa_kategorii = ?
    """
    
    with sqlite3.connect('sklep.db') as conn:
        cursor = conn.cursor()
        return cursor.execute(qr, (nazwa_kategorii,)).fetchall()
    
print(znajdz_produkty_w_kategorii("Elektronika"))    
print(znajdz_produkty_w_kategorii("Książki"))
print(znajdz_produkty_w_kategorii("Dom i ogród"))  
  