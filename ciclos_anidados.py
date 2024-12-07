#ciclos anidados...

# es un ciclo que suele contener otros ciclos, es decir, hay uno externo y hay uno interno (esto no implica que solo se puedan anidar 2) se usan para procesar datos de diferentes niveles o dimensiones.

# for papa in range(3):
#     for zanahoria in range(99):
#         print(f"i={papa}, j={zanahoria}")


#para que se aplica...
#procesar matrices, generar patrones visuales, resolver problemas jerarquicos como tableros o graficos.

# concepto clave.
#por cada iteracion del ciclo externo, el ciclo interno se ejecuyta completamente.


# Procesamientro de matrices con ciclos anidados.

#Matriz en IT:
# es una lista [], donde cada elemento es una lista o una sublista, estas van a representar una fila.

#Ejemplo 1: Imprimir una matriz de forma que quede representada como su representacion matematica.

# matriz = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# for fila in matriz:
#     for elemento in fila:
#         print(elemento, end=" ")
#     print()
# # 1 2 3
# # 4 5 6
# # 7 8 9

# suma = 0

# for fila in matriz:
#     for elemento in fila:
#         suma += elemento
#     print(suma)

# print(f"suma total: {suma}")

# contador_pares = 0

# for fila in matriz:
#     for elemento in fila:
#         if elemento % 2 == 0:
#             contador_pares += 1

# print(f"hay {contador_pares} numeros pares en la matriz")
