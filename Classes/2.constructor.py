class MyClass():
    
    def __init__(self, x, y):
        self.a = x
        self.b = y
        
        # adding
        self.c = self.a + self.b
    
    def printMe(self):
        print(self.c)
        
obj = MyClass(1, 3)
obj.printMe()