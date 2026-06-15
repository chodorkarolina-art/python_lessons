# Prawda czy fałsz?: Napisz program, który prosi użytkownika o wpisanie dowolnego tekstu.
# Następnie, używając konwersji na bool , sprawdź, czy wpisany tekst jest 
# "prawdziwy" (niepusty) i wyświetl odpowiedni komunikat.

print("Wpisz dowolny tekst: ", end="")
tekst = input()

if bool(tekst):
    print("Wpisałaś niepusty tekst - wartość True")
else:
    print("Wpisałeś pusty tekst - wartość False")
    
        
