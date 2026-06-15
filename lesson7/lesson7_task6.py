# Licznik wywołań: Stwórz domknięcie (closure). Napisz funkcję stworz_licznik() , która zwraca funkcję. 
# Każde wywołanie zwróconej funkcji powinno zwiększać wewnętrzny licznik 
# i zwracać jego aktualną wartość
# nonlocal oznacza: „używaj zmiennej z funkcji zewnętrznej”
# Dlaczego to jest closure? Bo: funkcja zwiększ_licznik pamięta licznik nawet po zakończeniu stworz_licznik()

def stworz_licznik():
    licznik = 0
    
    def zwieksz_licznik():
        nonlocal licznik
        licznik +=1
        return licznik
    return zwieksz_licznik
