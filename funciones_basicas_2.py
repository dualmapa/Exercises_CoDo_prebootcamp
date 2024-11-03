# -*- coding: utf-8 -*-
"""funciones_basicas_2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1S56i3AckJ3Wc6icOtwmbB1TzVpbK_xhM

# Funciones básicas (Práctica)
"""

#1. Multiplica por 2: multiplica_por_2(5) debe regresar [0, 2, 4, 6, 7, 10]
def multiplica_por_2(n):
  resultado = []
  i = 0
  while i <= n:
    resultado.append(i*2)
    i += 1
  return resultado

multiplica_por_2(10) #Se debe aplicar print dentro de un entorno de desarrollo, de resto no se mostrará en pantalla

#2. Suma y resta: Ejemplo: suma_y_resta([5, 4]) debe de imprimir 9 y regresar 1
def suma_y_resta(a, b):
    suma = a + b
    resta = a - b
    print(suma)
    return resta

resultado = suma_y_resta(5,4)
print(resultado)

#3. Sumatoria menos longitud: Ejemplo: sumatoria_menos_longitud([1, 2, 3, 4]) debe devolver 6 (sumatoria de números: 10 – longitud: 4)
def sum_menos_len(n):
  sumatoria = sum(n)
  longitud = len(n)
  resultado = sumatoria - longitud
  return resultado

a = (1,2,3,4)

print(sum_menos_len(a))

#4. Valores multiplicados por el segundo: escribe una función que reciba una lista y crea una nueva lista con todos los valores multiplicados por el segundo número. Imprime la longitud de la lista y regresa la nueva lista. Si la lista tiene menos de 2 elementos, haz que la función regrese una lista vacía.
#Ejemplo: valores_multiplicados_segundo([1, 3, 5, 7]) debe imprimir 4 y devolver [3, 9, 15, 21]
#Ejemplo: valores_multiplicados_segundo([1]) debe imprimir 1 y devolver [ ]

def valores_multiplicados_segundo(numeros):
    # Verificar si la lista tiene menos de 2 elementos
    if len(numeros) < 2:
        return []  # Regresar lista vacía si hay menos de 2 elementos

    # Obtener el segundo número de la lista
    segundo_numero = numeros[1]

    # Crear la nueva lista con los valores multiplicados por el segundo número
    nueva_lista = [numero * segundo_numero for numero in numeros]

    # Imprimir la longitud de la nueva lista
    print(len(nueva_lista))

    # Regresar la nueva lista
    return nueva_lista

# Ejemplo de uso
resultado1 = valores_multiplicados_segundo([1, 3, 5, 7])
print(resultado1)  # Debe imprimir 4 y devolver [3, 9, 15, 21]

resultado2 = valores_multiplicados_segundo([1])
print(resultado2)  # Debe imprimir 1 y devolver []

#5. Valor multiplado y longitud: escribe una función que reciba dos números enteros: valor y longitud. La función debe crear y regresar una lista cuyo tamaño sea igual a la longitud recibida y los valores sean igual a la longitud multiplicada por el valor dado.
#Ejemplo: valor_multiplicado_longitud(5, 2) regresa [10, 10]
#Ejemplo: valor_multiplicado_longitud(7, 5) regresa [35, 35, 35, 35, 35]

def valor_multiplicado_longitud(valor, longitud):
    # Crear la lista usando una comprensión de lista
    lista = [valor * longitud] * longitud
    return lista

# Ejemplos de uso
print(valor_multiplicado_longitud(5, 2))  # Debe regresar [10, 10]
print(valor_multiplicado_longitud(7, 5))  # Debe regresar [35, 35, 35, 35, 35]
