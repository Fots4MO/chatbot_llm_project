import torch

def preprocesar_entrada(texto, tokenizador, max_length=512):
    dispositivo = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    entrada = tokenizador(texto, return_tensors="pt", max_length=max_length, truncation=True, padding=True)
    return {k: v.to(dispositivo) for k, v in entrada.items()}


def crear_prompt_sistema(instrucciones, mensaje_usuario):
    """
    Crea un prompt de sistema para dar instrucciones al modelo.
    
    Args:
        instrucciones (str): Instrucciones para el chatbot
        mensaje_usuario (str): Entrada del usuario
    
    Returns:
        str: Prompt combinado
    """
    return f"{instrucciones}\nUser: {mensaje_usuario}\nAssistant:"
