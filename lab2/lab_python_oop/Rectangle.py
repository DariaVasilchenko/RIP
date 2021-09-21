from lab_python_oop.GeomFigure import GeomFigure
from lab_python_oop.FigureColor import FigureColor

class Rectangle(GeomFigure):
    FIGURE_TYPE = "Прямоугольник"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = FigureColor()
        self.color.colorproperty = color

    def square(self):
        return self.height * self.width

    def __repr__(self):
        return '{} {} цвета шириной {} и высотой {} площадью {}'.format(
            Rectangle.get_figure_type(),
            self.color.colorproperty,
            self.width,
            self.height,
            self.square()
        )