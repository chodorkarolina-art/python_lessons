# Kontekstowy menedżer with : Pokaż, jak instrukcja with open(...) as f: upraszcza kod z zadania 3, 
# eliminując potrzebę jawnego używania bloku finally do zamykania pliku.

# def wczytaj_plik():
#     sciezka = input("podaj sciezkę do pliku: ")
#     try:
#         plik = open(sciezka, mode='r')
#     except FileNotFoundError:
#        print(f"brak dostepu do pliku {sciezka} nie istnieje") 
#     except PermissionError:
#         print(f"brak dostepu do pliku {sciezka}")
#     else: 
#         plik.close()    
# wczytaj_plik()            
    
    
def wczytaj_plik():
    sciezka = input("podaj sciezkę do pliku: ")
    try:
        with open(sciezka, mode='r', encoding='utf-8') as plik:
            zawartosc = plik.read()
            print(zawartosc)
    except FileNotFoundError:
        print(f"brak dostepu do pliku {sciezka} nie istnieje") 
    except PermissionError:
        print(f"brak dostepu do pliku {sciezka}")
    else:
        print("Plik odczytany poprawnie.")
        
wczytaj_plik()