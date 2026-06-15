# Stwórz klasę Produkt w Pythonie z atrybutami id_produktu, nazwa_produktu i cena.
# Następnie napisz funkcję pobierz_wszystkie_produkty(), która połączy się z bazą danych,
# pobierze wszystkie produkty i zwróci listę obiektów klasy Produkt. To ćwiczenie pokaże Ci,
# jak ORM automatyzuje mapowanie wierszy na obiekty.

import sqlite3

class Produkt:
    def __init__(self, id_produktu, nazwa_produktu, cena):
        self.id_produktu = id_produktu
        self.nazwa_produktu = nazwa_produktu
        self.cena = cena
    
    def __repr__(self):
        return f"Produkt(id={self.id_produktu}, nazwa='{self.nazwa_produktu}', cena={self.cena})"
    
def pobierz_wszystkie_produkty():
        
    qr = """--sql
    select 
        id_produktu,
        nazwa_produktu,
        cena
    from produkty
    """
    with sqlite3.connect('sklep.db') as conn:
        cursor = conn.cursor()
        rows = cursor.execute(qr).fetchall()
        
    produkty = []
    for row in rows:
        produkt = Produkt(row[0], row[1], row[2])
        produkty.append(produkt)
        
    return produkty

if __name__ == "__main__":
    for p in pobierz_wszystkie_produkty():
        print(p)


    
    