# Kalkulator: Napisz funkcję kalkulator(a, b, operacja) , '
# która przyjmuje dwie liczby i string z operacją ( "+" , "-" , "*" lub / "). 
# Funkcja powinna zwracać wynik odpowiedniego działania.

def kalkulator (a,b,operacja):
    if operacja == "+":
        return a + b 
    elif operacja == "-":
        return a - b
    elif operacja == "*":
        return a * b
    elif operacja == "/":
        if b == 0:
            return "Nie można dzielić przez 0"
        return a / b
    else:
        return "Nieznana operacja"

print(kalkulator(5,3, "+"))
print(kalkulator(5,3, "-"))        
print(kalkulator(5,3, "*"))
print(kalkulator(5,3, "/"))    
