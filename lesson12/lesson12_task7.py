# To zadanie wprowadza kluczowe pojęcie relacji.
# Chcemy przypisać studentów do audytoriów (np. na egzamin). 
# Aby to zrobić, stwórz trzecią tabelę o nazwie przypisania w tej samej bazie uczelnia.db. 
# Tabela powinna mieć strukturę:
# id_przypisania (INTEGER, klucz główny)
# id_studenta (INTEGER) – będzie to tzw. klucz obcy wskazujący na id_studenta w tabeli studenci . id_audytoriu

import sqlite3

conn = sqlite3.connect("uczelnia.db")
cursor = conn.cursor()

def utworz_tabele_przypisania():
    
    query_przypisania = """
    CREATE TABLE IF NOT EXISTS przypisania (
        id_przypisania INTEGER PRIMARY KEY, 
        id_studenta INTEGER,
        id_audytorium INTEGER,
        
        FOREIGN KEY (id_studenta)
        REFERENCES studenci(id_studenta),
        
        FOREIGN KEY (id_audytorium)
        REFERENCES audytoria(id_audytorium)
        )
        """
        
    cursor.execute(query_przypisania)
    conn.commit()
    conn.close()

utworz_tabele_przypisania()
        
        
        
    
    