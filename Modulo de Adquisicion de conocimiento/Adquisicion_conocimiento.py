import json
import os

# Archivo donde se guardará la base de conocimientos
DB_FILE = "knowledge_base.json"

# Base de conocimientos inicial (precargada)
default_knowledge = {
    "hola": "¡Hola! ¿Cómo estás?",
    "como estas": "Estoy bien, gracias. ¿Y tú?",
    "de que te gustaría hablar": "Podemos hablar de tecnología, deportes o música."
}

# Cargar la base de datos si existe, si no crearla
if os.path.exists(DB_FILE):
    # Si el archivo existe, cargar la base de conocimientos desde el archivo JSON
    with open(DB_FILE, "r", encoding="utf-8") as file:
        knowledge_base = json.load(file)
else:
    # Si el archivo no existe, usar la base de conocimientos por defecto y crear el archivo
    knowledge_base = default_knowledge
    with open(DB_FILE, "w", encoding="utf-8") as file:
        json.dump(knowledge_base, file, indent=4, ensure_ascii=False)

print("¡Bienvenido al chatbot! Escribe 'salir' para terminar.")

# Bucle principal del chatbot
while True:
    user_input = input("Tú: ").strip().lower()  # Leer entrada del usuario y normalizar
    
    if user_input == "salir":
        # Si el usuario escribe 'salir', terminar el programa
        print("Chatbot: ¡Hasta luego!")
        break
    
    # Buscar coincidencia exacta en la base de conocimientos
    response = knowledge_base.get(user_input)
    
    if response:
        # Si se encuentra una respuesta, mostrarla
        print(f"Chatbot: {response}")
    else:
        # Si no se encuentra, pedir al usuario que enseñe una respuesta
        print("Chatbot: No sé cómo responder a eso. ¿Qué debería decir?")
        new_response = input("Tú (respuesta para aprender): ").strip()
        knowledge_base[user_input] = new_response  # Guardar la nueva respuesta
        
        # Guardar la base de conocimientos actualizada en el archivo
        with open(DB_FILE, "w", encoding="utf-8") as file:
            json.dump(knowledge_base, file, indent=4, ensure_ascii=False)
        
        print("Chatbot: ¡Gracias! Ahora puedo responder eso la próxima vez.")
