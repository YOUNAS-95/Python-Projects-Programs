y="hello {} , How are {}".format("YOUNAS", "YOU")
print(y)
y="Wellcome {} To Python programming {}".format("Younas","Language.")
print(y)
# Here we are using indexing to print the "format" statement.
y="Wellcome {0} {2} Python Programming {1}".format("Younas","Language.","To")
print(y)
#  Here We Are using Some Spaces Condition in Format().Method.
#                 ("<") This function is use for declared Varaible Right Side Spacing.
#                   for Example --------10
y="Wellcome {a:<10} To Python Programming {b:>7}".format(a=10,b=20)
print(y)#         (">") This function is use for left Side Varaible spacing.
                    #  For Example  10--------
                    # ("^") This functionis use for Both Side varaible spacing.
                    # For Example----10---- 
