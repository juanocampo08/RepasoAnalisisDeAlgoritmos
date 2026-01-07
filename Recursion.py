## Solución Ejercicio 1

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

    
    
