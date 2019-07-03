import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, p):
        if type(p) is not Point:
            return False
        return self.x == p.x and self.y == p.y

    def __mul__(self, v):
        self.scale(v)
        return self
    
    def distance(self, p): # method, or 'member function'
        dx = self.x - p.x
        dy = self.y - p.y
        return math.sqrt(dx*dx + dy*dy)
    
    def scale(self, v):
        self.x *= v
        self.y *= v
    

if __name__ == '__main__':
    p1 = Point()
    p2 = Point()
    p3 = Point(1,1)
    print(p1)
    print(p2)
    p1pointer = p1

    print(p1 == p2)
    print(p1.__eq__(p2))
    print(p1 == p1pointer)
    print(p1 != p2)
    print(p1.__ne__(p2))
    print(p3*11)
    print(p3.scale(11))
    print(p1 + p2)
    