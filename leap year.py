
leap=int(input("enter a year"))
if (leap%4==0 and leap%100!=0 or leap%400==0):
    print("it is a leap year")
else:
    print("it is not a leap year")