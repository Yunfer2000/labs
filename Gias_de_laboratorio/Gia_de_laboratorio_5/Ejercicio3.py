# Listas de números
lista1 = list(range(1, 11))
lista2 = list(range(5, 16))
lista3 = list(range(10, 21))

# a. Convertir las listas en conjuntos
conjunto1 = set(lista1)
conjunto2 = set(lista2)
conjunto3 = set(lista3)

# b. Conjunto de números presentes en las tres listas
conjunto_interseccion = conjunto1 & conjunto2 & conjunto3

# c. Conjunto de números presentes en al menos una de las listas
conjunto_union = conjunto1 | conjunto2 | conjunto3

# d. Conjunto de números presentes en la primera lista pero no en la última
conjunto_diferencia = conjunto1 - conjunto3

# e. Convertir conjuntos en tuplas y sumar el primer y último elemento de cada tupla
tupla_interseccion = (list(conjunto_interseccion)[0], list(conjunto_interseccion)[-1])
tupla_union = (list(conjunto_union)[0], list(conjunto_union)[-1])
tupla_diferencia = (list(conjunto_diferencia)[0], list(conjunto_diferencia)[-1])

# Sumar el primer y último elemento de cada tupla
suma_interseccion = sum(tupla_interseccion)
suma_union = sum(tupla_union)
suma_diferencia = sum(tupla_diferencia)

# Imprimir resultados
print("Conjunto de números presentes en las tres listas:", conjunto_interseccion)
print("Conjunto de números presentes en al menos una de las listas:", conjunto_union)
print("Conjunto de números presentes en la primera lista pero no en la última:", conjunto_diferencia)
print("Suma del primer y último elemento de la tupla de intersección:", suma_interseccion)
print("Suma del primer y último elemento de la tupla de unión:", suma_union)
print("Suma del primer y último elemento de la tupla de diferencia:", suma_diferencia)