
class Point():
    def __init__(self, coordinateX, coordinateY):
        self.x = coordinateX
        self.y = coordinateY
        
    def printMe(self):
        coordinate = (self.x, self.y)
        print(coordinate)
        

obj = Point(1, 3)
obj.printMe()