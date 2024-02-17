user=int(input("Enter First No:"))

users=str(input("Enter a Operator:"))

userss=int(input("Enter Second No:"))
if users=="+":
 print("The Value of ", user , users, userss , " is:", user+userss ) 
 print("Anwser")
elif users=="-":
   print("The Value of ", user , users, userss , " is:", user-userss ) 
elif users=="*":
   print("The Value of ", user , users, userss , " is:", user*userss ) 
elif users=="%":
   print("The Value of ", user , users, userss , " is:", user%userss ) 
elif users=="/":
 print("The Value of ", user , users, userss , " is:", user/userss ) 
else:
  print("You Entered Invalid Syntax")