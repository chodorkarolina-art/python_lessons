# 1. Opowieść o sobie
print("""Nazywam się Paweł.
Interesuję się programowaniem i analizą danych.
Lubię pracować z Pythonem i automatyką.
Uczę się Pythona, żeby rozwijać swoje umiejętności techniczne.""")

# 2. Interaktywny dialog
imie = input("Podaj swoje imię: ")
wiek = input("Podaj swój wiek: ")
miasto = input("Podaj swoje miasto: ")

print(
    "A więc, masz na imię",
    imie + ", masz",
    wiek,
    "lat i mieszkasz w mieście",
    miasto + ".",
)
# 3. Obwód prostokąta
dlugosc = float(input("Podaj długość: "))
szerokosc = float(input("Podaj szerokość: "))

obwod = 2 * (dlugosc + szerokosc)

print("Obwód prostokąta wynosi:", obwod)
# 4. Kody znaków
imie = "pawel"

print(f"""Kod ASCII pierwszej małej litery imienia: {ord(imie[0].lower())}
Kod ASCII pierwszej dużej litery imienia: {ord(imie[0].upper())}""")

# 5. Kreator postaci
rasa = input("Podaj rasę: ")
klasa = input("Podaj klasę: ")

print("Stworzono postać:", rasa, klasa)
# 6. Wyrażenie logiczne
prawo_jazdy = input("Czy masz prawo jazdy (tak/nie): ")
wiek = int(input("Podaj wiek: "))

wynik = (wiek >= 18) and (prawo_jazdy == "tak")

print(wynik)


# 7. Praktyka z venv (polecenia w terminalu)
# mkdir project_test
# cd project_test

# python -m venv venv

# # aktywacja (Windows)
# venv\Scripts\activate

# # aktywacja (Linux/Mac)
# source venv/bin/activate

# pip list

# deactivate
# 8. Ubuntu – nawigacja
# cd Desktop
# mkdir moj_pierwszy_projekt
# cd moj_pierwszy_projekt

# touch main.py

# ls
# 9. Zen w częściach
import this

# this.d <= słownik-mapa pokazujący, jaki znak mamy zastąpić innym

res = ""
for c in this.s:
    # get zwraca wartosc dla klucza c lub zwróci wartość domyślną, która jest drugim argumentem. domyślnie None
    res += this.d.get(c, c)

# dzielimy wynik/zdekodowany string na linie po `\n` czyli znaku nowej linii
res_lines = res.split("\n")

# wyswietlamy 2 pierwsze elementy listy
print(res_lines[:2])

# 10. Konwerter temperatury
c = float(input("Podaj temperaturę w stopniach Celsjusza: "))

f = c * 9 / 5 + 32

print("Temperatura", c, "°C to", f, "°F")
