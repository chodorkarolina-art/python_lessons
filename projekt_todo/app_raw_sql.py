from database_raw import TaskManagerRaw


class App:
    def __init__(self):
        self.db = TaskManagerRaw()

    def pokaz_zadania(self):
        zadania = self.db.pobierz_zadania()

        if not zadania:
            print("Brak zadań na liście.")
            return

        print("\n--- Twoja lista zadań ---")

        for id_zadania, opis, zrobione, priorytet in zadania:
            status = "✓" if zrobione else "✗"
            print(f"[{status}] ID: {id_zadania}, Opis: {opis}, Priorytet: {priorytet}")

        print("------------------------\n")

    def pokaz_wyszukane(self, fraza: str):
        zadania = self.db.wyszukaj_zadania(fraza)

        if not zadania:
            print("Nie znaleziono zadań.")
            return

        print("\n--- Wyniki wyszukiwania ---")

        for id_zadania, opis, zrobione, priorytet in zadania:
            status = "✓" if zrobione else "✗"
            print(f"[{status}] ID: {id_zadania}, Opis: {opis}, Priorytet: {priorytet}")

        print("------------------------\n")

    def run(self):
        while True:
            print("Menu:")
            print("1. Pokaż zadania")
            print("2. Dodaj zadanie")
            print("3. Oznacz jako zrobione")
            print("4. Usuń zadanie")
            print("5. Wyszukaj zadania")
            print("6. Wyjdź")

            wybor = input("Wybierz opcję: ")

            if wybor == "1":
                self.pokaz_zadania()

            elif wybor == "2":
                opis = input("Podaj opis zadania: ")
                self.db.dodaj_zadanie(opis)
                print("Zadanie dodane!")

            elif wybor == "3":
                try:
                    id_zad = int(input("Podaj ID: "))
                    self.db.oznacz_jako_zrobione(id_zad)
                    print("Zaktualizowano!")
                except ValueError:
                    print("Błędne ID")
                    

            elif wybor == "4":
                try:
                    id_zad = int(input("Podaj ID: "))
                    self.db.usun_zadanie(id_zad)
                    print("Usunięto!")
                except ValueError:
                    print("Błędne ID")

            elif wybor == "5":
                fraza = input("Szukaj: ")
                self.pokaz_wyszukane(fraza)

            elif wybor == "6":
                print("Do zobaczenia!")
                break

            else:
                print("Nieznana opcja")


if __name__ == "__main__":
    App().run()