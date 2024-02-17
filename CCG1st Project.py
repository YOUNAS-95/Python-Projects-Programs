print("Wellcome To Color Choise Game !")
print("Select The Color From The Following List: ")
list=['RED','GREEN','BLUE','YELLOW']
print(list)
def younass():
    print("Choise a Color You want")
    list=['RED','GREEN','BLUE','YELLOW']
    print(list)
while True:
    user=str.upper(input("Now Enter a Color: "))
    if user=="RED":
        x=int(input("WOW Great ! Now Enter a Number 1 or 2: "))
        if x==1:
            print("Idiot")
            print("Do you Want to play Again:")
            i=str(input("y/n: "))
            if i=="y":
             younass()
            elif i =="n":
             print("Thanks For Playing Game See You Next Time ! ")
             exit()
            else:
             print("Please Enter Only y/n and Try again")
        elif x==2:
             print("buffalo")
             print("Do you Want to play Again:")
             farhad=str and str(input("y/n: "))
             if farhad=="y":
              younass()
            
             elif farhad=="n":
              print("Thanks For Playing Game See You Next Time ! ")
              exit()
             else:
              print("Please Enter Only y/n and Try again")
        else:
          print("ALERT: Only 1 0r 2 can be selcted")
    
    elif user=="GREEN":
          i=int(input("WOW Great ! Now Enter a Number 3 or 4: "))
          if i==3:
             print("Cat")
             print("Do you Want to play Again:")
             haseeb=str(input("y/n: "))
             if haseeb=="y":
              younass()
          
             elif haseeb=="n":
               print("Thanks For Playing Game See You Next Time ! ")
               exit()
             else:
              print("Please Enter Only y/n and Try again")
          
          elif i==4:
            print("Dog")
            print("Do you Want to play Again:")
            j=str(input("y/n: "))
            if j=="y":
             younass()
          
            elif j=="n":
               print("Thanks For Playing Game See You Next Time ! ")
               exit()
            else:
              print("Please Enter Only y/n and Try again")
          else:
             print("ALERT: Only 3 0r 4 can be selcted")
    elif user=="BLUE":
            y=int(input("WOW Great ! Now Enter a Number 5 or 6: "))
            if y==5:
             print("Snake")
             print("Do you Want to play Again:")
             sharry=str(input("y/n: "))
             if sharry=="y":
               younass()
             elif sharry=="n":
              print("Thanks For Playing Game See You Next Time ! ")
              exit()
             else:
               print("Please Enter Only y/n and Try again")
  
            elif y==6:
             print("Monkey")
             print("Do you Want to play Again:")
             don=str(input("y/n: "))
             if don=="y":
              younass()
             elif don=="n":
              print("Thanks For Playing Game See You Next Time ! ")
              exit()
             else:
              print("Please Enter Only y/n and Try again")
            else:
             print("ALERT: Only 5 0r 6 can be selcted")
    elif user=="YELLOW":
            a=int(input("WOW Great ! Now Enter a Number 7 or 8: "))
            if a==7:
               print("You Are King of Heart")
               print("Do you Want to play Again:")
               e=str(input("y/n: "))
               if e=="y":
                 younass()
               elif e=="n":
                 print("Thanks For Playing Game See You Next Time ! ")
                 exit()
               else:
                  print("Please Enter Only y/n and Try again")
            elif a==8:
               print("Loser")
               print("Do you Want to play Again:")
               jehan=str(input("y/n: "))
               if jehan=="y":
                 younass()
               elif jehan=="n":
                  print("Thanks For Playing Game See You Next Time ! ")
                  exit()
               else:
                  print("Please Enter Only y/n and Try again")
            else:
              print("ALERT: Only 7 0r 8 can be selcted")
    else:
        print(" You Entered Invalid Color. Please entered a correct spaling.\nPlease reads The message Carefully and Try Again")
  

