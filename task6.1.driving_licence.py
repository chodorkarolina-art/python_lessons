prawo_jazdy = input("Czy masz prawo jazdy?(tak/nie): ")
age = int(input("Ile masz lat? "))

wynik = (prawo_jazdy == "tak") and (age >=18)

print(wynik)