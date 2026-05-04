# Mini-projekt: Sumator liczb z pliku: Napisz program, który:
# a. Pyta użytkownika o nazwę pliku.
# b. Otwiera plik i czyta go linia po linii.
# c. Każdą linię próbuje przekonwertować na liczbę i dodać do sumy.
# d. Ignoruje linie, których nie da się przekonwertować na liczbę (obsługa ValueError).
# e. Obsługuje FileNotFoundError, jeśli plik nie istnieje.
# f. Na końcu, w bloku finally, wyświetla obliczoną sumę (nawet jeśli wystąpiły błędy po
# drodze).


def sumator_liczb_z_pliku():
    nazwa_pliku = input("Podaj nazwę pliku")
    suma = 0
    
    try:
        with open(nazwa_pliku, "r", encoding="utf-8") as plik:
            for linia in plik:
                try:
                    liczba = float(linia.strip())
                    suma += liczba
                except ValueError:
                    continue    
                
    except FileNotFoundError:
        print(f"Plik {nazwa_pliku} nie istnieje")
        return
    
    print(f"Suma liczb z pliku: {suma}") 
    
sumator_liczb_z_pliku()            