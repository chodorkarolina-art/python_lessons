# Napisz skrypt, który dokona przypisań. 
# Dla każdego studenta z tabeli studenci dodaj wpis do tabeli przypisania, łącząc go z jednym z audytoriów.

import sqlite3

conn = sqlite3.connect("uczelnia.db")
cursor = conn.cursor()

def dodaj_przypisania():
    przypisania = [
        (1,1),
        (2,2),
        (3,3),
        (4,1)
    ]

    query = """--sql
    INSERT INTO przypisania (id_studenta, id_audytorium)
    VALUES (?, ?)
    """
    
    cursor.executemany(query, przypisania)

    conn.commit()
    conn.close()

dodaj_przypisania()

print("Przypisania zostały dodane.")


# import sqlite3

# conn = sqlite3.connect("uczelnia.db")
# cursor = conn.cursor()

# def dodaj_przypisania():

#     # pobranie studentów i audytoriów
#     cursor.execute("SELECT id_studenta FROM studenci")
#     studenci = cursor.fetchall()

#     cursor.execute("SELECT id_audytorium FROM audytoria")
#     audytoria = cursor.fetchall()

#     przypisania = []

#     for i, student in enumerate(studenci):
#         id_studenta = student[0]
#         id_audytorium = audytoria[i % len(audytoria)][0]

#         przypisania.append((id_studenta, id_audytorium))

#     query = """
#     INSERT INTO przypisania (id_studenta, id_audytorium)
#     VALUES (?, ?)
#     """

#     cursor.executemany(query, przypisania)

#     conn.commit()
#     conn.close()

# dodaj_przypisania()

# print("Przypisania zostały dodane.")