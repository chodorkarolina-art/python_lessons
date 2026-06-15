# Konwersja na wielkie litery: Użyj funkcji map() , aby przekształcić listę imion 
# imiona =["anna", "piotr", "kasia"] w listę imion pisanych wielką literą.

imiona = ['anna', "piotr", "kasia"]
wielkie_litery = list(map(str.upper, imiona))
""" map(str.upper, imiona) stosuje metodę upper() do każdego elementu listy
    list(...) zamienia wynik na listę
    map() to wbudowana funkcja w Pythonie, 
    która pozwala zastosować jakąś funkcję do każdego elementu iterowalnego obiektu 
    (np. listy, krotki) — bez pisania pętli for
"""
print(wielkie_litery)