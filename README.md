# Chatbot LLM Project

## Descripción

Este proyecto es una implementación de un **Chatbot utilizando modelos de lenguaje de tipo LLM** (Large Language Model), como GPT2 y otros modelos optimizados para tareas de conversación. El chatbot está diseñado para procesar entradas del usuario, generar respuestas coherentes, mantener el contexto de la conversación, y realizar optimizaciones de rendimiento.

## Funcionalidades

- **Conversación básica**: El chatbot es capaz de mantener una conversación sencilla, respondiendo preguntas y siguiendo un flujo básico de diálogo.
- **Manejo de contexto**: El modelo recuerda el historial de la conversación y usa esa información para generar respuestas más coherentes en conversaciones prolongadas.
- **Optimización para recursos limitados**: Implementa técnicas de optimización para mejorar la velocidad de inferencia y reducir el consumo de memoria. (Precausión)
- **Despliegue web**: El chatbot está disponible a través de una interfaz web utilizando **Gradio** para pruebas y demostraciones.

## Ejercicios

### Ejercicio 1: Carga de modelo base

**Objetivo**: Establecer el entorno de desarrollo necesario para trabajar con modelos LLM y cargar un modelo pre-entrenado utilizando las bibliotecas **Transformers** y **PyTorch**.

**Descripción**: En este ejercicio, se configura el entorno para cargar y usar modelos pre-entrenados. El modelo que se utiliza es GPT2 por defecto.

### Ejercicio 2: Procesamiento de Entrada y Generación de Respuestas

**Objetivo**: Desarrollar las funciones necesarias para procesar la entrada del usuario, preparar los tokens para el modelo y generar respuestas coherentes.

**Descripción**: Aquí se implementan las funciones que permiten procesar la entrada del usuario y generar una respuesta adecuada, considerando la información proporcionada en el historial de la conversación.

### Ejercicio 3: Manejo de Contexto Conversacional

**Objetivo**: Implementar un sistema para mantener el contexto de la conversación, permitiendo al chatbot recordar intercambios anteriores y responder coherentemente a conversaciones prolongadas.

**Descripción**: Este ejercicio implementa el manejo de contexto, manteniendo un historial de las interacciones y usando ese contexto para generar respuestas más naturales.

### Ejercicio 4: Optimización del Modelo para Recursos Limitados (precausión)

**Objetivo**: Implementar técnicas de optimización para mejorar la velocidad de inferencia y reducir el consumo de memoria, permitiendo que el chatbot funcione eficientemente en dispositivos con recursos limitados.

**Descripción**: Aquí se realizan optimizaciones en el modelo, como el uso de técnicas de cuantización y atención deslizante, para mejorar su rendimiento en dispositivos con capacidades limitadas.

**Advertencia**: Aún sin haber comprobado completamente el problema, parece ser que ejecutar el Ejercicio 4, puede "atrofiar" las capacidades del chatbot. Este comportamiento se ha observado debido a ciertos parámetros de optimización que afectan negativamente el rendimiento del modelo de conversación. Se recomienda no ejecutar este ejercicio si se busca mantener el funcionamiento correcto del chatbot. Aunque el ejercicio si cumple con el objetivo.

### Ejercicio 5: Personalización del Chatbot y Despliegue

**Objetivo**: Implementar técnicas para personalizar el comportamiento del chatbot y prepararlo para su despliegue como una aplicación web simple.

**Descripción**: Este ejercicio prepara el chatbot para ser utilizado en un entorno web con una interfaz gráfica, utilizando **Gradio** para la demostración y el despliegue del modelo.

## Instrucciones para clonar e instalar

### Clonar el repositorio

Puedes clonar este repositorio en tu máquina local utilizando el siguiente comando en tu terminal o consola de comandos:

```bash
git clone https://github.com/Fots4MO/chatbot_llm_project.git
```

##Instalación de dependencias

**Instalar Python**: Asegúrate de tener Python 3.7 o superior instalado en tu máquina. Puedes descargarlo desde python.org.

Crear un entorno virtual (opcional pero recomendado):

```bash
python -m venv .venv
```

###Activar el entorno virtual:

**En Windows**:

```bash
.\.venv\Scripts\actívate
```

**En macOS/Linux**:

```bash
source .venv/bin/actívate
```

**Instalar las dependencias**:

```bash
pip install -r requirements.txt
```

###Ejecutar el proyecto:

Puedes ejecutar el proyecto con el siguiente comando:

```bash
python main.py
```

Luego, selecciona el ejercicio que deseas ejecutar desde el menú interactivo.
