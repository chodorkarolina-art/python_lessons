# Licznik słów: Stwórz program, który pyta o nazwę pliku, odczytuje go, 
# a następnie zlicza i wyświetla całkowitą liczbę słów w tym pliku. 
# Obsłuż błąd FileNotFoundError , jeśli plik nie istnieje.

try:
    nazwa_pliku = input("Podaj nazwę pliku: ")
    
    with open(nazwa_pliku, 'r', encoding="utf-8") as plik:
        tekst = plik.read()
        
        slowa = tekst.split()
        liczba_slow = len(slowa)
        
except FileNotFoundError:
    print("Błąd: plik nie został znaleziony!")
else:
    print(f"Całkowita liczba słów w pliku: {liczba_slow}")
    
    # print("\n")
    
    # with open(nazwa_pliku, "r", encoding="utf-8") as plik:
    #     for linia in plik:
    #         print(plik.read())
    
    
    