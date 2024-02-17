print("Wellcome To The ATM Machine")
def younas():
    while True:
     w=int(input("Please Enter Your Pincode: "))
     if w== 0000:
       print("Your total Amount Is Rs.1000")
    
       print("Select The Method From The Following List: ")
       select=int(input("Enter \"1\" For Cash Withdraw\nEnter \"2\" For Cash Deposite\nEnter \"3\" For Check Balance\nEnter \"4\" For Quite\nNow Enter a Number : "))
       
       if select==1:
            Amount=1000
            x=int(input("Enter a Amount You Want To Withdraw: "))
            if x<1000:
             z=Amount-x
             print("Cash Withdraw")
             print("Your Remaining Balance is",z)
            elif x>1000:
               print("Efficience Balance Please Enter a Amount")
            else:
               print("Invalid Syntax You Entered")
       elif select==2:
           amount=1000
           y=int(input("Enter a Deposite Amount: "))
           print("Cash deposite")
           d=amount+y
           print("Your Total balance is: ",d)
       elif select==3:
            print("Your Current Balance is Rs.1000 ")
       elif select==4:
           print("Thanks For Using our service")
           exit()
       else:
           print("Please read the Statements Carefully")
     else:
       print("Alert ! Wrong Pincode")
       exit()
younas()
