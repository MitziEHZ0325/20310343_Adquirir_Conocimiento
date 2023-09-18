# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 23:01:47 2023

@author: Home
"""

import json

# Función para cargar la base de datos desde un archivo JSON
def cargar_base_de_datos():
    try:
        with open("base_de_datos.json", "r") as archivo:
            base_de_datos = json.load(archivo)
            return base_de_datos
    except FileNotFoundError:
        return {}

# Función para guardar la base de datos en un archivo JSON
def guardar_base_de_datos(base_de_datos):
    with open("base_de_datos.json", "w") as archivo:
        json.dump(base_de_datos, archivo, indent=4)

# Cargar la base de datos al inicio del programa
respuestas_predefinidas = cargar_base_de_datos()

# Agregar las preguntas y respuestas predefinidas originales
respuestas_predefinidas.update({
    "Hola": "¡Hola! Estoy aquí para ayudarte. ¿Cómo estás?",
    "¿Cómo estás?": "Estoy funcionando correctamente, gracias. ¿En qué puedo ayudarte?",
    "De qué te gustaría hablar?": "Puedo hablar sobre muchos temas. ¿Hay algo específico que te interese?",
    "Estoy bien, ¿y tú?": "Estoy funcionando correctamente, gracias. ¿En qué puedo ayudarte?",
    "¿Por qué debo de hacer tarea?": "Porque si no la haces, repruebas",
    "¿Vale la pena vivir?": "No, pero si te preguntan tú di que sí"
})

def agregar_conocimiento(pregunta, respuesta):
    respuestas_predefinidas[pregunta] = respuesta
    # Guardar la base de datos actualizada en el archivo JSON
    guardar_base_de_datos(respuestas_predefinidas)

def chat_bot(pregunta):
    # Buscar una respuesta predefinida
    respuesta = respuestas_predefinidas.get(pregunta)

    if respuesta:
        return respuesta
    else:
        # Si no se encuentra una respuesta predefinida, pedir al usuario que ingrese conocimiento nuevo.
        nuevo_conocimiento = input("Lo siento, no sé la respuesta. ¿Puedes proporcionarme información sobre eso? ")
        
        # Agregar el nuevo conocimiento a la base de datos usando la función agregar_conocimiento
        agregar_conocimiento(pregunta, nuevo_conocimiento)

        return "¡Gracias por compartir tu conocimiento!"

# Bucle principal del chat
while True:
    entrada_usuario = input("Tú: ")
    respuesta_bot = chat_bot(entrada_usuario)
    print("Bot:", respuesta_bot)