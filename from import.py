from publicacion import Publicacion
from habito import Habito

class Libro(Publicacion, Habito):
    """Hereda de Publicación y aplica hábitos de lectura"""
    def __init__(self, titulo: str, año: int, autor: str, paginas_totales: int):
        Publicacion.__init__(self, titulo, año)
        Habito.__init__(self, meta_diaria=10)  # Meta de 10 páginas/día
        self.autor = autor
        self.paginas_totales = paginas_totales
        self.paginas_leidas = 0

    def leer_paginas(self, cantidad: int):
        self.paginas_leidas += cantidad
        super().actualizar_progreso(cantidad)
        if self.paginas_leidas >= self.paginas_totales:
            print(f"¡Felicidades! Has completado el libro: {self._titulo}")

    def __str__(self):
        porcentaje = (self.paginas_leidas / self.paginas_totales) * 100
        return (f"{super().__str__()} - {self.autor}\n"
                f"Progreso: [{self.paginas_leidas}/{self.paginas_totales}] "
                f"({porcentaje:.1f}%) | Racha: {self._racha} días")


if __name__ == "__main__":
    # Ejemplo de uso
    habito_atomico = Libro("Hábitos Atómicos", 2018, "James Clear", 320)
    
    dias_lectura = [15, 8, 12, 10, 5, 15]
    for dia, paginas in enumerate(dias_lectura, 1):
        print(f"\nDía {dia} de lectura:")
        habito_atomico.leer_paginas(paginas)
    
    print("\nEstado final:")
    print(habito_atomico)