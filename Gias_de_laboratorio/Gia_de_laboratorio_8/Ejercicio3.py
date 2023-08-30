import random
import string
def generar_contraseña_segura(longitud):
    caracteres = string.ascii_letters + string.digits + "!@#$%."
    while True:
        contraseña = []
        contraseña.append(random.choice(string.ascii_uppercase))
        contraseña.append(random.choice(string.ascii_lowercase))
        contraseña.append(random.choice(string.digits))
        contraseña.append(random.choice("!@#$%."))
        for _ in range(longitud - 4):
            contraseña.append(random.choice(caracteres))
        random.shuffle(contraseña)
        contraseña_final = ''.join(contraseña)
        if (any(c.isupper() for c in contraseña_final) and
            any(c.islower() for c in contraseña_final) and
            any(c.isdigit() for c in contraseña_final) and
            any(c in "!@#$%." for c in contraseña_final)):
            return contraseña_final
while True:
    try:
        longitud_deseada = int(input("Ingrese la longitud deseada de la contraseña: "))
        if longitud_deseada < 8:
            print("La longitud mínima debe ser 8 caracteres.")
        else:
            break
    except ValueError:
        print("Ingrese un número válido.")
contraseña_generada = generar_contraseña_segura(longitud_deseada)
print("Contraseña generada:", contraseña_generada)