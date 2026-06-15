# Stwórz klasę Uzytkownik z atrybutem _wiek. Użyj dekoratora @property, aby stworzyć właściwość wiek. 
# Getter powinien zwracać wiek, a setter powinien sprawdzać, czy podany wiek jest w zakresie od 0 do 120.
# Jeśli nie jest, powinien wyświetlić komunikat błędu i nie zmieniać wartości.

class Uzytkownik:
    def __init__(self, wiek):
        self.wiek = wiek

    @property
    def wiek(self):
        return self._wiek

    @wiek.setter
    def wiek(self, nowy_wiek):
        if 0 <= nowy_wiek <= 120:
            self._wiek = nowy_wiek
        else:
            print("Błąd: wiek musi być w zakresie od 0 do 120.")
            
u = Uzytkownik(43)
print(u.wiek)

u.wiek = 130
print(u.wiek)

u.wiek = 67
print(u.wiek)

