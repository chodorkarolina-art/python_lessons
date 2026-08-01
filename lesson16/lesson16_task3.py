# Utwórz w Pythonie słownik, który będzie reprezentował żądanie GET w celu pobrania listy wszystkich artykułów z adresu /api/articles . 
# W nagłówkach dodaj klucz Host z wartością my-blog.com .

zadanie_get = {
    "method": "GET", 
    "path": "/api/articles",
    "headers" : {
        "Host": "my-blog.com"
     }
}

print(zadanie_get)   
