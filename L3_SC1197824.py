#Ejercicio 1
def tipo_triangulo(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"

def main():
    lado1 = float(input("Ingrese la longitud del primer lado: "))
    lado2 = float(input("Ingrese la longitud del segundo lado: "))
    lado3 = float(input("Ingrese la longitud del tercer lado: "))

    tipo = tipo_triangulo(lado1, lado2, lado3)
    print("El triángulo es:", tipo)

if __name__ == "__main__":
    main()

#Ejercicio 2
import math

# Función para obtener el perímetro de la circunferencia
def obtener_perimetro(radio):
    
   
    return 2 * math.pi * radio

# Función para obtener el área de la circunferencia
def obtener_area(radio):
    
    ret
    return math.pi * radio ** 2

# Función para obtener el volumen de la esfera
def obtener_volumen(radio):
    
   
    return (4/3) * math.pi * radio ** 3

def main():
    radio = ##?
    radio = f

    ra #?
float(input("Ingrese el radio del círculo: "))
    
    
    
  
# Calculando el perímetro
    perimetro = obtener_perimetro(radio)
    
    perimetro = obtener_perimetro(radio)
    pr #?

    perimetro = obtener_perimetro(radio

    perimetro = obtener_perimet

    perimetro = obtener

    perimetro = o

    perimet #?

    
print("El perímetro de la circunferencia es:", perimetro)
    
    
    
   
# Calculando el área
    area = obtener_area(radio)
    
    area = obtener_area(radio)
    priv#?

    area = obtener_area(radio)

    area = obtener_area(

    area = obten

    area #?

 
print("El área de la circunferencia es:", area)
    
    
    
# Calculando el volumen
    volumen = obtener_volumen(radio)
    
    volumen = obtener_volumen(radio)
    

    volumen = obtener_volumen(rad

    volumen = obtener_vol

    volumen = obte #?

    volumen 

    vo
print("El volumen de la esfera es:", volumen)

if __name__ == "__main__":
    main()

    main
#Ejercicio 3
def imprimir_nombre_mes(numero):

    meses = {
1: "Enero",
2:"Febrero",
       3: "Marzo",
       4: "Abril",
       5: "Mayo",
       6: "Junio",
7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
12: "Diciembre"
}
if numero in meses:

print(meses[numero])
    else:
print("Numero nno valido. Debe estar en el rango del 1 al 12.")

def main():
    numero = 
int(input("Ingrese un numero del 1 al 12:"))
    imprimir_nombre_mes(numero)

if__name__=="__main__":
main( )
