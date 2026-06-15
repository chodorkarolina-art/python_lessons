# Stwórz klasę Telewizor. Użyj enkapsulacji, aby ukryć następujące atrybuty: kanal (domyślnie 1), glosnosc (domyślnie 10), __wlaczony (domyślnie False).
# Stwórz publiczne metody do zarządzania telewizorem: wlacz() i wylacz() zmien_kanal(numer) : kanał można zmienić tylko, gdy TV jest włączony.
# glosniej() i ciszej() : głośność można regulować w zakresie 0-100 i tylko, gdy TV jest włączony.
# info(): wyświetla aktualny stan (włączony/wyłączony, kanał, głośność). 
# Przetestuj, czy nie da się zmienić kanału na wyłączonym telewizorze lub ustawić głośności powyżej 100.

class Telewizor:
    ZAKRES_GLOSNOSCI = (0,100)
    
    def __init__(self) -> None:
        self.__kanal = 1
        self.__glosnosc = 10
        self.__wlaczony = False 
        
        
    def glosniej(self, wartosc:int):
        print('podgłaśniamy o wartość', wartosc)
        self.__zmien_glosnosc(wartosc)
    
    def ciszej(self, wartosc:int):
        print('ściszamy o wartość', wartosc)
        self.__zmien_glosnosc(-wartosc)
    
    def on_off(self):
        self.__wlaczony = not self.__wlaczony 
        
    def wlacz(self):
        self.__wlaczony = True
    
    def wylacz(self):
        self.__wlaczony = False
        
    def zmien_kanal(self, nowy_kanal):
        if not self.__wlaczony:
            raise ValueError("Telewizor musi być włączony, aby zmienić kanał.")
        self.__kanal = nowy_kanal
    
    def info(self):
        print(f'[{"ON" if self.__wlaczony else "OFF"}][{self.__glosnosc=}][{self.__kanal=}]')
       
    def __zmien_glosnosc(self, wartosc: int):
        if not self.__wlaczony:
            raise ValueError("Telewizor musi być włączony, aby zmienić glośność.")
        if not isinstance(wartosc, int):
            raise TypeError
        
        m0, m1 = self.ZAKRES_GLOSNOSCI
        
        if not (m0 <= self.__glosnosc + wartosc <= m1):
            raise ValueError("Przekroczono zakres głośności!")
     
        self.__glosnosc += wartosc
        
             
t = Telewizor()

try:
    t.glosniej(10)
except ValueError as e:
    print(e)

t.wlacz()
t.glosniej(10)
t.ciszej(5)
t.zmien_kanal(5)
t.info()
        