# Logowanie błędów: Zmodyfikuj zadanie 1. tak, aby każdy napotkany wyjątek (wraz z jego treścią) był zapisywany do pliku log.txt , 
# a program kontynuował działanie. Użyj bloku finally , aby upewnić się, że plik z logami jest zawsze zamykany.

func_calc = {
    "+" : lambda x, y: x + y,
    "-" : lambda x, y: x - y,
    "*" : lambda x, y: x * y,
    "/" : lambda x, y: x / y
}

log_file = None

while True:
    try:
        log_file = open("log.txt", "a", encoding="utf-8")

        fnum1 = float(input("Podaj pierwszą liczbę: "))
        fnum2 = float(input("Podaj drugą liczbę: "))
        operacja = input("Podaj operację (+, -, *, /): ")

        if operacja not in func_calc:
            raise ValueError("Niepoprawna operacja!")

        wynik = func_calc[operacja](fnum1, fnum2)
        print(f"Wynik: {wynik:.2f}")

    except ZeroDivisionError as e:
        print(f"Błąd dzielenia przez zero: {e}")
        log_file.write(f"ZeroDivisionError: {e}\n")

    except ValueError as e:
        print(f"Błąd wartości: {e}")
        log_file.write(f"ValueError: {e}\n")

    finally:
        print("Kolejna operacja...\n")
        if log_file:
            log_file.close()
          
        
