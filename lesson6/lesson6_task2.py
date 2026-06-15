# Informacje o książce: Stwórz funkcję opis_ksiazki(tytul, autor, rok_wydania=2024- wartości domyślne) . 
# Funkcja powinna zwracać sformatowany string, np. "Książka '[Tytuł]' została napisana przez [Autor] i wydana w roku [Rok wydania]." .
# Przetestuj ją, wywołując z argumentami pozycyjnymi i nazwanymi.

def opis_ksiazki (tytul, autor, rok_wydania=2024):
    return f"Książka '{tytul}' została napisana przez {autor} i wydana w roku {rok_wydania}."

# test z argumentami pozycyjnymi
print(opis_ksiazki("Filary ziemi", "Kena Folleta",  1989))

# test z argumentami nazwanymi
print(opis_ksiazki(tytul="Władca Pierścieni", autor="J.R.R. Tolkien", rok_wydania=1954))
