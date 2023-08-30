import string
import random

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars):
    if length <= 0:
        raise ValueError("La longitud debe ser un número positivo.")
    
    character_pool = ""
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_special_chars:
        character_pool += string.punctuation

    if not character_pool:
        raise ValueError("Debes seleccionar al menos un tipo de carácter.")
    
    generate_character = lambda: random.choice(character_pool)
    password = "".join(generate_character() for _ in range(length))
    return password

def main():
    try:
        length = int(input("Longitud de la contraseña: "))
        use_uppercase = input("Incluir letras mayúsculas (S/N): ").upper() == "S"
        use_lowercase = input("Incluir letras minúsculas (S/N): ").upper() == "S"
        use_digits = input("Incluir números (S/N): ").upper() == "S"
        use_special_chars = input("Incluir caracteres especiales (S/N): ").upper() == "S"

        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars)
        print(f"Contraseña generada: {password}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()