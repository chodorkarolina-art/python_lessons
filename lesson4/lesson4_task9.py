# Mini-projekt: Prosty kalkulator walut:
# Zdefiniuj kursy w słowniku, np. kursy = {"USD": 4.0, "EUR": 4.3} .
# W pętli while True zapytaj użytkownika o kwotę w PLN i walutę (USD/EUR).
# Użyj if-elif-else , aby sprawdzić wybraną walutę i obliczyć wynik.
# Sformatuj wynik do dwóch miejsc po przecinku, używając f-stringa.
# Zapytaj użytkownika, czy chce kontynuować. Jeśli odpowie "nie", użyj break .

kursy = {"USD": 4.0, "EUR": 4.3, "GBP": 5.0}

while True:
    pln = float(input("Podaj kwotę w PLN: "))

    print("Dostępne waluty:")
    for waluta in kursy:
        print("-", waluta)

    wybor = input("Wybierz walutę z listy: ").upper()

    if wybor in kursy:
        wynik = pln / kursy[wybor]
        print(f"Wynik: {wynik:.2f} {wybor}")
    else:
        print("Nie ma takiej waluty")
        continue

    dalej = input("Czy chcesz kontynuować? (tak/nie): ").lower()
    if dalej == "nie":
        break 