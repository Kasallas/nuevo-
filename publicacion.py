class Publicacion:
    """Clase base para publicaciones"""
    def __init__(self, titulo: str, año: int):
        self._titulo = titulo
        self._año = año

    def __str__(self):
        return f"{self._titulo} ({self._año})"