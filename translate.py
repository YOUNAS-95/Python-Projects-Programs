# string="Hello Guys How Are You"
# dict1={'a':'1',
#        'b':'2',
#        'c':'3',
#        'd':'4',
#        'u':'5',
#        's':'6'
#        }
# t=string.maketrans(dict1)
# print(t)
# table="Hello Guys How Are You"
# s=table.translate(t)
# print(s)
string="younas zare so yloser wperson "
dict1="wxyz"
dict2="1234"
t=string.maketrans(dict1,dict2)
table=string.translate(t)
print(table)