# To zadanie wprowadza kluczowe pojęcie relacji.
# Chcemy przypisać studentów do audytoriów (np. na egzamin). 
# Aby to zrobić, stwórz trzecią tabelę o nazwie przypisania w tej samej bazie uczelnia.db. 
# Tabela powinna mieć strukturę:
# id_przypisania (INTEGER, klucz główny)
# id_studenta (INTEGER) – będzie to tzw. klucz obcy wskazujący na id_studenta w tabeli studenci . id_audytoriu

import sqlite3

def utworz_tabele_przypisania():
    conn = sqlite3.connect("uczelnia.db")
    cursor = conn.cursor()

    # (opcjonalnie, ale dobre praktyki)
    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS przypisania (
        id_przypisania INTEGER PRIMARY KEY,
        id_studenta INTEGER,
        id_audytorium INTEGER,

        FOREIGN KEY (id_studenta)
            REFERENCES studenci(id_studenta),

        FOREIGN KEY (id_audytorium)
            REFERENCES audytoria(id_audytorium)
    )
    """)

    conn.commit()
    conn.close()

    print("Tabela 'przypisania' została utworzona.")


utworz_tabele_przypisania()
        
        
        
    
    