print("Wellcome To The ATM Machine")
print("Select The Method From The Following List : ")
list=['Cash Withdraw','Cash Deposite','Check Balance']
def younas():
 while True:
     a=int(input("Enter \"1\" For Cash Withdraw \nEnter \"2\" For Cash Deposite \nEnter \"3\" For Check Balance\nEnter \"4\" for Quit:\nNow Enter a Number: "))
     if a==1:
        print("Your Total Amount is Rs:1000 Please Withdraw Under Your Amount")
        b=1000
        c=int(input("Enter a Amount You want To Withdraw under Your Amount: "))
        if b<1000:
          print("Cash Withdraw")
          e=b-c
          print("Your Remain Balance is : ",e)
        elif c>1000:
          print("\"Efficience Balance\"")
        else:
         print("Invalid ")
     elif a==2:
       b=1000
       x=int(input("Enter a Amount You Wont to Deposite: "))
       z=x+b
       print("Cash Deposite :",z)
     elif a==3:
       print("Your Total Amount is Rs.1000") 
     elif a==4:
       exit()
     else:
       print("Chwlia na MAr")



younas()


