# Adnotacje i docstring: Weź funkcję kalkulator z zadania 1. 
# Dodaj do niej pełne adnotacje typów dla wszystkich parametrów i wartości zwracanej. 
# Napisz również kompletny docstring opisujący jej działanie.

def kalkulator (a:float,b:float,operacja:str) -> float | str:
    """ Wykonuje podstawowe operacje matematyczne na dwóch liczbach
    
    a (flaot) = pierwsza_liczba
    b (flaot) = druga_liczba
    operacja(str) = symbol operacji do wyświetlenia/wykonania
    
    Dozwolone operacje matemetyczne :
    "+" dodawanie
    "-" odejmowanie
    "*" mznożenie
    "/" dzielenie
    
    Zwraca 
    float : wynik operacji matematycznej
    str : komunikat o błędzie, np. " Dzielenie przez 0
     
    kalkulator(5,3, "+")
    8
    kalkulator(5,3, "-")
    2  
    kalkulator(5,0, "*")
    Nie można dzielić przez 0
    kalkulator(5,%, "/")
    Nieznana operacja
     
    """
    if operacja == "+":
        return a + b 
    if operacja == "-":
        return a - b
    if operacja == "*":
        return a * b
    if operacja == "/":
        if b == 0:
            return "Nie można dzielić przez 0"
        return a / b
    return "Nieznana operacja"



    