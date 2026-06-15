# Dekorator z argumentem: Stwórz dekorator @powtorz(n) , który przyjmuje argument n 
# i powoduje, że udekorowana funkcja zostanie wykonana n razy.

def powtorz(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator


@powtorz(3)
def wyswietl(*args):
    print(*args)


wyswietl("Hej")

    
         