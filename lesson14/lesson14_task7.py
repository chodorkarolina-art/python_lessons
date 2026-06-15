# Napisz skrypt, który wyświetli nazwy wszystkich produktów zamówionych 
# przez klienta o imieniu 'Anna Nowak'. Będziesz potrzebować połączyć dane z czterech tabel:
# Klienci, Zamowienia, Zamowienia_Produkty i Produkty.


import sqlite3

def zadanie7():
    qr = """
    SELECT p.nazwa_produktu
    FROM Klienci k
    JOIN Zamowienia z ON k.id_klienta = z.id_klienta
    JOIN Zamowienia_Produkty zp ON z.id_zamowienia = zp.id_zamowienia
    JOIN Produkty p ON zp.id_produktu = p.id_produktu
    WHERE k.imie = 'Anna Nowak'
    """

    with sqlite3.connect('sklep.db') as conn:
        cursor = conn.cursor()
        return cursor.execute(qr).fetchall()


if __name__ == "__main__":
    wyniki = zadanie7()

    for (produkt,) in wyniki:
        print(produkt)