# Python Quitz For Fun 
x = int(input("Enter a number:"))
count = 0
count1 = 0
k = 0
for i in range(1,x+10):
    for j in range(1,x-i+1):
        print(" ",end=" ")
        count = count + 1
        while(k != 2*i-1):
            if (count<=x-1):
                print(i+k, end = " ")
                count = count + 1
            else:
                count1 = count1 + 1
                print((i+k-2*count1), end = "") 
                k = k + 1
                count1 = count1 = k = 0
    print()

