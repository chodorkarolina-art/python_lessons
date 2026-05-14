# # Dziennik użytkownika: Napisz program, który w pętli prosi użytkownika o wpisanie jednej linii tekstu. 
# Każda wpisana linia powinna być dopisywana (tryb 'a' ) do pliku
# dziennik.txt . Program kończy działanie, gdy użytkownik wpisze "koniec". 
                
     
def dziennik_uzytkownika():
    while True:
        tekst = input("Wpisz linię (lub 'koniec' by zakończyć): ")
        
        if tekst.lower() == "koniec":
            print("Zakończono zapis do dziennika")
            break
        
        with open("dziennik.txt", "a", encoding="utf-8") as plik:
            plik.write(tekst + "\n")
            
dziennik_uzytkownika()            
        
            
        
        
              