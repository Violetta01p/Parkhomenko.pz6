try:
   temp = int(input("Enter temperature: "))
   if temp < 16:
       print("Low temperature. Turn on the heater")
   elif temp > 28:
       print("High temperature. Tur on the air conditioner")
   elif 18 <= temp <= 28 :
       print("Temperture is normal")
except ValueError:
   print("Invaild input! Please enter a number.")
