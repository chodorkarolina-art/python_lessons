# Zdefiniuj klasę Produkt z konstruktorem init przyjmującym nazwa, cena i kategoria. 
# Stwórz obiekt tej klasy, a następnie wydrukuj każdy z jego atrybutów w osobnej linii.


class Produkt:
    def __init__(self, nazwa, cena, kategoria):
        self.nazwa = nazwa
        self.cena = cena
        self.kategoria = kategoria 
        
produkt1 = Produkt("Laptop", 9000, "Elektornika")   

print(produkt1.nazwa)
print(produkt1.cena)
print(produkt1.kategoria)    
    
    