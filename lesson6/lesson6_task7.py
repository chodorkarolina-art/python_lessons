# 7. Zwracanie wielu wartości: Stwórz funkcję analiza_listy(lista: list[int]) , która
# przyjmuje listę liczb i zwraca krotkę zawierającą trzy wartości: minimum, maksimum i sumę
# elementów z listy.

def analiza_listy(lista: list[int]) -> tuple [int,int,int]:
    return min(lista), max(lista), sum(lista)

print(analiza_listy([4,5,6,10,25,43]))


    
    