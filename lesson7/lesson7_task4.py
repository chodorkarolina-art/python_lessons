# Logowanie błędów: Zmodyfikuj zadanie 1. tak, aby każdy napotkany wyjątek (wraz z jego treścią) był zapisywany do pliku log.txt , 
# a program kontynuował działanie. Użyj bloku finally , aby upewnić się, że plik z logami jest zawsze zamykany.

func_calc = {
    "+" : lambda x, y: x + y,
    "-" : lambda x, y: x - y, 
    "*" : lambda x, y: x * y,
    "/" : lambda x, y: x / y
} 

while True:
    
    try:
        fnum1 = float(input("Podaj pierwszą liczbę: "))
        fnum2 = float(input("Podaj drugą liczbę: "))
        operacja = input("Podaj operację (+, -, *, /):")   

        
        if operacja not in func_calc:
            raise ValueError("Niepoprawna operacja!")
        
        wynik = func_calc[operacja](fnum1, fnum2)
        
    except ZeroDivisionError as e:
        print(f"Błąd dzielenia przez zero: {e}")
        with open("log.txt", 'a', encoding="utf-8") as log_file:
            log_file.write(f"ZeroDivisionError: {e}\n")    
    
    except ValueError as e:
        print(f"Błąd wartości: {e}")   
        with open("log.txt", 'a', encoding="utf-8") as log_file:
            log_file.write(f"ValueError: {e}\n") 
    else:
        print(f"Wynik: {wynik:.2f}")
        
    finally:
        print("Kolejna operacja...\n")
          
        
