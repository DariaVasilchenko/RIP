from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.Circle import Circle
from lab_python_oop.Square import Square

def main():
    rect = Rectangle(6, 6, "синего")
    circle = Circle(6, "зеленого")
    square = Square(6, "красного")
    print(rect)
    print(circle)
    print(square)

if __name__ == '__main__':
    main();


