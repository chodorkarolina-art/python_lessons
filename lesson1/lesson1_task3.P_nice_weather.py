weather_data = [
    {'temp': 12, 'rain': False},
    {'temp': 15, 'rain': False},
    {'temp': 14, 'rain': True},
    {'temp': 18, 'rain': False},
    {'temp': 20, 'rain': True},
    {'temp': 19, 'rain': False},
    {'temp': 24, 'rain': False},
    {'temp': 21, 'rain': True},
    {'temp': 18, 'rain': True},
    {'temp': 17, 'rain': False},
    {'temp': 24, 'rain': False},
]

def is_nice_weather(temp, rain):
    if 15 <= temp <=25 and not rain:
        return True
    else:
        return False
    
nice_days = 0

for day in weather_data:
    if is_nice_weather(day["temp"], day["rain"]):
        nice_days += 1
        
print("liczba ładnych dni:", nice_days)


