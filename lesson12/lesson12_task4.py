# Napisz funkcję bezpieczne_dzielenie(a, b), która zwraca wynik dzielenia a / b. Użyj blok try...except, 
# aby obsłużyć błąd ZeroDivisionError.
# Jeśli wystąpi ten błąd, funkcja powinna zwrócić None i wyświetlić komunikat "Błąd: Dzielenie przez zero!".

def bezpieczne_dzielenie(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print(" Błąd: Dzielenie przez 0!")
        return None
    
print(bezpieczne_dzielenie(120, 10))
print(bezpieczne_dzielenie(10, 0))