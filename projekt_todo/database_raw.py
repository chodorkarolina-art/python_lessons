import sqlite3


class TaskManagerRaw:
    def __init__(self, db_name: str = "todo_raw.db"):
        self.db_name = db_name
        self.init_db()

    def _connect(self):
        return sqlite3.connect(self.db_name)

    def init_db(self):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS zadania (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                opis TEXT NOT NULL,
                zrobione BOOLEAN NOT NULL DEFAULT 0 CHECK (zrobione IN (0, 1)),
                priorytet INTEGER DEFAULT 1
            )
            """)
            conn.commit()

    def dodaj_zadanie(self, opis: str, priorytet: int = 1):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO zadania (opis, zrobione, priorytet) VALUES (?, ?, ?)",
                (opis, 0, priorytet)
            )
            conn.commit()

    def pobierz_zadania(self):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, opis, zrobione, priorytet
                FROM zadania
            """)
            return cursor.fetchall()

    def oznacz_jako_zrobione(self, id_zadania: int):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE zadania SET zrobione = 1 WHERE id = ?",
                (id_zadania,)
            )
            conn.commit()
            
    def usun_zadanie(self, id_zadania: int):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM zadania WHERE id = ?",
                (id_zadania,)
            )
            conn.commit()

    def wyszukaj_zadania(self, fraza: str):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, opis, zrobione, priorytet
                FROM zadania
                WHERE opis LIKE ?
            """, (f"%{fraza}%",))
            return cursor.fetchall()
        