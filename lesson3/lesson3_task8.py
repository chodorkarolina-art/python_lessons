# Identyfikator po zmianie: Utwórz zmienną x = 10 . Wyświetl jej id() . 
# Następnie przypisz do x nową wartość x = x + 1 . 
# Ponownie wyświetl id() . Czy identyfikator się zmienił? Dlaczego? Odpowiedz w komentarzu.

x = 10
print(f"id(x) = {id(x)}")
x += 1
print(f"id(x) = {id(x)}")

# Dzieje się tak, ponieważ w Pythonie liczby całkowite (int) są niemutowalne.
# Gdy wykonujemy x = x + 1, nie modyfikujemy istniejącej liczby 10,
# tylko tworzymy nowy obiekt (11) i przypisujemy go do zmiennej x.
# Dlatego x wskazuje już na inny obiekt w pamięci, czyli ma inne id().