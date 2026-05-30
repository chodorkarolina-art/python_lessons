# Tworzenie i typowanie: Utwórz zmienne przechowujące Twoje imię (str), wiek (int), średnią
# ocen (float) i status studenta (bool). Wyświetl na ekranie wartość i typ każdej zmiennej.


name = input("Podaj swoje imię: ")
wiek = int(input("Podaj swój wiek: "))
status_studenta = input("Czy jesteś studentem (True/False): ").lower() == "true"

while True:
    średnia_ocen = float(input("Podaj średnią ocen (2.0-5.0): "))
    if 2.0 <= średnia_ocen <= 5.0:
        break
    print("Podaj poprawną wartość!")

print("Imię:", name, " | Typ:", type(name))
print("Wiek:", wiek, " | Typ:", type(wiek))
print("Średnia ocen:", średnia_ocen, "| Typ:", type(średnia_ocen))
print("Status studenta:", status_studenta, "| Typ:", type(status_studenta))

