# Get three numbers as input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))


if num1 >= num2 and num1 >= num3:
    
    print("the largest no is ",num1)

elif num2 >= num1 and num2 >= num3:
    print("the largest no is ",num2)

else:
    print("the largest no is ",num3)


# Smart way to find Largest No:

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))


largest_number = max(num1, num2, num3)


print(f"The largest number is: {largest_number}")

