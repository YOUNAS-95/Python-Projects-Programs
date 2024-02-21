print ("TOOl TAX MACHINE!")

def Tool ():

    while True:

        print("Islamabad To Lahore Tool Plaza Tax..")
        print("Here The List's..")
        print("Cars Tool tax 3$")
        print("Truck Tool tax 6$")
        print("Busses Tool tax 10$")

        user = str.capitalize(input("Select a Vechile: "))

        if user == 'Cars':
            amount = int(input("Collect the Amount: "))
            if amount == 3:
                print("Thank you! Take Your Slip.")
                print("RESTART THE MACHINE, Press the KEY > 1")
                again = int(input("Press: "))
                if again == 1:
                    print("Choose a Vechile")
                else:
                    print("Error")
            else:
                print("Stop Please Give the right amount.")
                wrong = int(input("AMOUNT: "))
                if wrong == 3:
                    print("Thank you!")
                else:
                    exit()

        elif user == 'Truck':
            a = int(input("Collect the Amount: "))
            if a == 6:
                print("Thank you! Take Your Slip.")
                print("RESTART THE MACHINE, Press the KEY > 1")
                ag = int(input("Press: "))
                if ag == 1:
                    print("Choose a Vechile")
                else:
                    print("Error")
            else:
                print("Stop Please Give the right amount")
                w = int(input("AMOUNT: "))
                if w == 3:
                    print("Thank you!")
                else:
                    exit()

        elif user == 'Busses':
            amo = int(input("Collect the Amount: "))
            if amo == 10:
                print("Thank you! Take Your Slip.")
                print("RESTART THE MACHINE, Press the KEY > 1")
                again = int(input("Press: "))
                if again == 1:
                    print("Choose a Vechile")
                else:
                    print("Error")
            else:
                print("Stop Please Give the right amount")
                wro = int(input("AMOUNT: "))
                if wro == 3:
                    print("Thank you!")
                else:
                    exit()

        else:
            print("Invalid vechile,Please enter a right vechile category")

Tool()  