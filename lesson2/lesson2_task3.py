# Praca z f-stringami: Poproś użytkownika o jego imię i rok urodzenia. 
# Oblicz jego przybliżony wiek i wyświetl komunikat w formacie: 
# "Cześć, [Imię]! W 2025 roku będziesz mieć około [Wiek] lat."

imię = input("Podaj swoje imię: ")
rok_urodzenia = int(input("Podaj swój rok urodzenia: "))

wiek = 2025 - rok_urodzenia

print(f"Cześć, {imię}! W roku 2025 będziesz mieć, {wiek} lat ")


