# Walidacja hasła v2: Rozbuduj funkcję do walidacji hasła. 
# Powinna ona zwracać listę wszystkich błędów walidacji, zamiast rzucać wyjątkiem po pierwszym napotkanym problemie. 
# Jeśli lista błędów nie jest pusta, rzuć własnym wyjątkiem BladWalidacjiError , przekazując do niego tę listę.

# Exception - pudełko na błąd 
# self.bledy - lista rzeczy w środku (Twoje dane (lista błędów))
# super().__init__() - etykieta na pudełku (tekst błędu)

#Tworzysz pustą listę: err_lst = [] Sprawdzam hasło krok po kroku. Każdy problem dodajesz do listy. Na końcu: jeśli lista nie jest pusta - błąd

class BladWalidacjiError(Exception):
    def __init__(self, bledy):
        self.bledy = bledy
        super().__init__("Błędy walidacji")
        
    

def walidacja_hasla(haslo: str):
    err_lst = []
    
    if len(haslo) < 8:
        err_lst.append("Hasło jest za krótkie, wymagane min. 8 znaków")
    if not any(znak.isupper() for znak in haslo):
        err_lst.append("Brak dużej litery")
    if not any(znak.isdigit() for znak in haslo):
        err_lst.append("Brak cyfry w hasle")
    if not any(not znak.isalnum() for znak in haslo):
        err_lst.append("Brak znaku specjalnego")
    if err_lst:
        raise BladWalidacjiError(err_lst)
    
try:
    walidacja_hasla("abc")
except BladWalidacjiError as e:
    print(e)           # Błędy walidacji
    print(e.bledy)     # lista błędów
        
    