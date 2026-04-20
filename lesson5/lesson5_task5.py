# Wielokrotne powitanie: Napisz funkcję wielokrotne_powitanie(imie: str, ilosc: int) -> None , 
# która wyświetla powitanie f"Cześć, {imie}!" tyle razy, ile wynosi ilosc . 
# Ta funkcja nie powinna niczego zwracać.

def wielokrotne_powitanie (imie: str, ilosc: int) -> None:
    """
imie: str → tekst (np. "ania")
ilosc: int → liczba powtórzeń
-> None → funkcja nic nie zwraca, tylko drukuje

range(3) → daje: 0, 1, 2
_ oznacza: „nie potrzebuję tej zmiennej”
czyli: wykonaj print() tyle razy, ile wynosi ilosc
"""
    for _ in range(ilosc):
        print(f"Cześć, {imie}! ")
    
wielokrotne_powitanie("ania", 3)

imiona = 'ania, kasia, irek, damian'

""" split() → dzieli tekst na listę
enumerate() → dodaje numerowanie """

for i, imie in enumerate(imiona.split(",")):
    wielokrotne_powitanie(imie, i)
    
    