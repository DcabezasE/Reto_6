import geometric_shapes.point as Poin
class Line():
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point
        self.length = start_point.compute_distance(end_point)
