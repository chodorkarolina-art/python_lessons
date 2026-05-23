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

# python dokonuje optymalizacji pamieci stąd często nie duplikuje w pamięci tych samych wartosci
# obejsc to mozna poprzez tworzenie zmiennych nie wprost, czyli np. poprzez rzutowanie


