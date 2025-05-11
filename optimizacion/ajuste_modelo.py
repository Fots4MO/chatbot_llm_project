from transformers import BitsAndBytesConfig, AutoTokenizer, AutoModelForCausalLM
import torch
import time
import psutil

def configurar_cuantizacion(bits=4):
    """
    Configura los parámetros para la cuantización del modelo.
    """
    config_cuantizacion = BitsAndBytesConfig(
        load_in_4bit=(bits == 4),
        load_in_8bit=(bits == 8),
        bnb_4bit_use_double_quant=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.float16
    )
    return config_cuantizacion

def cargar_modelo_optimizado(nombre_modelo, optimizaciones=None):
    """
    Carga un modelo con optimizaciones aplicadas.
    """
    if optimizaciones is None:
        optimizaciones = {
            "cuantizacion": True,
            "bits": 4,
            "offload_cpu": False,
            "flash_attention": False
        }

    cuant_config = configurar_cuantizacion(bits=optimizaciones["bits"]) if optimizaciones["cuantizacion"] else None

    modelo = AutoModelForCausalLM.from_pretrained(
        nombre_modelo,
        device_map="auto",
        quantization_config=cuant_config,
        torch_dtype=torch.float16,
        trust_remote_code=True
    )
    tokenizador = AutoTokenizer.from_pretrained(nombre_modelo, use_fast=True)

    return modelo.eval(), tokenizador

def aplicar_sliding_window(modelo, window_size=1024):
    """
    Configura la atención de ventana deslizante (solo si el modelo lo soporta).
    """
    if hasattr(modelo.config, "sliding_window"):
        modelo.config.sliding_window = window_size

def evaluar_rendimiento(modelo, tokenizador, texto_prueba, dispositivo):
    """
    Evalúa rendimiento: tiempo, memoria, tokens por segundo.
    """
    entrada = tokenizador(texto_prueba, return_tensors="pt").to(dispositivo)

    inicio = time.time()
    salida = modelo.generate(**entrada, max_new_tokens=100)
    fin = time.time()

    duracion = fin - inicio
    tokens = salida.shape[1]
    memoria = psutil.virtual_memory().used / (1024 ** 3)  # en GB

    return {
        "tiempo_inferencia": round(duracion, 3),
        "tokens_generados": tokens,
        "tokens_por_segundo": round(tokens / duracion, 2),
        "uso_memoria_GB": round(memoria, 2)
    }
