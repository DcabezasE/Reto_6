class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def compute_distance(self, point):
        # Calcular la distancia entre dos puntos utilizando la fórmula de la distancia euclidiana
        dx = self.x - point.x
        dy = self.y - point.y
        return (dx**2 + dy**2)**0.5