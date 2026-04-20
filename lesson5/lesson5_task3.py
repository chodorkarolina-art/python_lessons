# Sprawdzanie zakresu: Zdefiniuj zmienną globalną POZIOM_DOSTEPU = "user" . 
# Napisz funkcję, która próbuje zmienić tę zmienną na "admin" bez użycia słowa kluczowego global . 
# Wewnątrz funkcji stwórz zmienną lokalną o tej samej nazwie. 
# Wyświetl wartość zmiennej wewnątrz i na zewnątrz funkcji, aby zobaczyć różnicę.

POZIOM_DOSTEPU = "user"

def zmien_poziom():
    POZIOM_DOSTEPU = "admin" # zmienna lokalna (Nie zmienia globalnej)
    return POZIOM_DOSTEPU

nowy_poziom = zmien_poziom()

print("Zwrócona wartośś:", nowy_poziom)
print("Globalna zmienna:", POZIOM_DOSTEPU)
