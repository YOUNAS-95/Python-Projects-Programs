# ! COLOUR CHOICE GAME !
print("Welcome to Colour Choice Game!")

def Game ():
    while True:
            lists=['Red','Green','Blue','Black']
            print(lists)
            user=str.capitalize(input("Choose Your Colour: "))
            if user == 'Red':
                x=int(input("Enter A Number From.1/2: "))
                if x==1:
                    
                    print("'You Are DOG'.")
                elif x==2:
                    print("'You Are CAT'.")
                else:
                    print("You Entered a Wrong Number")
                    print("IF You Want To Play Again.Enter , y/n ")
                    b=str.lower(input("Enter an Alphabet: "))
                    if b=='y':
                      Game()
                    elif b=='n':
                        print("Thanks For Playing A GAME,GOOD BYE!")
                        exit()
            elif user=='Green':
                l=int(input("Enter A Number From.1/2: "))
                if l==1:
                    print("'You Are MONKEY'.")
                elif l==2:
                    print("'You Are DINASOUR'.")
                else:
                    print("You Entered a Wrong Number")
                    print("IF You Want To Play Again.Enter , y/n ")
                    n=str.lower(input("Enter an Alphabet: "))
                    if n=='y':
                      Game()
                    elif n=='n':
                        print("Thanks For Playing A GAME,GOOD BYE!")
                        exit()
            elif user == 'Blue':
                q=int(input("Enter A Number From.1/2: "))
                if q==1:
                    print("'You Are DONKEY'.")
                elif q==2:
                    print("'You Are GIREAFE'.")
                else:
                    print("You Entered a Wrong Number")
                    print("IF You Want To Play Again.Enter , y/n ")
                    d=str.lower(input("Enter an Alphabet: "))
                    if d=='y':
                      Game()
                    elif d=='n':
                        print("Thanks For Playing A GAME,GOOD BYE!")
                        exit()
            elif user == 'Black':
                k=int(input("Enter A Number From.1/2: "))
                if k==1:
                    print("'You Are PARROT'.")
                if k==2:
                    print("'You Are GOAT'.")
                else:
                    print("You Entered a Wrong Number")
                    print("IF You Want To Play Again.Enter , y/n ")
                    d=str.lower(input("Enter an Alphabet: "))
                    if d=='y':
                      Game()
                    elif d=='n':
                        print("Thanks For Playing A GAME,GOOD BYE!")
                        exit()       
            else:
                print("You Entered an Invalid Colour, Please enter a valid colour to continue the Game.\nThank U ")
Game()