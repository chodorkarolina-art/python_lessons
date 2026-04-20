# Mini-projekt: Walidator hasła: Stwórz funkcję sprawdz_haslo(haslo: str) -> bool .
# Funkcja powinna sprawdzać, czy hasło spełnia następujące warunki i zwracać True lub False :
# Ma co najmniej 8 znaków.
# Zawiera co najmniej jedną wielką literę.
# Zawiera co najmniej jedną cyfrę. Napisz do niej pełną dokumentację (docstring i adnotacje).
# Najważniejsze rzeczy do zapamiętania:
# any(...)  sprawdza, czy chociaż jeden znak spełnia warunek
# for znak in haslo → przechodzi po literach
# isupper() wielka litera
# isdigit() cyfra
# return False kończy funkcję od razu


def sprawdz_haslo(haslo: str) -> bool:
    """
Sprawdza, czy haslo spełnia podstawowe warunki bezpieczeństwa: 

warunki:
- co najmniej 8 znaków
- jedna wielka litera
- co najmniej jedną cyfrę

Parametry:
haslo (str) : haslo do sprawdzenia

zwraca:
bool True jeśli haslo spełnia warunki, False jeśli nie
"""
    if len(haslo) < 8:
        return False
    
    if not any(znak.isupper() for znak in haslo):
        return False
    
    if not any(znak.isdigit() for znak in haslo):
        return False
    
    return True
        
print(sprawdz_haslo("Karolina!%1"))
