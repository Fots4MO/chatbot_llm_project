from config.entorno import cargar_modelo
from chatbot.base import Chatbot
from despliegue.interfaz_web import crear_interfaz_web

def ejecutar():
    """
    Ejercicio 5: Personalización del chatbot y despliegue con Gradio.
    """
    print("🌐 Ejercicio 5: Iniciando interfaz web con Gradio...\n")

    # TODO: Cargar el modelo base o personalizado
    modelo, tokenizador = cargar_modelo("GPT2")

    # TODO: Crear instancia del chatbot
    instrucciones = "You are a friendly assistant. Answer in natural and helpful English."
    bot = Chatbot(modelo, tokenizador, instrucciones_sistema=instrucciones)

    # TODO: Crear y lanzar la interfaz web
    interfaz = crear_interfaz_web(bot)
    interfaz.launch(share=True) 
