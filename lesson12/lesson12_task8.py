# Stwórz prosty kalkulator, który prosi użytkownika o podanie dwóch liczb i operacji (+, -, *, /).
# Całość umieść w pętli while True , aby program działał do momentu przerwania.
# Użyj bloku try...except do obsługi:
# ValueError , jeśli użytkownik wpisze coś, co nie jest liczbą.
# ZeroDivisionError przy próbie dzielenia przez zero.
# Użyj bloku else , aby wyświetlić wynik tylko wtedy, gdy nie było błędu.
# Użyj bloku finally , aby na koniec każdej iteracji pętli wyświetlić komunikat "Koniec obliczeń.".

while True:
    try:
        liczba1 = float(input("podaj pierwsza liczbę: "))
        liczba2 = float(input("podaj drugą liczbę: "))
        operacja = input("podaj operację (+, -, *, /): ")

        if operacja == "+":
            wynik = liczba1 + liczba2
        elif operacja == "-":
            wynik = liczba1 - liczba2
        elif operacja == "*":
            wynik = liczba1 * liczba2
        elif operacja == "/":
            wynik = liczba1 / liczba2
        else:
            print("Niepoprawna operacja!")
            continue

    except ValueError:
        print("Błąd: musisz podać liczbę!")

    except ZeroDivisionError:
        print("Błąd: nie można dzielić przez zero!")

    else:
        print("Wynik:", wynik)

    finally:
        print("Koniec obliczeń.")
                          
            
            