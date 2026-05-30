height = input("Podaj swój wzrost w cm: ")
guardian = input("Czy masz opiekuna? (tak/nie): ").lower()

can_enter = (height >= "120" and guardian == "tak") or height >= "160"

print(f"Możesz wejść na karuzelę: {can_enter}")