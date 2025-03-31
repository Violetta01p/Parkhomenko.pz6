try:
products = int(input("Enter quanity of goods: "))
if products <= 0:
   print("Error! incorrect quanity")
elif products > 20:
   print("There is not enough products in stock!")
else:
   print("Your order has been accepted")
except ValueError:
   print("Invaild input! Please enter a number.")
