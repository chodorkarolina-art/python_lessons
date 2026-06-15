# Mini-projekt: Lista zadań: Stwórz prostą aplikację do zarządzania listą zadań. 
# Program powinien:
# Przy starcie próbować wczytać zadania z pliku zadania.json .
# Pozwalać użytkownikowi dodać nowe zadanie.
# Pozwalać wyświetlić wszystkie zadania.
# Przy zamknięciu (lub na polecenie) zapisywać aktualną listę zadań do pliku zadania.json

import json

try:
    with open("zadania.json", 'r', encoding="utf-8") as f:
        zadania = json.load(f)
except:
    zadania = [] 

while True:
    print("\n===Lista zadań===")
    print("\n1. Dodaj")    
    print("\n2. Pokaż")
    print("\n3. Wyjdź")

    wybor = input("Wybierz zadanie: ")  

    if wybor == "1":
        nowe = input("Podaj zadanie: ")
        zadania.append(nowe)
        print("Zadanie dodane! ")
    
    elif wybor == "2":
        if len(zadania) == 0:
            print("Brak zadań.")  
        else:
            print("\nTwoja lista zadań:")
    
            for i, z in enumerate(zadania, 1):
                print(f"{i}) {z}")
        
    elif wybor == "3":
        with open("zadania.json", 'w', encoding="utf-8") as f:
            json.dump(zadania, f, ensure_ascii=False,indent=4)   
            
        print("Zadania zapisane. Koniec programu.")    
        break         
        
    else: 
        print("Niepoprawny wybór!")
    
        
            