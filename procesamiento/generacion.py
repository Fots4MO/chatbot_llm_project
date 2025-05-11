def generar_respuesta(modelo, entrada_procesada, tokenizador, parametros=None):
    if parametros is None:
        parametros = {
            "do_sample": True,
            "max_new_tokens": 50,
            "temperature": 0.8,
            "top_p": 0.9,
            "top_k": 50,
            "repetition_penalty": 1.1,
            "pad_token_id": tokenizador.eos_token_id
        }

    salida = modelo.generate(**entrada_procesada, **parametros)
    respuesta = tokenizador.decode(salida[0], skip_special_tokens=True)
    return respuesta
