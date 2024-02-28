marks =int(input("Total marks :"))
obtained_marks=int(input("Obtained Marks:"))
grade=obtained_marks/marks*100
print(grade)
if grade>=90:
    print("grade A")
elif grade>80 and grade<90:
    print("grade B")
elif grade>70 and grade<80:
     print("grade C")
elif grade>60 and grade<70:
    print("grade D")
elif grade>50 and grade<60:
    print("grade E")
else:
    print(" you are fail")
