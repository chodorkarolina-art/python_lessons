# Napisz skrypt, który wypełni tabele studenci i audytoria przykładowymi danymi. 
# Dodaj co najmniej 4 studentów i 3 audytoria.

import sqlite3

conn = sqlite3.connect("uczelnia.db")
cursor = conn.cursor()

def dodaj_studenta():
    studenci = [("Antoni", "Nowak"),
                 ("Katarzyna", "Śliwka"),
                 ("Piotr", "Góral"),
                 ("Anna", "Zając")]
    
    query = """--sql
    INSERT INTO studenci (imie, nazwisko)
    VALUES (?, ?)
    """
    
    cursor.executemany(query, studenci)
    
def dodaj_audytoria():
    audytoria = [
        ("A", 101),
        ("B", 202),
        ("C", 53)
    ]
    
    query = """
    INSERT INTO audytoria (nazwa_budynku, numer_sali)
    VALUES (?, ?)
    """
    
    cursor.executemany(query, audytoria)

dodaj_studenta()
dodaj_audytoria()
  
conn.commit()
conn.close()

print("Dane zostały dodane do tabeli uczelnia.db")    