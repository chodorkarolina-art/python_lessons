# Znajdowanie liczb pierwszych: Użyj funkcji filter() , aby z listy liczb od 1 do 30 wybrać
# tylko liczby pierwsze. (Wskazówka: napisz pomocniczą funkcję czy_pierwsza(n) , 
# która sprawdza, czy liczba jest pierwsza).

liczby = list(range (1, 31))
liczby_pierwsze = list(filter(
    lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5)+1)), liczby))
"""for i in range(2, int(n**0.5) + 1)
sprawdzamy liczby od 2 do √n (pierwiastek z n),
bo jeśli liczba ma dzielnik, to na pewno znajdzie się on w tym zakresie
2. n % i != 0 sprawdzamy: „czy i nie dzieli liczby n” jeśli reszta z dzielenia ≠ 0 to nie jest dzielnik
3. Generator produkuje kolejne wartości True lub False, np. dla n = 7
"""
print(liczby_pierwsze)     
                  