# Stwórz metaklasę MetaWalidujMetody, która podczas tworzenia nowej klasy sprawdza, 
# czy wszystkie jej metody (poza metodami "magicznymi", czyli zaczynającymi się od __) mają docstring. 
# Jeśli któraś metoda go nie ma, metaklasa powinna podnieść TypeError z informacją, która metoda wymaga dokumentacji. 
# Przetestuj ją, tworząc klasę z poprawnie i niepoprawnie udokumentowanymi metodami.

# Metaklasa sprawdzająca docstringi metod

class MetaWalidujMetody(type):

    def __new__(cls, nazwa, bazy, atrybuty):

        for nazwa_metody, wartosc in atrybuty.items():

            # pomijamy metody magiczne
            if nazwa_metody.startswith("__"):
                continue

            # sprawdzamy tylko metody
            if callable(wartosc):

                # brak docstringa (None lub "")
                if not wartosc.__doc__:
                    raise TypeError(
                        f"Metoda '{nazwa_metody}' wymaga docstringa."
                    )

        return super().__new__(cls, nazwa, bazy, atrybuty)



# Klasa poprawna

class Samochod(metaclass=MetaWalidujMetody):

    def uruchom(self):
        """Uruchom samochód."""
        print("Samochód uruchomiony.")

    def zatrzymaj(self):
        """Zatrzymaj samochód."""
        print("Samochód zatrzymany.")


print("Klasa Samochod została utworzona poprawnie.")



# Klasa niepoprawna

try:

    class Telefon(metaclass=MetaWalidujMetody):

        def dzwon(self):
            """Wykonuje połączenie."""

        def wyslij_sms(self):
            print("SMS wysłany.")

except TypeError as e:
    print("Błąd:", e)
                    