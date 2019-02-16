class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y    

class Circle():
    def __init__(self, center, r): 
        self.r = r
        self.center = (center.x, center.y)
    
    def get_area(self):
        return 3.14 * self.r**2
    def get_perimeter(self):
        return 2 * 3.14 * self.r
    def get_center(self):
        return self.center
    def print(self):
        print(f'Circle:{self.center} ,r:{self.r}')

p1 = Point(0, 0)
c1 = Circle(p1, 3)
print(c1.get_area()) 
print(c1.get_perimeter()) 
print(c1.get_center())
c1.print()
p2 = Point(4, 5)
c2 = Circle(p2, 1)
print(c2.get_area())
print(c2.get_perimeter())
print(c2.get_center())
c2.print()