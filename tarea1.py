#Andrés Felipe Chamorro Pérez

from itertools import product

K = 3
M = 1000

Lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Lista2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
Lista3 = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

listas = [Lista1, Lista2, Lista3]

max_valor = 0
mejor_combinacion = None

for combinacion in product(*listas):
    suma_cuadrados = sum(x**2 for x in combinacion)
    resultado = suma_cuadrados % M
    
    if resultado > max_valor:
        max_valor = resultado
        mejor_combinacion = combinacion

print("Mejor combinación:", mejor_combinacion)
print("Suma de cuadrados:", sum(x**2 for x in mejor_combinacion))
print(f"Resultado con módulo {M}:", max_valor)
