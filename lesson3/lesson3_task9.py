# Bramki logiczne: Napisz program, który poprosi o dwie wartości logiczne ( True lub False ). 
# Niech użytkownik wprowadza 1 dla True i 0 dla False . 
# Program powinien wyświetlić wyniki operacji AND oraz OR dla tych dwóch wartości.


a = int(input("Podaj 1 (True) lub 0 (False): "))
b = int(input("Podaj 1 (True) lub 0 (False): "))

a = bool(a)
b = bool(b)

print("AND:", a and b)
print("OR:", a or b)
