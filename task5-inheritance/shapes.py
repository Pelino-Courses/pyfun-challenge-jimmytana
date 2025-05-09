from math import pi,sqrt
"""
progrma to calculate area ,perimeter of diferent shapes
"""
class shape:
  
    def __init__(self,name:str):
       
        if not isinstance(name,str):
            raise TypeError ("name must be a string.")
        self.name=name
    def area(self):
        """
        calculate the area of the shape 
        returns:
        float:area of the shape
        """
        raise NotImplementedError("subclasses must implement the are method")

    def __str__(self):
        return f"{self.name}"
class Circle(shape):
    """
    calculates the area and perimeter of a circle
    """
    def __init__(self,radius:float):
        super().__init__("circle")
        if radius<=0:
            raise ValueError("radius should be positive")
        self.radius=radius
    def area(self):
        return pi * self.radius**2
    def perimeter(self):
        return 2 *pi * self.radius
    def __str__(self):
        return f"{self.name}(radius={self.radius})"
class Rectangle(shape):
    """
    calculates the are and perimeter of rectangle
    """
    def __init__(self, width:float,height=float):
        super().__init__("rectangle")
        if width<=0 or height<=0:
            raise ValueError("width and height must be positive")
        self.width=width   
        self.height=height
    def area(self):
        return self.width*self.height
    def perimeter(self):
        return 2*(self.width+self.height)
class Triangle(shape):
    def __init__(self, a:float,b:float,c:float):
        super().__init__("Triangle")
        if any (side <=0 for side in (a,b,c)):
            raise ValueError("all side should be positive")
        if a+b <=c or a+c<=b or b+c<=a:
            raise ValueError("invalide side length")
        self.a=a
        self.b=b
        self.c=c
    def area(self):
        s=self.perimeter()/2
        return sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
    def perimeter(self):
        return self.a+self.b+self.c
    def __str__(self):
        return f"{self.name}(a={self.a},b={self.b},c={self.c})"
    # @classmethod
shapes=[ 
    Circle(5),
    Rectangle(4,6),
    Triangle(3,4,5),
    ]
for shape in shapes:
    print(f"{shape}-> Area:{shape.area():.2f},perimeter:{shape.perimeter():.2f}")