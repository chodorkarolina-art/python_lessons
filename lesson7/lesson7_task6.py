# Bezpieczne pobieranie ze słownika: Napisz funkcję pobierz_wartosc(slownik, klucz) ,
# która bezpiecznie zwraca wartość dla danego klucza. Jeśli klucza nie ma, funkcja nie powinna rzucać błędu, 
# tylko zwracać None . Zrób to bez użycia try...except
# (wskazówka: metoda .get() ). Następnie napisz drugą wersję z użyciem try...except KeyError .

dict_ = {'a':1,
         'b':2}
# wersja 1
def pobierz_wartosc(dict_: dict, key): 
    return dict_.get(key)

# wersja 2
def pobierz_wartosc_wtry(dict_: dict, key):
    try:
        return dict_[key]
    except KeyError:
        return None


print(pobierz_wartosc(dict_, 'a'))   # 1
print(pobierz_wartosc(dict_, 'x'))   # None

print(pobierz_wartosc_wtry(dict_, 'b'))  # 2
print(pobierz_wartosc_wtry(dict_, 'y'))  # None
