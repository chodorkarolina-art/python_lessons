# Napisz funkcję w Pythonie znajdz_sale_studenta(nazwisko), która przyjmuje nazwisko
# studenta jako argument. Funkcja powinna połączyć się z bazą, a następnie znaleźć i
# wyświetlić informację, w którym budynku i w jakiej sali znajduje się dany student.
# Tip
# Aby rozwiązać to zadanie, będziesz potrzebować klauzuli JOIN w zapytaniu SELECT.
# Pozwala ona łączyć wiersze z dwóch lub więcej tabel na podstawie powiązanych
# kolumn.
# Przykład: SELECT t1.kolumna, t2.kolumna FROM tabela1 AS t1 JOIN tabela2 AS t2
# ON t1.id = t2.id_z_tabeli1;

import sqlite3

def znajdz_sale_studenta(nazwisko):
    
    conn = sqlite3.connect("uczelnia.db")
    cursor = conn.cursor()
    
    qr = """--sql
    SELECT a.nazwa_budynku, a.numer_sali
    FROM audytoria as a
    JOIN przypisania as p 
    ON a.id_audytorium = p.id_audytorium
    JOIN studenci as s 
    ON s.id_studenta = p.id_studenta
    WHERE s.nazwisko = ?
    """
    
    cursor.execute(qr, (nazwisko,))
    wynik = cursor.fetchall()
    
    conn.close()
    
    if wynik:
        for budynek, sala in wynik:
            print(f"Student {nazwisko} ma zajęcia w budynku {budynek}, sala {sala}")
    else:
        print(f"Nie znaleziono studenta o nazwisku {nazwisko}")
    
  