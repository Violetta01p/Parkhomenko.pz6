password = input("Enter your password: ")
if len(password) < 8:
   print("Password is too short!")
elif password == "password" or password == "12345678":
   print("Password is too simple!")
else:
   print("Access granted!")
