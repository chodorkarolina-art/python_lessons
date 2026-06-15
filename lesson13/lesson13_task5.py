# Wybierz jedną z dodanych książek i napisz skrypt, który zaktualizuje jej rok_wydania na inną wartość. 
# Po aktualizacji wyświetl dane tej książki, aby potwierdzić, że zmiana się powiodła.

import sqlite3

def zaktualizuj_rok_wydania(autor, tytul, nowy_rok):
    with sqlite3.connect('biblioteka.db') as conn:
        c = conn.cursor()
        c.execute("""UPDATE ksiazki
                  SET rok_wydania = ?
                  WHERE autor = ? AND tytul = ?""",
                  (nowy_rok, autor, tytul))
        conn.commit()
        c.execute("select * from ksiazki where autor = ? and tytul = ?",(autor, tytul))
        
        return c.fetchall() 
          
if __name__ == "__main__":
    wynik = zaktualizuj_rok_wydania("Ken Follett", "Filary Ziemi", 2026)
    print(wynik)   
