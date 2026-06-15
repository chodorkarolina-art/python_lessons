# Komentowanie kodu: Poniżej znajduje się fragment kodu. 
# Dodaj do niego komentarze jednoliniowe oraz docstring dla funkcji, wyjaśniając, co robi każda część.


def oblicz_pole_prostokata(a, b):
    """
    Funkcja oblicza pole prostokąta na podstawie długości dwóch boków.
    Zwraca wynik mnożenia a * b.
    """
    # Obliczenie pola prostokąta jako iloczynu boków
    pole = a * b
    
    # Zwrócenie obliczonej wartości pola
    return pole

# Długości boków prostokąta
bok_a = 10
bok_b = 20

# Wywołanie funkcji i zapis wyniku
wynik = oblicz_pole_prostokata(bok_a, bok_b)

# Wyświetlenie wyniku w czytelnej formie
print(f"Pole prostokąta o bokach {bok_a} i {bok_b} wynosi {wynik}.")