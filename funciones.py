import random

def funcion_sumar(a, b):
    resultado = a + b
    return resultado
token = "YOUR TOKEN"

# Juego de Piedra, Papel o Tijera

def jugar_ppt(eleccion_usuario):
    opciones = ['piedra', 'papel', 'tijera']
    eleccion_bot = random.choice(opciones)

    if eleccion_usuario == eleccion_bot:
        resultado = "Empate"
    elif (eleccion_usuario == "piedra" and eleccion_bot == "tijera") or \
         (eleccion_usuario == "papel" and eleccion_bot == "piedra") or \
         (eleccion_usuario == "tijera" and eleccion_bot == "papel"):
        resultado = "¡Ganaste!"
    else:
        resultado = "Perdiste..."

    return f"Tú elegiste: {eleccion_usuario} | Bot eligió: {eleccion_bot} → {resultado}"

# Adivinar el número

numeros_secretos = {}

# Diccionario para guardar el estado del juego por usuario
juegos_adivinanza = {}

# Configuración de dificultad
dificultades = {
    "facil": {"intentos": None, "min": 1, "max": 10},
    "normal": {"intentos": 30, "min": 1, "max": 50},
    "dificil": {"intentos": 15, "min": 1, "max": 100},
    "extremo": {"intentos": 6, "min": 1, "max": 500},
    "casi_imposible": {"intentos": 3, "min": 1, "max": 1000},
}

def iniciar_adivinanza_dificultad(user_id, dificultad="facil"):
    dificultad = dificultad.lower().replace("-", "_")

    if dificultad not in dificultades:
        return "Esa dificultad no existe. Opciones: fácil, normal, difícil, extremo, casi_imposible."

    config = dificultades[dificultad]
    numero = random.randint(config["min"], config["max"])

    juegos_adivinanza[user_id] = {
        "numero": numero,
        "intentos_restantes": config["intentos"],
        "min": config["min"],
        "max": config["max"],
        "dificultad": dificultad
    }

    return f"🎯 Dificultad: **{dificultad.upper()}**. Adivina un número entre {config['min']} y {config['max']}. ¡Buena suerte!"

def verificar_adivinanza_dificultad(user_id, intento):
    juego = juegos_adivinanza.get(user_id)

    if not juego:
        return "No has iniciado un juego aún. Usa `$adivina <dificultad>`."

    secreto = juego["numero"]
    intentos = juego["intentos_restantes"]
    diferencia = abs(intento - secreto)

    # Determinar pistas según la diferencia
    if diferencia == 0:
        del juegos_adivinanza[user_id]
        return "🎉 ¡Correcto! Adivinaste el número."

    # Intentos finitos
    if intentos is not None:
        juego["intentos_restantes"] -= 1
        if juego["intentos_restantes"] <= 0:
            del juegos_adivinanza[user_id]
            return f"💀 ¡Perdiste! El número era {secreto}."

    # Dar pista según la dificultad
    pista = ""
    if diferencia >= 100:
        pista = "Estás muuuy lejos."
    elif diferencia >= 50:
        pista = "Estás lejos."
    elif diferencia >= 20:
        pista = "Te estás acercando..."
    elif diferencia >= 10:
        pista = "¡Muy cerca!"
    elif diferencia < 10:
        pista = "🔥 ¡A punto!"

    direccion = "mayor" if intento < secreto else "menor"

    mensaje = f"❌ No es {intento}. Prueba un número {direccion}. {pista}"
    if intentos is not None:
        mensaje += f" | Intentos restantes: {juego['intentos_restantes']}"
    return mensaje

# Dado

def lanzar_dado(caras=6, cantidad=1):
    """Lanza uno o varios dados con N caras. Devuelve la lista de resultados y la suma."""
    if caras < 2 or cantidad < 1:
        return "Error: mínimo 1 dado y al menos 2 caras."

    resultados = [random.randint(1, caras) for _ in range(cantidad)]
    total = sum(resultados)
    return resultados, total
