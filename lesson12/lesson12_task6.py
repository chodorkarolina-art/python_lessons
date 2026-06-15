# Stwórz własny wyjątek InvalidPasswordError. Następnie napisz funkcję ustaw_haslo(haslo),
# która sprawdza, czy hasło ma co najmniej 8 znaków. 
# Jeśli nie, funkcja powinna podnieść (raise) wyjątek InvalidPasswordError z odpowiednim komunikatem. 
# Napisz kod, który testuje tę funkcję w bloku try...except.

class InvalidPasswordError(Exception):
    pass

def ustaw_haslo(haslo):
    if len(haslo) < 8:
        raise InvalidPasswordError ("Hasło musi mieć 8 znaków.")
    
    print("Hasło zostało usawione poprawnie.")
    
try:
    haslo = input("Podaj haslo: ")
    ustaw_haslo(haslo)
    
except InvalidPasswordError as e:
    print("Błąd:", e)