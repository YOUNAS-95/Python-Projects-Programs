tup1 = ('Robert', 'Carlos','1965','Terminator 1995', 'Actor','Florida')
tup2 = (1,2,3,4,5,6,7)
print (tup1[0::3])
print (tup2[0:4])

# Packing and Unpacking
x = ("Guru99", 20, "Education","younas",30,"Haris",40)    # tuple packing
(company, emp, profile,name,age,name2,age2) = x    # tuple unpacking
print(company, emp, profile,name,age,name2,age2)




# Comparing tuples
# case 1
a=(5,6)
b=(1,4)
if (a>b):
    print ("a is bigger")
else: 
    print ("b is bigger")

#case 2
a=(5,6)
b=(5,4)
if (a>b):
    print ("a is bigger")
else: print ("b is bigger")

#case 3
a=(5,6)
b=(6,4)
if (a>b):
    print ("a is bigger")
else: print ("b is bigger")

#Tuples and dictionary
a = {'x':100, 'y':200}
b = a.items()
print (b) 

# Slicing of Tuple
x = ('\'a\'', "b","c", "d", "e")
print("holle \"haris\" how are you")
a=x[2:4]
print (x[0:4])

a =int(input("Enter a Number"))
if a>=0:
     print("Positive")
elif a==-0:
     print("Nagetive")
else:
    print("Nagetive")