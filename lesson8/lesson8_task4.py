# Asercja w funkcji: Stwórz funkcję oblicz_srednia(lista_ocen) , która zwraca średnią z listy. 
# Użyj assert , aby upewnić się, że przekazana lista nie jest pusta.

def srednia_ocen(liczba_ocen):
    assert len(liczba_ocen) > 0, "Liczba nie może być pusta!"
    
    return sum(liczba_ocen) / len(liczba_ocen)

oceny = [1, 4, 6, 4, 5, 3]

srednia = (srednia_ocen(oceny))
print(f"Średnia ocen: {srednia:.2f}")

