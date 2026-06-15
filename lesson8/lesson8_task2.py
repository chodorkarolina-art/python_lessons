# Walidator wieku: Stwórz funkcję rejestruj_uzytkownika(wiek) ,
# która rzuca własnym, zdefiniowanym przez Ciebie wyjątkiem WiekNiepoprawnyError , jeśli wiek jest mniejszy niż 
# Napisz kod, który wywołuje tę funkcję i obsługuje ten wyjątek


class WiekNiepoprawnyError(Exception):
    pass

def rejestruj_uzytkownika(wiek):
    if wiek < 18:
        raise WiekNiepoprawnyError("Użytkownik musi mieć powyżej 18 lat!.")
    print("Rejestracja zakończona sukcesem")
    
try:
    rejestruj_uzytkownika(16)
except WiekNiepoprawnyError as e:
    print(f"Błąd: {e}")
else:
    print("Brak błędów podczas rejestracji.")
finally:
    print("Koniec procesu rejestracji")           