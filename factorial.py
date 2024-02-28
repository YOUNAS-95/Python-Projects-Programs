# numbers=1
# while numbers<=50:
#    if numbers % 2==0:
#      print(numbers)
#    numbers=numbers+1



n = int(input("Enter a number: "))
fact = 1
while n > 0:
    fact *= n
    n -= 1
print("Factorial:", fact)