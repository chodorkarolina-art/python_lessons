# Konfiguracja w JSON: Stwórz słownik Pythona z ustawieniami aplikacji, 
# np. konfiguracja = {"uzytkownik": "admin", "motyw": "ciemny", "rozdzielczosc": [1920, 1080]} . 
# Zapisz ten słownik do pliku config.json z wcięciami i poprawnym kodowaniem polskich znaków.

# tworzy słownik config
# otwiera plik config.json w trybie zapisu
# zapisuje dane jako JSON
# używa indent=4 (czytelne formatowanie)
# używa ensure_ascii=False (polskie znaki OK)
# używa poprawnego utf-8

import json

config = {"uzytkownik": "admin", "motyw": "ciemny", "rozdzielczosc": [1920, 1080]}

with open("config.json", "w", encoding="utf-8") as f:
    json.dump(config, f, indent=4, ensure_ascii=False)
   
    