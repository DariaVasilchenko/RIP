from lab_python_oop.FigureColor import FigureColor
from lab_python_oop.Rectangle import Rectangle

class Square(Rectangle):
    FIGURE_TYPE = "Квадрат"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, length, color):
        self.length = length
        super().__init__(self.length, self.length, color)

    def __repr__(self):
        return '{} {} цвета со стороной {} площадью {}'.format(
            Square.get_figure_type(),
            self.color.colorproperty,
            self.length,
            self.square()
        )
