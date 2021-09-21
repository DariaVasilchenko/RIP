from lab_python_oop.GeomFigure import GeomFigure
from lab_python_oop.FigureColor import FigureColor
import math

class Circle(GeomFigure):
    FIGURE_TYPE = "Круг"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, radius, color):
        self.radius = radius
        self.color = FigureColor()
        self.color.colorproperty = color

    def square(self):
        return math.pi * (self.radius**2)

    def __repr__(self):
        return '{} {} цвета радиусом {} площадью {}'.format(
            Circle.get_figure_type(),
            self.color.colorproperty,
            self.radius,
            self.square()
        )