from .triangle import Triangle

class Equilateral(Triangle):
    def __init__(self, vertices: list, edges: list) -> None:
        """Inicializa un triángulo equilátero."""
        super().__init__(vertices, edges)

