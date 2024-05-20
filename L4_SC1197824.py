# Parte 1
lista = [50, 75, 46, 22, 80, 65, 8]
def obtener_mayor(lista):
    mayor = lista[0]
    for lista in lista:
        if lista > mayor:
            mayor = lista 
    return mayor

def obtener_menor(lista):
    menor = lista[0]
    for lista in lista:
        if lista < menor:
            menor = lista
    return menor 

mayor_lista = obtener_mayor(lista)
menor_lista = obtener_menor(lista)
print("El mayor lista es:", mayor_lista)
print("El menor lista es:", menor_lista)

#Parte 2
abecedario = [chr(i) for i in range(ord('a'), ord('z') + 1)]
lista_filtrada = [letra for idx, letra in enumerate(abecedario) if (idx + 1) % 3 != 0]
print(lista_filtrada)

#Parte 3
Lista_palabras = ["manzana", "pera", "melocoton", "fresa", "melon", "piña"]
palabra_buscada = input("Introcude una palabra para buscar:")
conteo = Lista_palabras.count(palabra_buscada)
print("La palabra buscada", palabra_buscada, "aparece", conteo, "veces en la lista")

#Parte 4
import random
vector = [random.randint(1, 100) for _ in range(100)]
pares = [num for num in vector if num % 2 == 0]
impares = [num for num in vector if num % 2 != 0]
print("Números pares:")
print(pares)
print("Números impares:")
print(impares)