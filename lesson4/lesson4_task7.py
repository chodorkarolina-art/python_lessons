# Wyszukiwarka w liście: Stwórz listę imion: imiona = ["Anna", "Jan", "Piotr","Kasia"]
# Poproś użytkownika o podanie imienia do wyszukania. 
# Użyj pętli for z instrukcją break oraz blokiem else , aby: 
# Jeśli imię zostanie znalezione, wyświetlić "Znaleziono!" i przerwać pętlę.
# Jeśli pętla zakończy się bez znalezienia imienia, wyświetlić "Nie znaleziono imienia naliście."

imiona = ["Anna", "Jan", "Piotr", "Kasia"]

wyszukiwanie = input("Podaj imię do wyszukania: ")

for imie in imiona:
    if imie == wyszukiwanie:
        print("Znaleziono!")
        break
else:
    print("Nie znaleziono imienia na liście.")