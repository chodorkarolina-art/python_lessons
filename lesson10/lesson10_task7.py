# Zaprojektuj hierarchię klas: Instrument -> Strunowy i Dety. Następnie Gitara (dziedziczy po Strunowy) i Trabka (dziedziczy po Dety). 
# Klasa Instrument powinna mieć metodę graj(), która zwraca ogólny komunikat. 
# Każda kolejna klasa w hierarchii powinna nadpisywać tę metodę, dodając coś od siebie i wywołując wersję z klasy nadrzędnej za pomocą super().graj().
# Instrument.graj() -> "Wydaje dźwięk."
# Strunowy.graj() -> "Wydaje dźwięk. [Szarpnięcie struny]"
# Gitara.graj() -> "Wydaje dźwięk. [Szarpnięcie struny] [Akord G-dur]" (challenge)

class Instrument:
    def graj(self):
        raise NotImplementedError
    
class Strunowy(Instrument):
    def graj(self):
        return "Wydaje dźwięk w reakcji na szarpnięcie struny."
    
class Dety(Instrument):
    def graj(self):
        return "Wydaje dźwięk po dmuchnięciu w ustnik."
    
class Gitara(Strunowy):
    def graj(self):
        return super().graj() + " palcem."
    
class Skrzypce(Strunowy):
    def graj(self):
        return (
            super().graj()
            .replace('Wydaje', 'wydają', 1)
            .replace("dźwięk", "dźwięki", 1)
            + " smyczkiem."
           )
    
i = Instrument()
s = Strunowy()
g = Gitara()
s_ = Skrzypce()

for obj in [s, g, s_]:
    print(obj.__class__.__name__, "->", obj.graj())