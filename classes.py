class calculator:
    def __init__(self):
        self.current = 12 
    
    def add(self, amount):
        self.current +=amount
    def getCurrent(self):
        return self.current
a= calculator()
a.current
a.getCurrent()
a.add(1)
 