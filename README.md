# Ejercicios de recursión.


## Ejercicios de recursion sin cola


### *Ejercicio 1*

    Calcula n! = n × (n-1) × (n-2) × ... × 1
    
    Pensamiento Recursivo:
    5! = 5 × 4! 
    4! = 4 × 3!
    3! = 3 × 2!
    2! = 2 × 1!
    1! = 1  ← CASO BASE

### *Ejercicio 2*

    Cuenta cuántos elementos hay en una lista
    
    Ejemplo: 
    contar_elementos([1, 2, 3, 4]) → 4
    contar_elementos([]) → 0
    
    Pistas:
    - Caso base: ¿Qué pasa con una lista vacía?
    - Caso recursivo: 1 elemento + contar el resto

### *Ejercicio 3*


    Multiplica todos los elementos de una lista
    
    Ejemplo: 
    multiplicar_lista([2, 3, 4]) → 24
    multiplicar_lista([5]) → 5
    
    Pistas:
    - Caso base: lista vacía → ¿cuál es el elemento neutro de la multiplicación?
    - Caso recursivo: primer elemento × multiplicar(resto)


### *Ejercicio 4*

Retorna el último elemento de una lista
    
    Ejemplo:
    obtener_ultimo([1, 2, 3, 4]) → 4
    obtener_ultimo([100]) → 100
    
    Pistas:
    - Caso base: lista con un solo elemento
    - Caso recursivo: ignorar el primero, buscar en el resto

### *Ejercicio 5*

Suma todos los números pares desde 0 hasta n
    
    Ejemplo:
    sumar_pares(6) → 0 + 2 + 4 + 6 = 12
    sumar_pares(5) → 0 + 2 + 4 = 6
    
    Pistas:
    - Caso base: n <= 0
    - Caso recursivo: si n es par, súmalo y baja de 2 en 2
    - Si n es impar, baja 1 y continúa
    
### *Ejercicio 6*

Cuenta cuántas vocales hay en un texto
    
    Ejemplo: 
    contar_vocales("hola") → 2
    contar_vocales("python") → 1
    
    Pistas: 
    - Caso base: string vacío
    - Define vocales = 'aeiouAEIOU'
    - Caso recursivo: si primera letra es vocal, suma 1
    - Siempre procesa el resto del texto

## Ejercicios de recursion con cola

### *Ejercicio 1*

    Cuenta elementos usando tail recursion
    
    Ejemplo:
    contar_elementos_cola([1, 2, 3]) → 3
    
    Pistas:
    - Caso base: lista vacía → retorna acumulador
    - Caso recursivo: incrementa acumulador y procesa resto
    - ¡La llamada recursiva debe ser lo ÚLTIMO!

### *Ejercicio 2*

  Calcula n! con tail recursion
    
    Ejemplo: 
    factorial_cola(5) → 120
    factorial_cola(3) → 6
    
    Pistas:
    - Caso base: n == 0 o n == 1 → retorna acumulador
    - Caso recursivo: multiplica n con acumulador
    - Reduce n en cada llamada

### *Ejercicio 3*

Suma todos los elementos de una lista con tail recursion
    
    Ejemplo:
    suma_lista_cola([1, 2, 3, 4]) → 10
    
    Pistas: 
    - Caso base: lista vacía
    - Caso recursivo: suma primer elemento al acumulador
    - Procesa el resto de la lista

### *Ejercicio 4*

    Invierte un string usando tail recursion
    
    Ejemplo:
    invertir_cola("hola") → "aloh"
    invertir_cola("python") → "nohtyp"
    
    Pistas: 
    - Caso base: texto vacío → retorna acumulador
    - Caso recursivo:  agrega primer carácter AL INICIO del acumulador
    - Procesa el resto del texto

### *Ejercicio 5*

Calcula base^exponente con tail recursion
    
    Ejemplo: 
    potencia_cola(2, 5) → 32
    potencia_cola(3, 3) → 27
    
    Pistas: 
    - Caso base: exponente == 0 → retorna acumulador
    - Caso recursivo: multiplica base con acumulador
    - Reduce exponente en cada llamada


