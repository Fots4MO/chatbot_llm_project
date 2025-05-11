from config.entorno import cargar_modelo
from chatbot.base import Chatbot

def prueba_chat():
    """
    Prueba básica de conversación por consola.
    """
    instrucciones = "You are a helpful assistant. Always respond clearly."
    modelo, tokenizador = cargar_modelo("GPT2")
    bot = Chatbot(modelo, tokenizador)

    print("🤖 Chatbot listo. Escribe 'salir' para terminar.\n")
    while True:
        entrada = input("👤 Tú: ")
        if entrada.lower() in ["salir", "exit", "quit"]:
            print("🤖 Adiós.")
            break
        respuesta = bot.responder(entrada)
        print(f"🤖 {respuesta}\n")

if __name__ == "__main__":
    print("=== Proyecto Chatbot LLM ===")
    print("1. Prueba básica del chatbot")
    print("2. Ejecutar ejercicio 1")
    print("3. Ejecutar ejercicio 2")
    print("4. Ejecutar ejercicio 3")
    print("5. Ejecutar ejercicio 4")
    print("6. Ejecutar despliegue web (Gradio)")
    opcion = input("Selecciona una opción (1-6): ")

    if opcion == "1":
        prueba_chat()
    elif opcion == "2":
        import ejercicios.ejercicio1 as e1
        e1.ejecutar()
    elif opcion == "3":
        import ejercicios.ejercicio2 as e2
        e2.ejecutar()
    elif opcion == "4":
        import ejercicios.ejercicio3 as e3
        e3.ejecutar()
    elif opcion == "5":
        import ejercicios.ejercicio4 as e4
        e4.ejecutar()
    elif opcion == "6":
        import despliegue.interfaz_web as web
        web.main_despliegue()
    else:
        print("❌ Opción no válida.")
