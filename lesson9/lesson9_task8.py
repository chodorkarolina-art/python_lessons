# Wyszukiwarka logów: Wyobraź sobie, że masz duży plik log.txt . Napisz program, który
# pyta użytkownika o szukane słowo (np. "ERROR") i zapisuje wszystkie 
# linie zawierające to słowo do nowego pliku wyniki_wyszukiwania.txt .

def wyszukiwarka_logow():
    szukane_slowo = input("Podaj słowo do wyszukania (np. ERROR): ")

    try:
        with open("log.txt", "r", encoding="utf-8") as plik_we:
            with open("wyniki_wyszukiwania.txt", "w", encoding="utf-8") as plik_wy:

                for linia in plik_we:
                    if szukane_slowo in linia:
                        plik_wy.write(linia)

        print("Zakończono wyszukiwanie. Wyniki zapisane.")

    except FileNotFoundError:
        print("Plik log.txt nie istnieje.")


wyszukiwarka_logow()