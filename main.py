from shapes_modular.point import Point
from shapes_modular.line import Line
from shapes_modular.rectangle import Rectangle
from shapes_modular.square import Square
from shapes_modular.triangle import Triangle

try:
    # Create Point objects
    p1 = Point(0, 0)
    p2 = Point(4, 0)
    p3 = Point(4, 3)
    p4 = Point(0, 3)
    p5 = Point(0, 0)
    p6 = Point(4, 0)
    p7 = Point(2, 3)

    # Create Line objects
    l1 = Line(p1, p2)
    l2 = Line(p2, p3)
    l3 = Line(p3, p4)
    l4 = Line(p4, p1)
    l5 = Line(p5, p6)
    l6 = Line(p6, p7)
    l7 = Line(p7, p5)

    # Create Rectangle object
    rectangle = Rectangle(vertices=[p1, p2, p3, p4], edges=[l1, l2, l3, l4])
    print(f"Área del rectángulo: {rectangle.compute_area()}")
    print(f"Perímetro del rectángulo: {rectangle.compute_perimeter()}")

    # Create Square object
    square = Square(vertices=[p1, p2, p3, p4], edges=[l1, l2, l3, l4])
    print(f"Área del cuadrado: {square.compute_area()}")
    print(f"Perímetro del cuadrado: {square.compute_perimeter()}")

    # Create Triangle object
    triangle = Triangle(vertices=[p5, p6, p7], edges=[l5, l6, l7])
    print(f"Área del triángulo: {triangle.compute_area():.2f}") 
    print(f"Perímetro del triángulo: {triangle.compute_perimeter():.2f}")
except Exception as e:
    print(f"Error: {e}")