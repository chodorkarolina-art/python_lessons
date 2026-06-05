# Błąd konwersji: Napisz program, który świadomie spróbuje przekonwertować słowo "Python" na liczbę całkowitą. 
# Uruchom go, zobacz błąd ValueError , a następnie "napraw" program, 
# umieszczając błędną linię w komentarzu i dodając wyjaśnienie, dlaczego kod nie działał.

# liczba = int("Python")
# ValueError - python wyświetli informację o błędzie. Funkcja int() potrafi zamieniać napisy zawierające cyfry na liczby całkowite.
# może zamieniać tylko napisy reprezentujące liczby całkowite.
# Napis "Python" nie jest liczbą.


# Demonstracja błędu ValueError

try:
    liczba = int("Python")
except ValueError:
    print("Błąd: nie można zamienić napisu 'Python' na liczbę całkowitą.")
    
liczba_calkowita = int("123")
print(liczba_calkowita)
    

    