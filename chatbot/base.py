from procesamiento.entrada import preprocesar_entrada
from procesamiento.generacion import generar_respuesta
from conversacion.contexto import GestorContexto

class Chatbot:
    def __init__(self, modelo, tokenizador):
        self.modelo = modelo
        self.tokenizador = tokenizador
        self.contexto = GestorContexto()

    def responder(self, mensaje_usuario, parametros=None):
        self.contexto.agregar_mensaje("usuario", mensaje_usuario)
        prompt = self.contexto.construir_prompt_gpt2()
        entrada = preprocesar_entrada(prompt, self.tokenizador, max_length=512)
        respuesta = generar_respuesta(self.modelo, entrada, self.tokenizador, parametros)
        self.contexto.agregar_mensaje("asistente", respuesta.strip())
        return respuesta.strip()
