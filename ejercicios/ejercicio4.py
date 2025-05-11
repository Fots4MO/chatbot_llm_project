from optimizacion.ajuste_modelo import (
    cargar_modelo_optimizado,
    evaluar_rendimiento,
    aplicar_sliding_window
)

def ejecutar():
    """
    Ejercicio 4: Optimización del modelo para recursos limitados.
    """
    print("🧪 Ejercicio 4: Evaluación de optimizaciones\n")

    texto_prueba = "What is the purpose of quantum computing?"
    modelos = [
        {"nombre": "Base (sin optimizar)", "opt": {"cuantizacion": False}},
        {"nombre": "Cuantización 4-bit", "opt": {"cuantizacion": True, "bits": 4}},
        {"nombre": "Cuantización + Sliding Window", "opt": {"cuantizacion": True, "bits": 4, "flash_attention": False}}
    ]

    for config in modelos:
        print(f"🔧 Probando configuración: {config['nombre']}")
        modelo, tokenizador = cargar_modelo_optimizado("GPT2", config["opt"])
        aplicar_sliding_window(modelo)  # solo se activa si el modelo lo soporta
        dispositivo = next(modelo.parameters()).device
        metricas = evaluar_rendimiento(modelo, tokenizador, texto_prueba, dispositivo)
        for k, v in metricas.items():
            print(f"   {k}: {v}")
        print("")
