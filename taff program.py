def younas():
 user=int(input("Enter your roll no:"))
 if user%2==0:
    print("even number")
 else:
    print("odd number")
    # this is for even numbers
    for i in range(0,21,2):
        z=i*user
        print(z)
 # this is for odd number
    for x in range(0,21,1):
        y=x*user
        print(x)
younas()