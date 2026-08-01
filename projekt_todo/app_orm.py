from sqlalchemy.orm import Session
from sqlalchemy_app.database import get_db
from sqlalchemy_app.models import Zadanie, Tag


def pokaz_zadania(db: Session):
    """Wyświetla listę wszystkich zadań."""
    zadania = db.query(Zadanie).all()

    if not zadania:
        print("Brak zadań na liście.")
        return

    print("\n--- Twoja lista zadań ---")

    for zadanie in zadania:
        status = "✓" if zadanie.zrobione else "✗"
        tagi = ", ".join(tag.nazwa for tag in zadanie.tagi)

        print(f"[{status}] ID: {zadanie.id}, Opis: {zadanie.opis}, Tagi: {tagi}")

    print("------------------------\n")


def dodaj_zadanie(db: Session, opis: str):
    """Dodaje nowe zadanie do bazy."""

    nowe_zadanie = Zadanie(opis=opis)

    db.add(nowe_zadanie)
    db.commit()
    db.refresh(nowe_zadanie)

    return nowe_zadanie


def oznacz_jako_zrobione(db: Session, id_zadania: int):
    """Oznacza zadanie jako zrobione."""

    zadanie = db.query(Zadanie).filter(Zadanie.id == id_zadania).first()

    if zadanie:
        zadanie.zrobione = True
        db.commit()
        print("Zadanie zaktualizowane!")
    else:
        print("Nie znaleziono zadania.")


def usun_zadanie(db: Session, id_zadania: int):
    """Usuwa zadanie z bazy."""

    zadanie = db.query(Zadanie).filter(Zadanie.id == id_zadania).first()

    if zadanie:
        db.delete(zadanie)
        db.commit()
        print("Zadanie usunięte!")
    else:
        print("Nie znaleziono zadania.")


def wyszukaj_zadania(db: Session, fraza: str):
    """Wyszukuje zadania po fragmencie opisu."""

    return (
        db.query(Zadanie)
        .filter(Zadanie.opis.contains(fraza))
        .all()
    )


def pokaz_wyszukane_zadania(db: Session, fraza: str):
    """Wyświetla wyniki wyszukiwania."""

    zadania = wyszukaj_zadania(db, fraza)

    if not zadania:
        print("Nie znaleziono zadań.")
        return

    print("\n--- Wyniki wyszukiwania ---")

    for zadanie in zadania:
        status = "✓" if zadanie.zrobione else "✗"
        tagi = ", ".join(tag.nazwa for tag in zadanie.tagi)

        print(f"[{status}] ID: {zadanie.id}, Opis: {zadanie.opis}, Tagi: {tagi}")

    print("------------------------\n")


def dodaj_tag_do_zadania(db: Session, id_zadania: int, nazwa_tagu: str):
    """Dodaje tag do zadania (many-to-many)."""

    zadanie = db.query(Zadanie).filter(Zadanie.id == id_zadania).first()

    if not zadanie:
        print("Nie znaleziono zadania.")
        return

    tag = db.query(Tag).filter(Tag.nazwa == nazwa_tagu).first()

    if not tag:
        tag = Tag(nazwa=nazwa_tagu)
        db.add(tag)
        db.commit()
        db.refresh(tag)

    if tag not in zadanie.tagi:
        zadanie.tagi.append(tag)
        db.commit()

    print("Dodano tag do zadania!")


# ✅ NOWA FUNKCJA
def edytuj_zadanie(db: Session, id_zadania: int, nowy_opis: str):
    """Edytuje opis zadania."""

    zadanie = db.query(Zadanie).filter(Zadanie.id == id_zadania).first()

    if not zadanie:
        print("Nie znaleziono zadania.")
        return

    zadanie.opis = nowy_opis
    db.commit()

    print("Zadanie zaktualizowane!")


def main():
    db_generator = get_db()
    db_session = next(db_generator)

    while True:
        print("\nMenu (SQLAlchemy):")
        print("1. Pokaż zadania")
        print("2. Dodaj zadanie")
        print("3. Oznacz zadanie jako zrobione")
        print("4. Usuń zadanie")
        print("5. Wyszukaj zadania")
        print("6. Dodaj tag do zadania")
        print("7. Edytuj zadanie")
        print("8. Wyjdź")

        wybor = input("Wybierz opcję: ")

        if wybor == '1':
            pokaz_zadania(db_session)

        elif wybor == '2':
            opis = input("Podaj opis zadania: ")
            dodaj_zadanie(db_session, opis)
            print("Zadanie dodane!")
            
  
        elif wybor == '3':
            try:
                id_zadania = int(input("Podaj ID zadania: "))
                oznacz_jako_zrobione(db_session, id_zadania)
            except ValueError:
                print("Błędne ID.")
                
        
        elif wybor == '4':
            try:
                id_zadania = int(input("Podaj ID zadania: "))
                usun_zadanie(db_session, id_zadania)
            except ValueError:
                print("Błędne ID.")

        elif wybor == '5':
            fraza = input("Podaj frazę: ").strip()
            pokaz_wyszukane_zadania(db_session, fraza)

        elif wybor == '6':
            try:
                id_zadania = int(input("ID zadania: "))
                tag = input("Nazwa tagu: ")
                dodaj_tag_do_zadania(db_session, id_zadania, tag)
            except ValueError:
                print("Błędne ID.")

        elif wybor == '7':
            try:
                id_zadania = int(input("ID zadania: "))
                nowy_opis = input("Nowy opis zadania: ")
                edytuj_zadanie(db_session, id_zadania, nowy_opis)
            except ValueError:
                print("Błędne ID.")

        elif wybor == '8':
            print("Do zobaczenia!")
            db_session.close()
            break

        else:
            print("Nieznana opcja.")


if __name__ == "__main__":
    main()