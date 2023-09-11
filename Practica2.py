# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 18:44:57 2023

@author: Home
"""

# Base de datos de respuestas predefinidas
respuestas_predefinidas = {
    "Hola": "¡Hola! Estoy aquí para ayudarte. ¿Cómo estás?",
    "¿Cómo estás?": "Estoy funcionando correctamente, gracias. ¿En qué puedo ayudarte?",
    "De qué te gustaría hablar?": "Puedo hablar sobre muchos temas. ¿Hay algo específico que te interese?",
    "Estoy bien, ¿y tú?": "Estoy funcionando correctamente, gracias. ¿En qué puedo ayudarte?",
    "¿Por qué debo de hacer tarea?": "Por que si no la haces, repruebas",
    "¿Vale la pena vivir?": "No, pero si te preguntan tú di que sí"
}

def chat_bot(pregunta):
    # Buscar una respuesta predefinida
    respuesta = respuestas_predefinidas.get(pregunta)

    if respuesta:
        return respuesta
    else:
        # Si no se encuentra una respuesta predefinida, pedir al usuario que ingrese conocimiento nuevo.
        nuevo_conocimiento = input("Lo siento, no sé la respuesta. ¿Puedes proporcionarme información sobre eso? ")

        # Agregar el nuevo conocimiento a la base de datos
        respuestas_predefinidas[pregunta] = nuevo_conocimiento
        return "¡Gracias por compartir tu conocimiento!"

# Bucle principal del chat
while True:
    entrada_usuario = input("Tú: ")
    respuesta_bot = chat_bot(entrada_usuario)
    print("Bot:", respuesta_bot)