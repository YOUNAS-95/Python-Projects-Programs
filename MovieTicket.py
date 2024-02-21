# Movies Ticket Distribution With Age limitation.
while True:
  User = int(input("Please Enter Your Age: "))

  if User < 12 :
    print("Your Ticket PRice is 5$.")
  
  elif User >= 12 and User <= 18 :
#   elif     12 < User <=18:
    print("Your Ticket Price is 8$.")
  else:
    print("Your ticket Price is 10$.")


