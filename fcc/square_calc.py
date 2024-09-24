class Rectangle: 
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height
    
    def get_perimetr(self):
        return 2* (self.width + self.height)
    
    def get_diagonal(self):
        return (self.width**2 + self.height**2)**0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "To big!"
        picture = (("*" * self.width) + "\n") * self.height
        return picture

    def get_amount_inside(self, shape):
        return (self.width // shape.width) * (self.width // shape.height)
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)
    
    def __str__(self):
        return f'Square(side={self.width})'

rect = Rectangle(12, 8)
print(rect.get_area())
rect.set_height(1)
print(rect.get_perimetr())
print(rect)

sq = Square(7)

print(sq.get_area())
sq.set_side(2)
print(sq.get_diagonal())
print(sq.get_picture())