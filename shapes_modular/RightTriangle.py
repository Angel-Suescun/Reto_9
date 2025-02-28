from .triangle import Triangle

class RightTriangle(Triangle):
    def __init__(self, is_regular: bool = False, 
        vertices: list =[], 
        edges: list = [], 
        inner_angles: list = None) -> None:
        """Inicializa un triángulo rectangulo."""
        super().__init__(is_regular, vertices, edges)
