import requests

BASE_URL = "http://localhost:5000"

# Paso 1: Menú de opciones
print("=== JUEGO DEL AHORCADO ===")
print("1. Palabra aleatoria")
print("2. Elegir una categoría")
opcion = input("Selecciona una opción (1 o 2): ")

palabra = ""

if opcion == "1":
    # Palabra aleatoria
    r = requests.get(f"{BASE_URL}/palabras?cantidad=1")
    palabra = r.json()[0]["palabra"].lower()

elif opcion == "2":
    # Mostrar categorías disponibles
    r = requests.get(f"{BASE_URL}/categorias")
    categorias = r.json()

    print("\nCategorías disponibles:")
    for i, cat in enumerate(categorias):
        print(f"{i+1}. {cat}")

    seleccion = int(input("Selecciona una categoría: "))
    categoria_elegida = categorias[seleccion - 1]

    # Obtener palabras por categoría
    r = requests.get(f"{BASE_URL}/palabras/categoria?tipo={categoria_elegida}")
    palabras_categoria = r.json()["palabras"]

    # Elegir una palabra al azar entre esas
    import random
    palabra = random.choice(palabras_categoria).lower()

else:
    print("Opción no válida. Saliendo...")
    exit()

# Ahorcado
letras_adivinadas = []
letras_incorrectas = []
intentos_maximos = 6

print("\n¡Comienza el juego del ahorcado!\n")

while True:
    progreso = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            progreso += letra
        else:
            progreso += "*"

    print("\nPalabra:", progreso)
    print("Letras incorrectas:", ", ".join(letras_incorrectas))
    print("Te quedan", intentos_maximos - len(letras_incorrectas), "intentos")

    if progreso == palabra:
        print("\n¡Felicidades! ¡Has adivinado la palabra!")
        break

    if len(letras_incorrectas) >= intentos_maximos:
        print("\nLo siento, te quedaste sin intentos. La palabra era:", palabra)
        break

    letra = input("Ingresa una letra: ").lower()

    if len(letra) != 1 or not letra.isalpha():
        print("Por favor ingresa solo una letra.")
        continue

    if letra in letras_adivinadas or letra in letras_incorrectas:
        print("Ya has intentado con esa letra.")
        continue

    if letra in palabra:
        letras_adivinadas.append(letra)
    else:
        letras_incorrectas.append(letra)
