# Sprawdzanie zakresu: Zdefiniuj zmienną globalną POZIOM_DOSTEPU = "user" . 
# Napisz funkcję, która próbuje zmienić tę zmienną na "admin" bez użycia słowa kluczowego global . 
# Wewnątrz funkcji stwórz zmienną lokalną o tej samej nazwie. 
# Wyświetl wartość zmiennej wewnątrz i na zewnątrz funkcji, aby zobaczyć różnicę.

POZIOM_DOSTEPU = "user"

def zmien_poziom():
    POZIOM_DOSTEPU = "admin" # zmienna lokalna (Nie zmienia globalnej)
    print("Wewnątrz funkcji:", POZIOM_DOSTEPU)

zmien_poziom()

print("Poza funkcją:", POZIOM_DOSTEPU)
