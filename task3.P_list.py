temps =  [12, 15, 14, 18, 20, 19, 24, 21, 18, 17, 24]
rains = [False, False, True, False, True, False, False, True, True, False, False]

weather_data = [{"temp": t, "rain": r} for t, r in zip(temps,rains)]

print(weather_data)