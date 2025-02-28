from .triangle import Triangle

class Scalene(Triangle):
    def __init__(self, is_regular: bool = False, 
        vertices: list =[], 
        edges: list = []) -> None:
        """Inicializa un triángulo escaleno."""
        super().__init__(is_regular, vertices, edges)
