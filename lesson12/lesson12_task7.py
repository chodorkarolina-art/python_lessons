# Stwórz klasę Data z atrybutami dzien, miesiac, rok. Dodaj metodę klasy (@classmethod) o nazwie ze_stringa, 
# która przyjmuje datę w formacie "DD-MM-RRRR" (np. "25-12-2023") 
# i tworzy na jej podstawie obiekt klasy Data. Pamiętaj o konwersji typów na int.

class Data:
    def __init__(self, dzien, miesiac, rok):
        self.dzien = dzien
        self.miesiac = miesiac
        self.rok = rok
        
    @classmethod
    def ze_stringa(cls, data_string):
        dzien, miesiac, rok = data_string.split("-")
        
        return cls(int(dzien), int(miesiac), int(rok))
    
data1 = Data.ze_stringa("25-12-2023")

print(data1.dzien)
print(data1.miesiac)
print(data1.rok)