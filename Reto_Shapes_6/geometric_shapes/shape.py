import geometric_shapes.line as lin
import geometric_shapes.point as Poin
from math import acos
from math import degrees

class Shape:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = [lin.Line(vertices[i], vertices[(i + 1) % len(vertices)]) for i in range(len(vertices))]
        self.inner_angles = self.compute_inner_angles()
        self.regular = self.compute_regular()
    def compute_regular(self):
        regular = False
        v1=0
        v2=0
        for edge in self.edges:
            v2 = round(edge.start_point.compute_distance(edge.end_point))
            if v1 != 0:
                if v1 == v2:
                    regular=True
                    v1 = v2
                else:
                    regular= False
            else:
                v1 = v2
        return regular


    def compute_inner_angles(self):
        # Calcular los ángulos internos de la forma
        angles = []
        for i in range(len(self.vertices)):
            prev_point = self.vertices[i - 1]
            current_point = self.vertices[i]
            next_point = self.vertices[(i + 1) % len(self.vertices)]

            # Calcular los vectores entre los puntos
            v1 = Poin.Point(prev_point.x - current_point.x, prev_point.y - current_point.y)
            v2 = Poin.Point(next_point.x - current_point.x, next_point.y - current_point.y)

            # Calcular el ángulo entre los vectores utilizando el producto escalar
            dot_product = v1.x * v2.x + v1.y * v2.y
            magnitude_v1 = (v1.x**2 + v1.y**2)**0.5
            magnitude_v2 = (v2.x**2 + v2.y**2)**0.5
            angle_rad = acos(dot_product / (magnitude_v1 * magnitude_v2))
            angle_deg = degrees(angle_rad)

            angles.append(angle_deg)

        return angles

    def compute_area(self, shape_edges):
        if len(self.vertices) == 3:
            H=[]
            for i in self.vertices:
                H.append(i.y)
            H.sort(reverse=True)
            Height=H[0]
            for edge in shape_edges:
                Base = edge.start_point.compute_distance(edge.end_point)
                break
            print(f"El area es : {(Height * Base)/2}")
        elif len(self.vertices) == 4:
            E=[]
            for edge in shape_edges:
                E.append(edge.start_point.compute_distance(edge.end_point))
            Base=E[0]
            Height=E[1]
            print(f"El area es: {Base*Height}")
     
    def compute_perimeter(self, shape_edges):
        perimeter = 0
        for edge in shape_edges:
            perimeter += edge.start_point.compute_distance(edge.end_point)

        print(f"El perimetro es : {perimeter:.2f}" )

    def compute_type(self, valid_angles, list_edge):
        type = ()
        num_angles = 0
        for i in valid_angles:
            num_angles += 1
        if num_angles == 3:
            type = Triangle.compute_triangle(self, valid_angles)
        if num_angles == 4:
            type = Rectangle.compute_rectangle(self, list_edge)
        print(type)

            
        

# Clase Triangle para representar un triángulo
class Triangle(Shape):
    def __init__(self, inner_angles):
        self.inner_angles = inner_angles
    def compute_triangle(self, valid_angles):
        set_angle=0
        for i in set(valid_angles):
            set_angle+=1
            if i == 90:
                print(TriRectangle.triangle_rect(self))
        if set_angle == 1:
            return (Equilateral.triangle_equil(self))
        elif set_angle == 2:
            return (Isosceles.triangle_isos(self))
        elif set_angle == 3:
            return(Scalene.triangle_Scal(self))


class Isosceles(Triangle):
    def __init__(self, inner_angles):
        self.inner_angles =inner_angles

    def triangle_isos(self):
        return("El triangulo es isosceles")

class Equilateral(Triangle):
    def __init__(self, inner_angles):
        self.inner_angles =inner_angles

    def triangle_equil(self):
        return("El triangulo es equilatero")

class Scalene(Triangle):
    def __init__(self, inner_angles):
        self.inner_angles =inner_angles

    def triangle_Scal(self):
        return("El triangulo es escaleno")

class TriRectangle(Triangle):
    def __init__(self, inner_angles):
        self.inner_angles =inner_angles

    def triangle_rect(self):
        return("El triangulo es rectangulo")


# Clase Rectangle para representar un rectángulo
class Rectangle(Shape):
    def __init__(self, vertices):
        super().__init__(vertices)
    def compute_rectangle(self, list_edge):
        set_edge = 0
        for i in set(list_edge):
            set_edge += 1
        if set_edge == 1:
            return(Square.valid_square(self))
        elif set_edge == 2:
            return("La figura es especificamente un rectangulo")

# Clase Square para representar un cuadrado
class Square(Rectangle):
    def valid_square(self):
        return("La figura es un cuadrado")
