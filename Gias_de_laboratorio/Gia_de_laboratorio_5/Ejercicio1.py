edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# a. Ordena la lista y encuentra la edad mínima y máxima
edades_ordenadas = sorted(edades)
edad_minima = edades_ordenadas[0]
edad_maxima = edades_ordenadas[-1]
print("Edad mínima:", edad_minima)
print("Edad máxima:", edad_maxima)

# b. Añade de nuevo la edad mínima y máxima a la lista
edades_ordenadas.append(edad_minima)
edades_ordenadas.append(edad_maxima)
print("Lista con edades y extremos añadidos:", edades_ordenadas)

# c. Encuentra la edad mediana
mediana = edades_ordenadas[len(edades_ordenadas) // 2] if len(edades_ordenadas) % 2 == 1 else (edades_ordenadas[len(edades_ordenadas) // 2 - 1] + edades_ordenadas[len(edades_ordenadas) // 2]) / 2
print("Edad mediana:", mediana)

# d. Encuentra la edad promedio
promedio = sum(edades_ordenadas) / len(edades_ordenadas)
print("Edad promedio:", promedio)

# e. Encuentra el rango de las edades
rango_edades = edad_maxima - edad_minima
print("Rango de edades:", rango_edades)

# f. Compara el valor de (mínimo - promedio) y (máximo - promedio), usa el método abs()
diferencia_minimo = abs(edad_minima - promedio)
diferencia_maximo = abs(edad_maxima - promedio)
print("Diferencia entre mínimo y promedio:", diferencia_minimo)
print("Diferencia entre máximo y promedio:", diferencia_maximo)