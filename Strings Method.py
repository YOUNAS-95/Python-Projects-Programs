
while True:
    chr = input("enter a character \n")
    if(chr.isalpha()):
        print("character is alphabet")
        break
    if(chr.isdigit()):
        print("character is digit")
        break
    if(chr.isascii()):
        print("you type wrong character")
        break

