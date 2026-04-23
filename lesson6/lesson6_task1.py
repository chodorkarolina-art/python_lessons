# Sortowanie słownika: Masz słownik oceny = {"Jan": 4, "Anna": 5, "Piotr": 3,"Kasia": 4} . 
# Użyj funkcji sorted() i funkcji lambda, 
# aby posortować elementy słownika (klucz, wartość)
# według ocen (od najwyższej do najniższej)

slownik_oceny = {"Jan": 4, "Anna": 5, "Piotr": 3, "Kasia": 4}
posortowany_slownik = sorted(slownik_oceny.items(), key=lambda x: x[1], reverse=True)
""" slownik_oceny.items() zwraca pary (klucz, wartość)
    key=lambda x: x[1] oznacza sortowanie po wartości (czyli ocenie)
    x to para (klucz, wartość)
    x[1] to wartość (ocena), po której sortujesz 
    reverse=True ustawia kolejność malejącą (od najwyższej do najniższej)
"""
print(posortowany_slownik)