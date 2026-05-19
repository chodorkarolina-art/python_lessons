# Napisz skrypt, który wyświetli nazwy wszystkich produktów zamówionych 
# przez klienta o imieniu 'Anna Nowak'. Będziesz potrzebować połączyć dane z czterech tabel:
# Klienci, Zamowienia, Zamowienia_Produkty i Produkty.


import sqlite3

def zadanie7():
    
    qr = """--sql
    select 
        produkty.nazwa_produktu
    from klienci
    inner join zamowienia
        on klienci.id_klienta = zamowienia.id_klienta
    inner join zamowienia_produkty
        on zamowienia.id_zamowienia = zamowienia_produkty.id_zamowienia
    inner join produkty
        on zamowienia_produkty.id_produktu = produkty.id_produktu    
    where klienci.imie = 'Anna Nowak'
    """
    
    with sqlite3.connect('sklep.db') as conn:
        cursor = conn.cursor()
        return cursor.execute(qr).fetchall()

if __name__ == "__main__":
    print(zadanie7())