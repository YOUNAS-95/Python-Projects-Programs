
while True:
  user = str.lower(input("Enter a single character You Want to Check its Vowel or Not : "))

  if user in 'ieaou':
    print("This is vowel")
  else:
    print("This is consonant")