# Stwórz klasę Film, która przy tworzeniu obiektu będzie przyjmować tytul, rezyser i rok_produkcji. 
# Dodaj metodę informacje(), która będzie zwracać string z pełnymi informacjami o filmie w formacie: "Tytuł" (rok_produkcji), reżyseria: Reżyser. 
# Stwórz dwanobiekty tej klasy i wydrukuj informacje o nich.

class Film:
    
    def __init__(self, tytuł, rezyser, rok_produkcji):
        self.tytuł = tytuł
        self.rezyser = rezyser
        self.rok_produkcji = rok_produkcji

    def informacje(self):
        return f'"{self.tytuł}" ({self.rok_produkcji}), reżyseria: {self.rezyser}'
    
film1 = Film("Gwiezdne wojny: Nowa nadzieja", "George Lucas", 1977)
film2 = Film("Monty Python i Święty Graal", "Terry Gilliam i Terry Jones", 1975)

print(film1.informacje())
print(film2.informacje())
