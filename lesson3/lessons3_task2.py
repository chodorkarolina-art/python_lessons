# Porównanie is vs == : Utwórz dwie różne listy lista1 = [1, 1] i lista2 = [1, 1] .
# Sprawdź wynik porównania lista1 is lista2 oraz lista1 == lista2 . 
# Wyświetl wyniki i w komentarzu wyjaśnij, dlaczego są różne.

lista1 = [1, 1]
lista2 = [1, 1]

print(lista1 is lista2)

print(lista1 == lista2)

# lista1 == lista2 - True, ponieważ operator == porównuje zawartość obiektów. 
# Obie listy mają takie same elementy [1, 1].
# lista1 is lista2 - False, ponieważ operator is sprawdza, 
# czy obie zmienne wskazują na ten sam obiekt w pamięci. 
# Tutaj zostały utworzone dwie różne listy, więc są to dwa różne obiekty.