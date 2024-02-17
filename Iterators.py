# list =  ["younas ", "Haris" , "Yousaf", "Farhad"]
# obj = iter(list)
# print(obj.__next__())

var = "Younas"
item = iter(var)
while True:
    try :
        hars = next(item)
        print(hars)

    except  StopIteration:
        break
