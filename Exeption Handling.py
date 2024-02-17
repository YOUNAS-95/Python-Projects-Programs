try:
    a=int(input("Enter a Number you want to print that number Table : "))
    for i in range(1,11):
        z=a*i
        print(a,"X",i,"=", z)
except:
   print("Value Error")
else:
    print("Fix The Error")
finally:
    print("Get Finally printed")



try:
    print("younas")
except:
    print("W")
else:
    print("hello")
finally:
    print("Again wrong")