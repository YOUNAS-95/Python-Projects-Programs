for i in range(10):
    print('*' * (i + 1))

num= int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"Factorial of {num}: {factorial}")

# my_string = "Hello, World!"
# vowel_count = 0
# for char in my_string:
#     if char.lower() in 'aeiou':
#         vowel_count += 1
# print("Number of vowels:", vowel_count)
