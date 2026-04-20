#Tworzenie profilu: Napisz funkcję stworz_profil(imie, **dane_dodatkowe) , 
# która przyjmuje imię oraz dowolną liczbę nazwanych argumentów (np. wiek=30 , miasto="Warszawa" ). 
# Funkcja powinna zwrócić słownik z profilem użytkownika, gdzie
# klucz 'imie' jest obowiązkowy, a reszta danych jest pobierana z **dane_dodatkowe .

def stworz_profil(imie, **dane_dodatkowe):
    """ *args → dowolne argumenty pozycyjne (lista)
    **kwargs → dowolne argumenty nazwane (słownik)
    update() → dodaje słownik do słownika"""

    profil={"Imię": imie}
    profil.update(dane_dodatkowe)
    return profil

profil = stworz_profil("Ania", wiek=30, miasto="Warszawa")
print(profil)
    