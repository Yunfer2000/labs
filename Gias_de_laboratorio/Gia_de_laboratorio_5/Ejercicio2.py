frase = "Soy profesor y me encanta inspirar y enseñar a la gente"

# Divide la frase en palabras utilizando el método split
palabras = frase.split()

# Convierte la lista de palabras en un conjunto para obtener las palabras únicas
palabras_unicas = set(palabras)

# Cuenta la cantidad de palabras únicas
cantidad_palabras_unicas = len(palabras_unicas)
print(palabras_unicas)
print("Cantidad de palabras únicas:", cantidad_palabras_unicas)