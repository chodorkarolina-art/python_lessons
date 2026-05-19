# Napisz skrypt, który znajdzie nazwę i cenę najdroższego produktu w sklepie. Użyj funkcji MAX().

# import sqlite3

# conn = sqlite3.connect('sklep.db')
# cursor = conn.cursor()

# query = """
# SELECT nazwa_produktu, cena
# FROM Produkty
# WHERE cena = (
#     SELECT MAX(cena)
#     FROM Produkty
# )
# """

# cursor.execute(query)
# wynik = cursor.fetchone()


# print(f"Produkct z najwyższą ceną to: {wynik[0]}")
# print(f"Cena: {wynik[1]} zł")

# conn.close()

import sqlite3

def zadanie2():
    qr = """
    SELECT nazwa_produktu, cena
    FROM Produkty
    WHERE cena = (
        SELECT MAX(cena)
        FROM Produkty
        )
        """
    with sqlite3.connect('sklep.db') as conn:
        c = conn.cursor()
        return c.execute(qr).fetchone()
    
if __name__ == "__main__":
    wynik = zadanie2()
        
    print(f"Produkct z najwyższą ceną to: {wynik[0]}")
    print(f"Cena: {wynik[1]} zł")
        