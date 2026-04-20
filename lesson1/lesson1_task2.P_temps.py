temps =  [12, 15, 14, 18, 20, 19, 24, 21, 18, 17, 24]

def desc_temp(temp):

    if temp >= 20:
        return("warm")
    elif temp <= 10:
        return("cold")
    else:
       return("med_warm")
   
for temp in temps :
    print(desc_temp(temp))  