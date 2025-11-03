import math
from geometric_figure import GeometricFigure
from color import Color

class Circle(GeometricFigure):
    FIGURE_TYPE = "Круг"
    
    def __init__(self, radius, color):
        self.radius = radius
        self.color = Color(color)
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def __repr__(self):
        return "{} {} цвета радиусом {}, площадью {:.2f}.".format(
            self.FIGURE_TYPE,
            self.color.color,
            self.radius,
            self.area()
        )
    
    @classmethod
    def get_name(cls):
        return cls.FIGURE_TYPE
