# Prawda czy fałsz?: Napisz program, który prosi użytkownika o wpisanie dowolnego tekstu.
# Następnie, używając konwersji na bool , sprawdź, czy wpisany tekst jest 
# "prawdziwy" (niepusty) i wyświetl odpowiedni komunikat.

tekst = input("Wpisz dowolny tekst:")

if bool(tekst):
    print("Wpisałaś niepusty tekt - wartość True")
else:
    print("Wpisałeś pusty tekta - wartość False")
    
        
