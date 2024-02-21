Dict = {
           'Tim': 18,
           'Charlie':12,
           'Tiffany':22,
           'Robert':25
    }	
print(Dict)

x = 20
y = 20
if ( x is y ):
	print ("x & y  SAME identity")
num = int(input("Enter a number: "))
a, b = 0, 1

while b < num:
    a, b = b, a + b

if b == num:
     print("Fibonacci number")
   
else:
    print("Not a Fibonacci number")


x = float(input("Enter the x-coordinate: "))
y = float(input("Enter the y-coordinate: "))
if x > 0 and y > 0:
    print("Quadrant I")
elif x < 0 and y > 0:
    print("Quadrant II")
elif x < 0 and y < 0:
    print("Quadrant III")
elif x > 0 and y < 0:
    print("Quadrant IV")
else:
    print("On the axes or at the origin")