import geometric_shapes.point as point
import geometric_shapes.shape as Tri
import geometric_shapes.shape as Squa



if __name__ == "__main__":
    try:
        triangle_vertices = [point.Point(0, 0), point.Point(4, 0), point.Point(0, 5)]
        triangle = Tri.Shape(triangle_vertices)

        angle_validation =0
        validated_angles =[]
        for i in triangle.inner_angles:
            angle_validation += round(i)
            validated_angles.append(round(i))
        if angle_validation >= 180:
            print("Ángulos internos del triángulo redondeados:", validated_angles)
            print("Longitudes de los lados del triángulo:")
            list_edge=[]
            for edge in triangle.edges:
                print(f"{edge.start_point.compute_distance(edge.end_point):.2f}")
                list_edge.append(edge.start_point.compute_distance(edge.end_point))

            triangle.compute_perimeter(triangle.edges)
            triangle.compute_area(triangle.edges)
            triangle.compute_type(validated_angles, list_edge)
            
            
            print("Es regular?", triangle.regular)
        else:
            print("no es un triangulo??")
    except ZeroDivisionError:
        print("Error: no se puede dividir entre 0")
        #El error aparece cuando hay dos puntos consecutivos con las mismas coordenadas, el codigo busca una el angulo interno de tres puntos entonces busca dos magnitudes, pero si una magnitud es 0 entonces falla con el producto punto para sacar el cos del angulo
    except TypeError:
        print("Error: te falto poner datos o el que pusiste no es computable")
        #El error aparece cuando se meten datos que no se pueden computar ya sea porque es un str y no se suma con un numero, o tambien cuandl hace falta datos por el formato (X, Y), si se pone datos de mas, aparece que hace falta agregar un tercer slot
    except ModuleNotFoundError:
        print("Error: no se pudo importar un modulo")
        #El error aparece por fallo del codigo, no de los datos que ingreso el usuario, ya sea porque el modulo a importar no existe o no se escribio bien
    except NameError:
         print("Error: no se pudo definió bien una variable")
        #El error aparece cuando no se especifica ya sea por un caracter o demas, entonces no se define el nombre

    try:
        square_vertices = [point.Point(0, "0"), point.Point(0, 2), point.Point(1, 1), point.Point(1, 0)]
        square = Squa.Shape(square_vertices)

        angle_validation =0
        validated_angles=[]
        for i in square.inner_angles:
            angle_validation += i
            validated_angles.append(round(i))
        if angle_validation == 360:  
            print("Ángulos internos del cuadrado:", validated_angles)
            print("Longitudes de los lados del cuadrado:")
            list_edge=[]
            for edge in square.edges:
                print(f"{edge.start_point.compute_distance(edge.end_point):.2f}")
                list_edge.append(edge.start_point.compute_distance(edge.end_point))
            square.compute_perimeter(square.edges)
            square.compute_area(square.edges)
            square.compute_type(validated_angles, list_edge)

            print("Es regular?", square.regular)
        else: 
            print("no es un cuadrado")
    except ZeroDivisionError:
        print("Error: no se puede dividir entre 0")
    except TypeError:
        print("Error: te falto poner datos o el que pusiste no es computable")
        

  