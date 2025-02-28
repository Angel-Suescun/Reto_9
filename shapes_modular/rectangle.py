from .shape import Shape

class Rectangle(Shape):
    def __init__(self, vertices: list, edges: list) -> None:
        """Inicializa un rectángulo con cuatro vértices y cuatro aristas."""
        super().__init__(is_regular=True)
        if len(vertices) == 4 and len(edges) == 4:
            self.vertices = vertices
            self.edges = edges
        else:
            raise ValueError("Un rectángulo debe tener 4 vértices y 4 aristas.")

    def compute_area(self) -> float:
        """Calcula el área del rectángulo como el producto de dos lados."""
        return self._edges[0].get_length() * self._edges[1].get_length()