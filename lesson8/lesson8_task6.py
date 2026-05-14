# Tworzenie struktury folderów: Użyj modułu pathlib , aby napisać skrypt, 
# który tworzy strukturę folderów: Projekt/src , Projekt/data , Projekt/docs .

# Path("Projekt") = punkt startowy
# / "src" = dokładanie kolejnego folderu
# / = łączenie ścieżek (nie dzielenie!)
# mkdir() = tworzenie folderu
# parents=True = twórz też nadrzędne foldery
# exist_ok=True = nie krzycz, jeśli już istnieje

from pathlib import Path

base = Path("Projekt")

(base / "src").mkdir(parents=True, exist_ok=True) 
(base / "data").mkdir(parents=True, exist_ok=True) 
(base / "docs").mkdir(parents=True, exist_ok=True) 

print("Struktura foderów została utworzona")