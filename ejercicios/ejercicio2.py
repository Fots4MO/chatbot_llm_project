from config.entorno import cargar_modelo
from procesamiento.entrada import crear_prompt_sistema, preprocesar_entrada
from procesamiento.generacion import generar_respuesta

def ejecutar():
    """
    Ejercicio 2: Procesamiento de entrada y generación de respuestas.
    """
    print("🧪 Ejercicio 2: Procesamiento de entrada y generación de respuesta\n")

    # Cargar modelo y tokenizador
    modelo, tokenizador = cargar_modelo("GPT2")

    # TODO: Crear un prompt de sistema para definir la personalidad del chatbot
    instrucciones = "You are a helpful assistant. Always answer in English."
    entrada_usuario = "How are you?"
    prompt = crear_prompt_sistema(instrucciones, entrada_usuario)

    # TODO: Procesar la entrada
    entrada = preprocesar_entrada(prompt, tokenizador)

    # TODO: Generar y mostrar la respuesta
    respuesta = generar_respuesta(modelo, entrada, tokenizador)
    print(f"🤖 {respuesta}")
