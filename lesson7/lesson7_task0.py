# Bezpieczny kalkulator: Napisz program, który w pętli prosi użytkownika o podanie dwóch
# liczb i operacji ( + , - , * , / ). Zaimplementuj pełną obsługę błędów ValueError 
# (gdydane nie są liczbami) i ZeroDivisionError . Dodaj blok else do wyświetlania wyniku i
# finally z komunikatem "Kolejna operacja...".
#lambda definiuje operacje matematyczne w słowniku.

# lambda definiuje operacje matematyczne w słowniku.
# ValueError as e i ZeroDivisionError as e przechwytują błędy i zapisują je do zmiennej e.
# else wykona się tylko wtedy, gdy nie wystąpi żaden wyjątek.
# finally wykona się zawsze — niezależnie od tego, czy był błąd, czy nie.

while True:
    try:
        fnum1 = float(input("Podaj pierwszą liczbę: "))
        fnum2 = float(input("Podaj drugą liczbę: "))
        operacja = input("Podaj operację (+, -, *, /):")   
        func_calc = {
            "+" : lambda x, y: x + y,
            "-" : lambda x, y: x - y, 
            "*" : lambda x, y: x * y,
            "/" : lambda x, y: x / y
        } 
        
        if operacja not in func_calc:
            raise ValueError("Niepoprawna operacja!")
        
        wynik = func_calc[operacja](fnum1, fnum2)
        
    except ZeroDivisionError as e:
        print(f"Błąd dzielenia przez zero: {e}")    
    
    except ValueError as e:
        print(f"Błąd wartości: {e}")   
     
    else:
        print(f"Wynik: {wynik}")
        
    finally:
        print("Kolejna operacja...\n")  