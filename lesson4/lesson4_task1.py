# Kalkulator zniżek: 
# Napisz program, który oblicza cenę biletu. Cena bazowa to 100 PLN.
# Jeśli użytkownik jest studentem ( tak/nie ) LUB ma mniej niż 18 lat, 
# przysługuje mu 50% zniżki. 
# Użyj operatorów or i and.

cena = 100 

wiek = int(input("Wiek: "))
student = input("Czy student: tak/nie: ")

if student == "tak" or wiek < 18:
    cena *= 0.5

print("Cena", cena, "PLN")

