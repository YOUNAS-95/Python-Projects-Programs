class About():
  
    name =  "younas" 
    occupation = "Software engineer"
    salaray = 100000
    
    def younas(self):
     
     print(f"{self.name} is a {self.occupation} and its salary is {self.salaray}")
 
a = About()
b = About()
c = About()

a.name = "haris"
a.occupation = "Software Engineer"
a.salaray = 20000

b.name= "Yousaf"
b.occupation = "Accountant"
b.salaray = 30000


a.younas()
b.younas()
c.younas()



