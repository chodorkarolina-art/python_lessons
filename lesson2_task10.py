# 10. Mini-projekt "Formater danych": Napisz program, który poprosi użytkownika o jego imię i nazwisko w jednej linii 
# (np. " jan kowalski "). Program powinien:
# Oczyścić zbędne białe znaki.
# Sprawić, aby każde słowo zaczynało się wielką literą (metoda .title() ).
# Wyświetlić sformatowane dane oraz ich długość.


dane = input("Podaj imię i nazwisko: ")

dane = dane.strip()

dane = dane.title()

print("Sformatowane dane:", dane)
print("Długość:", len(dane))