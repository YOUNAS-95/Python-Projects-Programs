class bankacount:
  
  def withdraw(argu1):
    
        print("SELECT THE METHOD FROM THE FOLLOWING LIST:")
        select=int(input("Enter \"1\" For cash Withdraw:\nNow Enter A No:"))
        if select==1:
         Amount=1000
         a=int(input("Enter your Withdraw Amount" ))
         if a<1000:
           z=Amount-a
           print("cash Withdrw")
           print("Your Remaing Balance is",z)
         elif a>1000:
            print("Efficience Balance")
         else:
           print("Invalid Syntax You Entered !")
           

  def deposite(argu2):
       
        print("Do you want to deposite:")
        select=int(input("Enter \"2\" For cash Deposite:\nNow Enter A No:"))
        if select==2:
         amount=1000  
         a=int(input("Enter your deposit amount:"))
         c=amount+a
         print("cash Withdraw:",c)
        else:
           print("Invalid Syntax")

obj = bankacount()
obj.withdraw()
obj.deposite()
#ye bankacount ka project hai 

