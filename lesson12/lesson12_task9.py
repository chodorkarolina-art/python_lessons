# Stwórz klasę KontoBankowe za pomocą @dataclass, która ma atrybut _saldo (prywatne).
# Stwórz właściwość ( @property ) saldo , która tylko odczytuje wartość _saldo .
# Stwórz metodę wplac(kwota) , która dodaje kwotę do salda. Metoda powinna podnosić
# ValueError , jeśli kwota jest ujemna.
# Stwórz metodę wyplac(kwota) , która odejmuje kwotę od salda. Metoda powinna
# podnosić ValueError , jeśli kwota do wypłaty jest ujemna, oraz własny wyjątek
# BrakSrodkowError , jeśli saldo jest niewystarczające.
# Przetestuj działanie klasy, obsługując wszystkie możliwe wyjątki.

from dataclasses import dataclass

class BrakSrodkowError(Exception):
    pass

@dataclass
class KontoBankowe:
    _saldo: float
    
    @property
    def saldo(self):
        return self._saldo
    
    def wplac(self, kwota):
        if kwota < 0:
            raise ValueError("Kwota wpłaty nie może być ujemna.")
        
        self._saldo += kwota
        
    def wyplac(self, kwota):
        if kwota < 0:
            raise ValueError("Kwota wypłaty nie może być ujemna.")
        if kwota > self._saldo:
            raise BrakSrodkowError ("Brak wystarczających środków.")
        
        self._saldo -= kwota
        
konto = KontoBankowe(5600)

print("Początkowe saldo:", konto.saldo)

try:
    konto.wplac(400)
    print("Saldo po wpłacie:", konto.saldo)
except ValueError as e:
    print("Błąd wpłaty:", e)
    
try:
    konto.wplac(-300)
except ValueError as e:
    print("Błąd wpłaty:", e)
    

try:
    konto.wyplac(6200)
except (ValueError, BrakSrodkowError) as e:
    print("Błąd wypłaty:", e)
    
try:
    konto.wyplac(-3000)
except (ValueError, BrakSrodkowError) as e:
    print("Błąd wypłaty:", e)    
        
            