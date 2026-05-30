name = int(input("Podaj liczbę całkowitą: "))

binary = bin(name)
hexadecimal = hex(name)

print(f"Liczba {name} w systemie binarnym to: {binary}")
print(f"Liczba {name} w systemie szesnastkowym to: {hexadecimal}")