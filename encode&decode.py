string='Yöunas'
# UTF-8 is use for special characater like this "ö" etc.
# Ascii is use for normal character like "Younas" etc.
# And encode function is use for encode the special character and show the encoded output to us of that character.
# Example Are written in program Below.
string_utf=string.encode('UTF-8')
print(string_utf)
user=input("Enter a Character You Want To Encode It like this Yöunas: ")
x=user.encode('ASCII')
print(x)
# Decode Function Han Bhai This function decode the encode function Magar Ye Compiler MAi Kam NAi kaRta 
# Only USed in Power shell And CMD. For example.

#   Decode Function not Working in program 
