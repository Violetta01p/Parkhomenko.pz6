try:
   sum = int(input("Enter the top-up amount: "))
   if  sum < 10:
       print("Minimum top-up amount 10 uah")
   elif sum > 3000:
       print("The top-up amount is too large!")
   else:
       print("Topp up for the amound of :" , sum, "uah completed successfully"),
except ValueError:
   print("Invaild input! Please enter a number.")
