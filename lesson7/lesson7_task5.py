# Przerzucanie wyjątku: Napisz funkcję przetworz_dane(dane) , 
# która w bloku try...except łapie KeyError (np. przy próbie dostępu do nieistniejącego klucza w słowniku), 
# loguje go, a następnie rzuca ( raise ) nowy, własny wyjątek
# BladPrzetwarzaniaDanychError z informacją, którego klucza brakowało.

class BladPrzetwarzaniaDanychError(Exception):
    pass

def przetworz_dane(dane):
    try:
        wartosc = dane["Klucz"]
        
        print(f"Wartość: {wartosc}")
        
    except KeyError as e:
        blad = f"Brak klucza: {e}"
        
        with open("log.txt", 'a', encoding="utf-8") as log_file:
            log_file.write(f"KeyError: {blad}\n")   
        raise BladPrzetwarzaniaDanychError(
            f"Brak klucza {e}"
            )
        
dane = {"Mag": 13}

try:
    przetworz_dane(dane)
except BladPrzetwarzaniaDanychError as e:
    print(f"Złapano wyjątek: {e}")