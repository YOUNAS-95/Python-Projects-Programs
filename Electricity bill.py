# To calculate the electricity bill
# if 500 unit used-pay pay 5.Rs for each unit
# if 700 unit used-pay pay 10.Rs for each unit
# if 1000 unit used-pay pay 15.Rs for each unit
# if more than 1000 unit used-pay pay 20.Rs for each unit
def electricity_bill(n):
    if n<500:
        print("your bill Rs is",n*5)
    elif n>500 and n<700:
        print("your bill Rs is",n*10)
    elif n>700 and n<1000:
        print("your bill Rs is",n*15)
    elif n>1000:
        print("your bill Rs is",n*20)
def instruction():
    print("The last of date of electricity bill is 20 april")
    print("after 20 april you have to submit electricity bill then you will pay a fine 1000Rs")

for i in range(5):
    a=input("Enter a customer name")
    n=int(input("Enter the electricity unit you have used"))
    electricity_bill(n)
    print()
    instruction()

