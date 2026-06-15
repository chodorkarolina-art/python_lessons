# Odczyt konfiguracji: Napisz program, który odczytuje plik config.json z poprzedniego zadania 
# i wyświetla komunikat: Witaj, [uzytkownik]! Twój motyw to [motyw].


import json

with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)
    
print(f"Witaj {config['uzytkownik']}! Twój motyw to {config['motyw']}.")   


