import math

class Point:
    def __init__(self, x: float, y: float) -> None:
        """Inicializa un punto con coordenadas x e y."""
        self._x = x
        self._y = y

    def compute_distance(self, other_point: 'Point') -> float:
        """Calcula la distancia a otro punto."""
        return math.sqrt((self._x - other_point._x) ** 2 + (self._y - other_point._y) ** 2)

    def set_coordinates(self, x: float, y: float) -> None:
        """Establece nuevas coordenadas x e y para el punto."""
        self._x = x
        self._y = y

    def get_x(self) -> float:
        """Obtiene la coordenada x del punto."""
        return self._x

    def get_y(self) -> float:
        """Obtiene la coordenada y del punto."""
        return self._y

if __name__ == '__main__':
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    print(p1.compute_distance(p2))  # 5.0