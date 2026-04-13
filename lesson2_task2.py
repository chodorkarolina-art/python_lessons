# Kalkulator BMI: Napisz program, który zapyta użytkownika o 
# jego wagę w kilogramach
# i wzrost w metrach.
# Oblicz i wyświetl wskaźnik masy ciała (BMI) według wzoru: BMI = waga / (wzrost * wzrost).

waga = float(input("Podaj swoją wagę w kilogramach: "))
wzrost = float(input("Podaj swój wzrost w metrach: "))
      
if wzrost >=0 and waga >=0 :            
    bmi = waga / (wzrost **2)        
    print("Twoje BMI: ", round(bmi, 2))


    if bmi < 18.5:
        print("Niedowaga")
    elif bmi < 25:    
        print("Waga prawidłowa")
    elif bmi < 30:
        print("Nadwaga")
    else:
        print("Otyłość")   

else :
     print("Waga musi być większy od 0!")     
    
print(bmi)
