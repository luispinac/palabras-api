import requests

# Obtener una palabra aleatoria desde tu API local
try:
    respuesta = requests.get("http://localhost:5000/palabras?cantidad=1")
    datos = respuesta.json()
    palabra = datos[0]["palabra"].lower()
except Exception as e:
    print("No se pudo obtener una palabra desde la API:", e)
    palabra = "fallback"  # Palabra de respaldo si la API falla

# Inicializar variables del juego
letras_adivinadas = []
letras_incorrectas = []
intentos_maximos = 6

print("Bienvenido al juego del ahorcado conectado a una API local.\n")

while True:
    # Mostrar progreso con asteriscos
    progreso = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            progreso += letra
        else:
            progreso += "*"

    print("\nPalabra:", progreso)
    print("Letras incorrectas:", ", ".join(letras_incorrectas))
    print("Te quedan", intentos_maximos - len(letras_incorrectas), "intentos")

    # Condiciones de fin de juego
    if progreso == palabra:
        print("\n¡Felicidades! ¡Has adivinado la palabra!")
        break

    if len(letras_incorrectas) >= intentos_maximos:
        print("\nLo siento, te quedaste sin intentos. La palabra era:", palabra)
        break

    # Entrada del jugador
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
