# Mini motor de inferencia usando Modus Tollens
# Modus Tollens: Si P entonces Q. No Q, por tanto No P.

# Definimos un conjunto de reglas del tipo: "Si P entonces Q"
reglas = [
    {"condicion": "Hay fuego", "conclusion": "Habrá humo"},
    {"condicion": "Está encendido el auto", "conclusion": "Habrá ruido del motor"},
    {"condicion": "La computadora está encendida", "conclusion": "La pantalla está iluminada"},
    {"condicion": "Hay corriente eléctrica", "conclusion": "La computadora está encendida"}
]

# Obtenemos todas las posibles conclusiones para negar (No Q)
# Esto permite al usuario seleccionar qué hechos negados conoce
posibles_negaciones = sorted({f"No {regla['conclusion']}" for regla in reglas})

# Mostramos al usuario los hechos negados posibles para elegir
print("Hechos posibles para negar (No Q):")
for idx, hecho in enumerate(posibles_negaciones, 1):
    print(f"{idx}. {hecho}")

# Solicitamos al usuario que seleccione los hechos negados iniciales por su número
# El usuario ingresa los números de los hechos negados separados por coma
seleccion = input("Elige los hechos negados iniciales separados por coma (ejemplo: 1,3): ")
indices = [int(i.strip()) for i in seleccion.split(",") if i.strip().isdigit()]
# Creamos el conjunto de hechos negados iniciales seleccionados por el usuario
hechos_negados = {posibles_negaciones[i-1] for i in indices if 1 <= i <= len(posibles_negaciones)}

def motor_inferencia_tollens(reglas, hechos_negados):
    """
    Motor de inferencia basado en Modus Tollens.
    Aplica reglas del tipo 'Si P entonces Q' mientras se puedan inferir nuevas negaciones.
    Si se sabe 'No Q', se puede inferir 'No P'.
    """
    nuevos_negados = set(hechos_negados)  # Copiamos los hechos negados iniciales
    aplicado = True  # Bandera para saber si se aplicó alguna regla en la iteración

    print("\nProceso de inferencia:")
    # Continuamos aplicando reglas mientras se infieran nuevas negaciones
    while aplicado:
        aplicado = False
        for regla in reglas:
            neg_conclusion = f"No {regla['conclusion']}"  # No Q
            neg_condicion = f"No {regla['condicion']}"    # No P
            # Si 'No Q' está en los hechos negados y 'No P' aún no,
            # entonces inferimos 'No P' y lo agregamos a los hechos negados
            if neg_conclusion in nuevos_negados and neg_condicion not in nuevos_negados:
                print(f"  - Aplicando: Si '{regla['condicion']}' entonces '{regla['conclusion']}'. '{neg_conclusion}' ⇒ '{neg_condicion}'")
                nuevos_negados.add(neg_condicion)
                aplicado = True  # Se aplicó al menos una regla en esta iteración
    return nuevos_negados  # Retornamos todos los hechos negados inferidos

# Ejecutamos el motor de inferencia Tollens con las reglas y hechos negados seleccionados
negaciones_inferidas = motor_inferencia_tollens(reglas, hechos_negados)

# Mostramos los hechos negados iniciales seleccionados por el usuario
print("\nHechos negados iniciales seleccionados:")
for hecho in hechos_negados:
    print(f"- {hecho}")

# Mostramos todos los hechos negados inferidos (incluyendo los iniciales)
print("\nTodos los hechos negados inferidos:")
for hecho in negaciones_inferidas:
    print(f"- {hecho}")