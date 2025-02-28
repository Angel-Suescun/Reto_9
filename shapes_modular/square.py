from .rectangle import Rectangle


class Square(Rectangle):
    def compute_area(self) -> float:
        """
        Calcula el área del cuadrado como el cuadrado de la longitud de un lado.
        """
        return self._edges[0].get_length() ** 2
    
