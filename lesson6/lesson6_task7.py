# Łączenie map i filter: Mając listę liczb [-5, 2, 8, -1, 0, 10] , 
# użyj filter dowybrania tylko liczb dodatnich, a następnie map do obliczenia ich kwadratów. 
# Zrób to w jednej linijce.
# filter(lambda x: x > 0, ...) wybiera tylko liczby dodatnie
# map(lambda x: x**2, ...) podnosi każdą do kwadratu

wynik = list(map(lambda x: x**2, filter(lambda x: x > 0, [-5, 2, 8, -1, 0, 10])))
print(wynik)
                 