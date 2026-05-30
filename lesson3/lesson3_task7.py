# Obliczanie wieku psa: Przyjmuje się, że pierwszy rok życia psa to 15 ludzkich lat,  drugi to 9, a każdy kolejny to 5.
# Napisz program, który pyta o wiek psa w latach, 
# a następnie oblicza i wyświetla jego wiek w "ludzkich" latach.

wiek_psa = int(input("Podaj wiek pas: "))

if wiek_psa == 1:
    print(f" Pies ma {15} ludzkich lat")
elif wiek_psa ==2:
    print(f"Pies ma {15 + 9} ludzkich lat")
else:
    print(f"Pies ma", 15 + 9 + (wiek_psa - 2) * 5, "ludzkich lat")
    
