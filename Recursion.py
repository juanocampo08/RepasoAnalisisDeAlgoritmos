"""## Solución Ejercicio 1

def factorial(numero : int):
    if (numero == 0) or (numero == 1):
        return 1

    resultado = numero * factorial(numero - 1) 

    return resultado

print(factorial(4))


## Solución Ejercicio 2

def contar_elementos_lista(lista: list):
    if len(lista) == 0:
        return 0
    print(lista)
    return 1 + contar_elementos_lista(lista[:-1:1])

numeros = [0, 1, [], {}, 5, (), 7, 8, 9]
print(contar_elementos_lista(numeros))


## Solución Ejercicio 3

def multiplicar_lista(lista:list):
    if len(lista) == 0:
        return 1
    
    return lista[-1] * multiplicar_lista(lista[:-1:1])


lista = [1, 2, 3, 4]
print(multiplicar_lista(lista))


## Solución Ejercicio 4

def obtener_ultimo(lista: list):
    if len(lista) == 1:
        return lista[0]
    
    return obtener_ultimo(lista[1:])

lista = [1, 2, 3, []]
print(obtener_ultimo(lista))


## Solución Ejercicio 5

def sumar_pares(numero: int):
    if numero == 0:
        return 0
    

    if (numero % 2) == 0:
        return numero + sumar_pares(numero - 2)
    else:
        return sumar_pares(numero - 1)


print(sumar_pares(8))


## Solución Ejercicio 6

def contar_vocales(cadena: str):
    vocales = "aeiouAEIOU"
    if len(cadena) == 0:
        return 0
    print(cadena)
    
    if cadena[-1] in vocales:
        return 1 + contar_vocales(cadena[:-1])
    else: 
        return contar_vocales(cadena[:-1])
    
print(contar_vocales("holA"))
print(contar_vocales("python"))
print(contar_vocales("murcielago"))

"""
print("=" * 100)

## Solución Ejercicio 1

"""def contar_elementos_cola(lista: list, contador: int = 0):
    if len(lista) == contador:
        return contador
    
    return contar_elementos_cola(lista, contador + 1)

lista = []
print(contar_elementos_cola(lista))"""

## Solución Ejercicio 2

"""def factorial_cola(numero:int , resultado: int = 1):
    if numero == 0 or numero == 1:
        return resultado
    
    resultado *= numero
    return factorial_cola(numero - 1, resultado)

print(factorial_cola(5))

"""


## Solución Ejercicio 3

"""def sumar_lista_cola(lista: list, indice: int = 0, suma: int = 0):
    if len(lista) == indice:
        return suma
    suma += lista[indice] 
    return sumar_lista_cola(lista, indice + 1, suma)

lista = [1, 2, 3, 4]
print(sumar_lista_cola(lista))"""



## Solución Ejercicio 4

"""def invertir_cola(cadena: str, acumulacion: str = ""):
    if len(cadena) == 0:
        return acumulacion

    acumulacion += cadena[-1]
    return invertir_cola(cadena[:-1], acumulacion)

print(invertir_cola("hola"))"""

## Solución Ejercicio 5

"""def potencia_cola(base: int, exponente: int, acumulador = 1):
    if exponente == 0:
        return acumulador

    acumulador *= base

    return potencia_cola(base, exponente - 1, acumulador)

print(potencia_cola(2, 4))
"""