from .line import Line
from .point import Point
import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Tiempo de ejecución de {func.__name__}: {end_time - start_time:.6f} segundos")
        return result
    return wrapper

class Shape:
    def __init__(self, is_regular: bool = True) -> None:
        """Inicializa una figura geométrica con regularidad opcional."""
        self._is_regular = is_regular
        self._vertices = []
        self._edges = []

    @property
    def vertices(self) -> list:
        """Obtiene los vértices de la figura."""
        return self._vertices

    @vertices.setter
    def vertices(self, vertices: list) -> None:
        """Establece los vértices de la figura, verificando que sean válidos."""
        if all(isinstance(vertex, Point) for vertex in vertices):
            self._vertices = vertices
        else:
            raise ValueError("Todos los vértices deben ser objetos de tipo Point.")

    @property
    def edges(self) -> list:
        """Obtiene las aristas de la figura."""
        return self._edges

    @edges.setter
    def edges(self, edges: list) -> None:
        """Establece las aristas de la figura, verificando que sean válidas."""
        if all(isinstance(edge, Line) for edge in edges):
            self._edges = edges
        else:
            raise ValueError("Todas las aristas deben ser objetos de tipo Line.")

    @property
    def inner_angles(self) -> list:
        """Obtiene los ángulos interiores de la figura."""
        return self._inner_angles

    @inner_angles.setter
    def inner_angles(self, inner_angles: list = None) -> None:
        """
        Establece los ángulos interiores de la figura. 
        Se calculan automáticamente si es regular.
        """
        if self._is_regular:
            n = len(self._vertices)
            self._inner_angles = [(180 * (n - 2)) / n] * n
        else:
            print("La figura no es regular, los triángulos tiene funcion especial")

    @timing_decorator
    def compute_area(self) -> float:
        """Calcula el área de la figura (debe ser implementado en subclases)."""
        raise NotImplementedError(
            "El método para calcular el área debe implementarse en las subclases.")

    @timing_decorator
    def compute_perimeter(self) -> float:
        """Calcula el perímetro de la figura como la suma de sus aristas."""
        return sum(edge.get_length() for edge in self._edges)

    @classmethod
    def from_vertices_and_edges(cls, vertices: list, edges: list, is_regular: bool = True):
        """Crea una instancia de Shape a partir de vértices y aristas."""
        instance = cls(is_regular)
        instance.vertices = vertices
        instance.edges = edges
        return instance

if __name__ == '__main__':
    p1 = Point(0, 0)
    p2 = Point(3, 0)
    p3 = Point(3, 4)
    p4 = Point(0, 4)
    l1 = Line(p1, p2)
    l2 = Line(p2, p3)
    l3 = Line(p3, p4)
    l4 = Line(p4, p1)
    r = Shape.from_vertices_and_edges([p1, p2, p3, p4], [l1, l2, l3, l4], is_regular=True)
    print(r.compute_perimeter())  # 14.0
    r.inner_angles = None
    print(r.inner_angles)  # [90.0, 90.0, 90.0, 90.0]