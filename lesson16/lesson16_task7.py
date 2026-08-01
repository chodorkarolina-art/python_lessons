# Parser URL: Napisz funkcję parse_url(url: str) -> dict , która przyjmuje jako argument adres URL w formie stringa 
# (np. https://api.example.com:8080/users/search?active=true ) i zwraca słownik zawierający jego części: protocol , domain , port i path .
# Dla podanego przykładu, wynik powinien być: {'protocol': 'https', 'domain': 'api.example.com', 'port': 8080, 'path': '/users/search?active=true'} .
# Obsłuż przypadek, gdy port nie jest podany (dla http domyślny to 80, dla https 443).
# Wskazówka: Użyj metod do manipulacji stringami, takich jak split() czy find() .

def parse_url(url: str) -> dict:
    protocol, rest = url.split("://")
    
    if ":" in rest.split("/")[0]:
        domain_port, path = rest.split("/", 1)
        domain, port = domain_port.split(":")
        port = int(port)
        
    else:
        domain_part, path = rest.split("/", 1)
        domain = domain_part
        path = "/" + path
        port = 80 if protocol == "http" else 443
        
    return {
        "protocol": protocol,
        "domain": domain,
        "port": port, 
        "path": path
    }
    
url = "https://api.example.com:8080/users/search?active=true"
print(parse_url(url))