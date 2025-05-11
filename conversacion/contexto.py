class GestorContexto:
    def __init__(self, max_turnos=6):
        self.historial = []
        self.max_turnos = max_turnos

    def agregar_mensaje(self, rol, contenido):
        self.historial.append((rol, contenido))
        if len(self.historial) > self.max_turnos * 2:
            self.historial = self.historial[-self.max_turnos * 2:]

    def construir_prompt_gpt2(self):
        prompt = ""
        for rol, texto in self.historial:
            if rol == "usuario":
                prompt += f"User: {texto}\n"
            elif rol == "asistente":
                prompt += f"Assistant: {texto}\n"
        prompt += "Assistant: "
        return prompt
