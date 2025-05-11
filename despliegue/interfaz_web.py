import gradio as gr
from peft import LoraConfig, get_peft_model, TaskType
from transformers import AutoTokenizer, AutoModelForCausalLM

def configurar_peft(modelo, r=8, lora_alpha=32):
    """
    Configura el modelo para fine-tuning con PEFT/LoRA.
    """
    lora_config = LoraConfig(
        r=r,
        lora_alpha=lora_alpha,
        target_modules=["q_proj", "v_proj"],  # ajustar según arquitectura
        lora_dropout=0.1,
        bias="none",
        task_type=TaskType.CAUSAL_LM
    )
    modelo_peft = get_peft_model(modelo, lora_config)
    return modelo_peft

def guardar_modelo(modelo, tokenizador, ruta):
    """
    Guarda el modelo y tokenizador en una ruta específica.
    """
    modelo.save_pretrained(ruta)
    tokenizador.save_pretrained(ruta)

def cargar_modelo_personalizado(ruta):
    """
    Carga un modelo personalizado desde una ruta específica.
    """
    modelo = AutoModelForCausalLM.from_pretrained(ruta)
    tokenizador = AutoTokenizer.from_pretrained(ruta)
    return modelo.eval(), tokenizador

def crear_interfaz_web(chatbot):
    """
    Crea una interfaz web simple para el chatbot usando Gradio.
    """
    def responder_interfaz(input_text):
        return chatbot.responder(input_text)

    interfaz = gr.Interface(
        fn=responder_interfaz,
        inputs=gr.Textbox(label="Tu mensaje"),
        outputs=gr.Textbox(label="Respuesta del chatbot"),
        title="Chatbot LLM - Gradio",
        description="Interactúa con el modelo en tiempo real."
    )
    return interfaz

def main_despliegue():
    # Ruta del modelo personalizado o base
    modelo_id = "GPT2"

    from config.entorno import cargar_modelo
    from chatbot.base import Chatbot

    modelo, tokenizador = cargar_modelo(modelo_id)
    bot = Chatbot(modelo, tokenizador)

    interfaz = crear_interfaz_web(bot)
    interfaz.launch()

if __name__ == "__main__":
    main_despliegue()
