def es_bisiesto ():
    año = int(input("Ingrese el año: "))
    if año % 4 == 0 and (año % 100 !=0 or año % 400 == 0):
        return ("Este año es bisiesto")
    else:
        return ("El año no es bisiesto")
print (es_bisiesto())