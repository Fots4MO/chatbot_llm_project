from config.entorno import cargar_modelo
from chatbot.base import Chatbot

def ejecutar():
    print("🧪 Ejercicio 3: Chat con contexto (GPT2)\n")
    modelo, tokenizador = cargar_modelo()
    bot = Chatbot(modelo, tokenizador)

    mensajes = [
        "Hello!",
        "Can you tell me a joke?",
        "And a fun fact?",
        "Thanks, that's enough for today."
    ]

    for mensaje in mensajes:
        print(f"👤 Usuario: {mensaje}")
        respuesta = bot.responder(mensaje)
        print(f"🤖 Asistente: {respuesta}\n")
