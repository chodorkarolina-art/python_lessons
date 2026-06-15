# Wielokrotne powitanie: Napisz funkcję wielokrotne_powitanie(imie: str, ilosc: int) -> None , 
# która wyświetla powitanie f"Cześć, {imie}!" tyle razy, ile wynosi ilosc . 
# Ta funkcja nie powinna niczego zwracać.

def wielokrotne_powitanie (imie: str, ilosc: int) -> None:
    """
    Funkcja wyświetla powitanie tyle razy, ile wynosi ilosc.
    Nie zwraca żadnej wartości.
    """
    for _ in range(ilosc):
        print(f"Cześć, {imie}! ")
    
wielokrotne_powitanie("ania", 3)

    