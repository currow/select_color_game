import random


class Tablero:
    def __init__(self, tamano):
        self.colores = [["" for _ in range(tamano)] for _ in range(tamano)]

    def set_color(self, fila, columna, color):
        self.colores[fila][columna] = color

    def get_color(self, fila, columna):
        return self.colores[fila][columna]

    def rellena_tabla(self):
        # Calculamos el color a usar como valor a seleccionar de manera aleatorio
        valor_fijo = f"#{random.randint(0, 0xFFFFFF):06X}"

        # Porcentaje de probabilidad de que aparezca el color fijo. Lo seteamos por defecto
        probabilidad = 0.4
        # Cuenta el número total de celdas 
        total_celdas = sum(len(fila) for fila in self.colores)
        # Calculamos la cantidad de celdas que tendrán el color fijo según la probabilidad
        cantidad_fija = int(total_celdas * probabilidad)
        # Creamos un conjunto de índices aleatorios para las celdas que tendrán el color fijo
        celdas_fijas = set(random.sample(range(total_celdas), cantidad_fija))

        indice = 0
        # Recorremos la matriz de colores y asignamos el color fijo o un color aleatorio según corresponda
        for fila in range(len(self.colores)): # filas
            for columna in range(len(self.colores[fila])): # columnas
                if indice in celdas_fijas: # Si corresponde a una celda que debe tener el color fijo, lo asignamos
                    self.colores[fila][columna] = valor_fijo
                else: # En caso contrario, asignamos un color aleatorio
                    self.colores[fila][columna] = f"#{random.randint(0, 0xFFFFFF):06X}"
                indice += 1
                