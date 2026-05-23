# Błąd konwersji: Napisz program, który świadomie spróbuje przekonwertować słowo "Python" na liczbę całkowitą. 
# Uruchom go, zobacz błąd ValueError , a następnie "napraw" program, 
# umieszczając błędną linię w komentarzu i dodając wyjaśnienie, dlaczego kod nie działał.

liczba = int("Python")
# ValueError - python wyświetli informację o błędzie. Funkcja int() potrafi zmieniać tylko cyfry na tekst. 

liczba_całkowita = int("123")
print(liczba_całkowita)