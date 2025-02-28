import math

from .shape import Shape

class Triangle(Shape):
    def __init__(self,
                is_regular: bool = True, 
                vertices: list = [], 
                edges: list = [], 
                ) -> None:
        """
        Inicializa un triángulo con tres vértices, tres aristas y ángulos.
        """
        super().__init__(is_regular)
        if len(vertices) == 3 and len(edges) == 3:
            self.vertices = (vertices)
            self.edges = edges
        else:
            raise ValueError("Un triángulo debe tener 3 vértices y 3 aristas.")

    def compute_area(self) -> float:
        """Calcula el área del triángulo utilizando la fórmula de Herón."""
        s = self.compute_perimeter() / 2
        return math.sqrt(s * (s - self._edges[0].get_length()) 
                         * (s - self._edges[1].get_length()) 
                         * (s - self._edges[2].get_length())
                )
    def compute_inner_angles(self) -> None:
        """Calcula los ángulos interiores del triángulo."""
        a = self._edges[0].get_length()
        b = self._edges[1].get_length()
        c = self._edges[2].get_length()
        
        cos_A = (b**2 + c**2 - a**2) / (2 * b * c)
        cos_B = (a**2 + c**2 - b**2) / (2 * a * c)
        cos_C = (a**2 + b**2 - c**2) / (2 * a * b)

        radians_A = math.acos(cos_A)
        radians_B = math.acos(cos_B)
        radians_C = math.acos(cos_C)

        self._inner_angles = [
            math.degrees(radians_A),
            math.degrees(radians_B), 
            math.degrees(radians_C)]


