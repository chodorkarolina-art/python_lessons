# Stwórz klasę danych (@dataclass) o nazwie Film, która będzie przechowywać tytuł (string),
# reżysera (string) i rok_produkcji (integer). Utwórz dwie instancje tej klasy i wyświetl je.

from dataclasses import dataclass
        
@ dataclass
class Film:
    tytul: str
    rezyseria: str
    rok_produkcji: int
    
film1 = Film("Gwiezdne Wojny", "George Lucas", 1977)
film2 = Film("Avatar", "James Cameron", 2009)

print(film1)
print(film2)
           