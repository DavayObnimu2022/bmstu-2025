
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from geometric_figure import GeometricFigure
from color import Color

class Rectangle(GeometricFigure):
    FIGURE_TYPE = "Прямоугольник"
    
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = Color(color)
    
    def area(self):
        return self.width * self.height
    
    def __repr__(self):
        return "{} {} цвета шириной {} и высотой {}, площадью {}.".format(
            self.FIGURE_TYPE,
            self.color.color,
            self.width,
            self.height,
            self.area()
        )
    
    @classmethod
    def get_name(cls):
        return cls.FIGURE_TYPE
