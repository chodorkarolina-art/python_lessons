# Identyfikator obiektu: Utwórz trzy zmienne ( a , b , c ) z tą samą wartością 256 . 
# Sprawdź i wyświetl ich id() . Następnie utwórz trzy zmienne z wartością 257 i również sprawdź ich id() . 
# Czy widzisz różnicę w zachowaniu Pythona? Wyjaśnij dlaczego w komentarzu.

a, b, c = 256, 256, 256
print(id(a), id(b), id(c))

# niezgodnie z poleceniem, ale uzyskujemy wynik oczekiwany w poleceniu
x = int("257")
y = int("257")
z = int("257")

print(id(x), id(y), id(z))

# Python przechowuje w pamięci jedną wspólną kopię małych liczb całkowitych
# (zwykle z zakresu od -5 do 256). Zjawisko to nazywa się integer interning.
# Dlatego zmienne a, b i c wskazują na ten sam obiekt i mają identyczne id().

# Dla liczb spoza tego zakresu Python nie musi współdzielić obiektów.
# Tworząc liczbę 257 przez int("257"), wymuszamy utworzenie osobnych obiektów,
# dlatego zmienne x, y i z mogą mieć różne id().


