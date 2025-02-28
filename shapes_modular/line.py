from .point import Point

class Line:
    def __init__(self, start_point: Point, end_point: Point) -> None:
        """Inicializa un segmento de línea definido por dos puntos."""
        self._start_point = start_point
        self._end_point = end_point
        self._length = start_point.compute_distance(end_point)

    def get_length(self) -> float:
        """Obtiene la longitud de la línea."""
        if self._length <= 0:
            raise ValueError("La longitud de la línea no puede ser negativa.")
        return self._length

if __name__ == '__main__':
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    l = Line(p1, p2)
    print(l.get_length())  # 5.0
