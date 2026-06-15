# Iloczyn elementów: Użyj funkcji reduce() , aby obliczyć iloczyn (wynik mnożenia)
# reduce() robi coś takiego:
# bierze 2 elementy
# łączy je w jeden
# bierze kolejny
# znowu łączy
# aż zostanie jedna wartość
# wszystkich liczb w liście [1, 2, 3, 4, 5]

from functools import reduce

liczby = [1,2,3,4,5]
iloczyn = reduce(lambda x, y: x * y, liczby)
print(iloczyn)
