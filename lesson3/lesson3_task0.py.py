# Mini-kalkulator: Napisz program, który prosi użytkownika o podanie dwóch liczb, 
# a następnie wyświetla wynik ich dodawania, odejmowania, mnożenia i dzielenia. 
# Pamiętaj o konwersji typów z input()

def calculator(a: float | int, b: float | int) -> None:
    result1 = a * b 
    result2 = a - b 
    result3 = a / b 
    result4 = a
    
    print(result1, result2, result3, result4, sep="\n")
    
    
def main():
    a = float(input("Podaj pierwszą liczbę: "))
    b = float(input("Podaj drugą liczbę: "))    
    
    calculator(a, b)
    
if __name__ == "__main__":
    main()
    
    
    
