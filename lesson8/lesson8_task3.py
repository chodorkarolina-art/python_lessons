# Czytanie pliku: Napisz funkcję, która próbuje otworzyć i odczytać plik o podanej nazwie.
# Obsłuż wyjątki FileNotFoundError (gdy pliku nie ma) oraz PermissionError (gdy nie ma uprawnień do odczytu).

def wczytaj_plik():
    sciezka = input("podaj ścieżkę do pliku: ")
    plik = None

    try:
        plik = open(sciezka, mode='r', encoding='utf-8')
        zawartosc = plik.read()
        print(zawartosc)

    except FileNotFoundError:
        print(f"Plik {sciezka} nie istnieje")

    except PermissionError:
        print(f"Brak dostępu do pliku {sciezka}")

    else:
        print("Plik odczytany poprawnie.")

    finally:
        if plik is not None:
            plik.close()
            print("Plik zamknięty.")

wczytaj_plik()

         
        