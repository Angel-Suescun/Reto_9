from .triangle import Triangle

class Isosceles(Triangle):
    def __init__(self, is_regular: bool = False, 
            vertices: list =[], 
            edges: list = [], ) -> None:
        """Inicializa un triángulo isósceles."""
        super().__init__(is_regular, vertices, edges)
