# Średnia ocen: Napisz funkcję oblicz_srednia(*args) , 
# *args = Gwiazdka (*) przed nazwą parametru oznacza, że funkcja może przyjąć dowolną liczbę argumentów pozycyjnych.
# W praktyce wszystkie przekazane wartości trafiają do jednej zmiennej args jako krotka (tuple).
# która przyjmuje dowolną liczbę ocen (argumentów pozycyjnych)
# i zwraca ich średnią arytmetyczną. 
# sum(args) dodaje wszystkie liczby, np. 4 + 5 + 3 = 12
# len(args) to liczba elementów, np. 3
# Jeśli nie podano żadnej oceny, powinna zwrócić 0.
# :.2f oznacza: liczba zmiennoprzecinkowa z 2 miejscami po przecinku

def oblicz_srednia (*args):
    if len(args) == 0:
        return 0
    return sum(args) / len(args)

print(f"{oblicz_srednia(1,3,4,3,6,4,5):.2f}")
