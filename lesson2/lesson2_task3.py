#. Analiza stringa: Utwórz zmienną z łańcuchem znaków " Python jest super! " .
# Wykonaj następujące działania i wyświetl wynik każdego kroku: 
# Usuń zbędne białe znaki na początku i na końcu. 
# Przekształć cały ciąg na małe litery. 
# Zamień słowo "super" na "świetny". 
# Wyświetl na ekranie znak pod indeksem 4 .

tekst = " Python jest super! "

tekst = tekst.strip()
print(tekst)

tekst = tekst.lower()
print(tekst)

tekst = tekst.replace("super", "świetny")
print(tekst)

print(tekst[4])