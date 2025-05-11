from config.entorno import cargar_modelo, verificar_dispositivo
from procesamiento.entrada import preprocesar_entrada
from procesamiento.generacion import generar_respuesta

def ejecutar():
    """
    Ejercicio 1: Configuración del entorno y prueba de carga del modelo.
    """
    print("🧪 Ejercicio 1: Carga de modelo base\n")

    # TODO: Verificar el dispositivo disponible
    dispositivo = verificar_dispositivo()
    print(f"Utilizando dispositivo: {dispositivo}")

    # TODO: Cargar un modelo pequeño adecuado para chatbots
    modelo, tokenizador = cargar_modelo("GPT2")

    # TODO: Realizar una prueba simple de generación de texto
    prompt = "How are you?"
    entrada = preprocesar_entrada(prompt, tokenizador)
    respuesta = generar_respuesta(modelo, entrada, tokenizador)

    print(f"\n🤖 Respuesta: {respuesta}")
