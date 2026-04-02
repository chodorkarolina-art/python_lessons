num1 = float(input("Podaj pierwszą liczbę: "))
num2 = float(input("Podaj drugą liczbę: "))
operation = input("Wybierz operację (+, -, *, /): ")

if operation == "+":
    result = num1 + num2

elif operation == "-":
    result = num1 - num2
    
elif operation == "*":
    result = num1 * num2
    
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Nie można dzielić przez zero!"

print(f"Wynik: {result}")