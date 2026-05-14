# Eksport do CSV: Masz listę słowników: produkty = [{"nazwa": "Mleko", "cena": 3.50}, {"nazwa": "Chleb", "cena": 4.20}] . 
# Zapisz te dane do pliku produkty.csv ,gdzie pierwszy wiersz to nagłówki ("nazwa", "cena").  
# DictWriter to klasa z modułu csv, która służy do: zapisywania słowników do pliku CSV
# "produkty.csv" → nazwa pliku
# "w" → tryb zapisu (write)
# newline="" → usuwa puste linie (ważne w CSV)
# encoding="utf-8" → obsługa polskich znaków
# with → automatycznie zamyka plik po zakończeniu
# writer.writeheader() zapisuje pierwszą linię:
# writer.writerows(produkty_csv)  zapisuje każdy słownik jako wiersz(tabelka do pobrania):


import csv

produkty_csv = [
    {"nazwa": "Mleko", "cena": 3.50}, 
    {"nazwa": "Chleb", "cena": 4.20}
]

with open("produkty.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["nazwa", "cena"])
    writer.writeheader()
    writer.writerows(produkty_csv)
    
print("Zapisano plik CSV")    