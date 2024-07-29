class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    @x.setter
    def x(self, value):
        if isinstance(value, (int, float)):
            self.__x = value
        else:
            raise ValueError("Must be a NUMBER!!!")
    
    @y.setter
    def y(self, value):
        if isinstance(value, (int, float)):
            self.__y = value
        else:
            raise ValueError("Must be a NUMBER!!!")
        
    
class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        elif index == 1:
            return self.coordinates.y
        else:
            raise IndexError

    def __setitem__(self, index, vaule):
        if index == 0:
            self.coordinates.x = vaule
        elif index == 1:
            self.coordinates.y = vaule
        else:
            raise IndexError 
p = Point(1,15)

v = Vector(p)

print(v[1])

v[0] = 100
v[1] = 130

print(f"After modification: x coordinate: {v[0]}")  # Should print: After modification: x coordinate: 10
print(f"After modification: y coordinate: {v[1]}") 