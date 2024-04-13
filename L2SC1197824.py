#Ejercicio laboratorio 2
#parte 1
def contar_pares_impares(numero):
    pares = 0 
    impares = 0
    for i in range(1, numero + 1):
        if i % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares
numero = int(input(" Ingrese un numero entero positivo:"))
if numero <= 0
    print("Ingresar un numero entero positivo.")
else: 
    cantidad_pares, cantidad_impares = contar_pares_impares(numero)
    print("Cantidad de numeros pares:", cantidad_pares)
    print("Cantidad de numeros impares:", cantidad_impares)

#parte 2
inicio= int(input("Ingrese un numero inicial que sea par del rango:"))
fin= int(input("Ingrese un numero final que sea para del rango:"))

suma_pares= 0

for num in range(inicio, fin + 1):
    if num % 2 == 0:
        suma_pares += num

print("La suma de todos numeros pares en el rango es:", suma_pares)

#parte 3
numero = int(input("Ingrese un numero para mostrar su tabla de multplicar:"))

print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    resultado  = numero * i 
    print(f"{numero}"x {i} = {resultado})

#parte 4
for num in range(1, 51):
    if num % 3 == 0 and num % 5 == 0: 
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)   

#parte 5
numero = int(input("Ingrese un numero"))

print(f"Los divisores de {numero} son: ")

for i in range(1, numero + 1):
    if numero %  i == 0:
        print(i)