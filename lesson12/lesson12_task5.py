# Napisz program, który próbuje otworzyć i odczytać plik o nazwie nieistniejacy.txt. 
# Użyj bloku try...except, aby obsłużyć wyjątek FileNotFoundError i wyświetlić przyjazny komunikat użytkownikowi.

try:
    with open("nieistniejący.txt", "r", encoding="utf-8") as plik:
        zawartosc = plik.read()
        print(zawartosc)
        
except FileNotFoundError:
    print("Błąd: Plik nie został znaleziony. Sprawdź nazwę pliku i spróbuj ponownie")