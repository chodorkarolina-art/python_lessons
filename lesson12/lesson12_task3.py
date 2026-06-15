# Stwórz klasę KalkulatorWalut. Dodaj w niej metodę statyczną (@staticmethod) o nazwie usd_na_pln, 
# która przyjmuje kwotę w dolarach i zwraca ją przeliczoną na złotówki 
# (przyjmij stały kurs, np. 1 USD = 4.0 PLN). Wywołaj tę metodę bez tworzenia obiektu klasy.


class KalkulatorWalut:
    @staticmethod
    def usd_na_pln(usd):
        kurs = 4.0
        return usd * kurs


wynik = KalkulatorWalut.usd_na_pln(140)
print(wynik)