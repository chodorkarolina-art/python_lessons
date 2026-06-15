# import z CSV: Napisz program, który odczytuje plik produkty.csv i oblicza sumę cen wszystkich produktów. 
# Użyj csv.DictReader , aby łatwiej odwoływać się do kolumn po nazwach.


import csv 

suma = 0 

with open("produkty.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    
    for wiersz in reader:
        suma += float(wiersz["cena"])

print(f"Suma cen produktów: {suma}")        
    
# with open("produkty.csv", "r", encoding="utf-8") as f:
#     print("Zawartość po zapisie:")
#     print(f.read()) 