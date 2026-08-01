#  Klasa Request : Napisz klasę w Pythonie o nazwie HttpRequest .
# Konstruktor __init__ powinien przyjmować method , target oraz opcjonalnie headers (słownik) i body (string).
# Dodaj metodę display() , która będzie drukować sformatowane żądanie na konsoli w czytelnej formie, np.:
# --- HTTP Request ---
# Method: GET
# Target: /index.html
# Headers:
# Host: example.com
# User-Agent: PythonClient/1.0
# Body:
# (empty)
# --------------------
# Przetestuj klasę, tworząc obiekt dla żądania POST z przykładowymi danymi.

class HttpRequest:
    def __init__(self, method, target, headers: dict = None, body: str = ""):
        self.method = method
        self.target = target
        self.headers = headers if headers else {}
        self.body = body
        
    def display(self):
        print("--- HTTP Request ---")
        print(f"Method : {self.method}")
        print(f"Target: {self.target}")
        print("Headers: ")
        for key, value in self.headers.items():
            print(f"{key}: {value}")
            
        print("Body:")
        if self.body:
            print(self.body)
        else:
            print("(empty)")
            
        print("--------------------")
        
# TEST

request = HttpRequest(
    method="POST",
    target="/index.html",
    headers={
        "Host": "example.com",
        "User-Agent": "PythonClient/1.0"    
    },
    body="Przykladowe dane"
)       

request.display()
        
        