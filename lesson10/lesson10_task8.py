# Stwórz klasę RejestracjaUzytkownika. W konstruktorze init przyjmuj email i haslo.
# Wewnątrz konstruktora dodaj walidację:
# Sprawdź, czy email zawiera znak @ . Jeśli nie, podnieś wyjątek ValueError z odpowiednim komunikatem.
# Sprawdź, czy haslo ma co najmniej 8 znaków. Jeśli nie, podnieś ValueError. 
# Użyj bloku try...except, aby przetestować tworzenie obiektów z poprawnymi i niepoprawnymi danymi.

class RejestracjaUzytkownika:
    def __init__(self, email, haslo:str):
        if '@' not in email:
            raise ValueError("Email musi zawierać znak '@'.")
        if len(haslo) < 8:
            raise ValueError("Hasło musi mieć co najmniej 8 znaków.")
        
        self.email = email
        self.haslo = haslo 

try:
    u1 = RejestracjaUzytkownika("janmail.com", "12345678")
except ValueError as e:
    print(e)

try:
    u2 = RejestracjaUzytkownika("jan@mail.com", "123")
except ValueError as e:
    print(e)

u3 = RejestracjaUzytkownika("jan@mail.com", "bezpiecznehaslo")
print("OK:", u3.email)