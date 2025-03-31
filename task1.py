try:
age = int(input("Enter your age: "))
if age < 18:
   print("Access denied")
else:
   print("Access allowed")
except ValueError:
   print("Invaild input! Please enter a number.")
