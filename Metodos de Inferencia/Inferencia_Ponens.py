# Mini motor de inferencia usando Modus Ponens
# Modus Ponens: Si P entonces Q. Si P es verdadero, entonces Q es verdadero.

# Definimos un conjunto de reglas del tipo: "Si P entonces Q"
reglas = [
    {"condicion": "Llueve", "conclusion": "La calle estará mojada"},
    {"condicion": "La calle estará mojada", "conclusion": "El tráfico será más lento"},
    {"condicion": "Hace frío", "conclusion": "Las personas usarán suéter"},
    {"condicion": "Hay fuego", "conclusion": "Habrá humo"},
    {"condicion": "El tráfico será más lento", "conclusion": "Las personas llegarán tarde"}
]

# Obtenemos todos los posibles hechos iniciales a partir de las condiciones de las reglas
posibles_hechos = sorted({regla["condicion"] for regla in reglas})

# Mostramos al usuario los hechos posibles para que elija los iniciales
print("Hechos posibles para elegir como iniciales:")
for idx, hecho in enumerate(posibles_hechos, 1):
    print(f"{idx}. {hecho}")

# Solicitamos al usuario que seleccione los hechos iniciales por su número
seleccion = input("Elige los hechos iniciales separados por coma (ejemplo: 1,3): ")
indices = [int(i.strip()) for i in seleccion.split(",") if i.strip().isdigit()]
# Creamos el conjunto de hechos iniciales seleccionados por el usuario
hechos = {posibles_hechos[i-1] for i in indices if 1 <= i <= len(posibles_hechos)}

def motor_inferencia(reglas, hechos):
    """
    Motor de inferencia basado en Modus Ponens.
    Aplica reglas del tipo 'Si P entonces Q' mientras se puedan inferir nuevos hechos.
    """
    nuevos_hechos = set(hechos)  # Copiamos los hechos iniciales
    aplicado = True  # Bandera para saber si se aplicó alguna regla en la iteración

    print("\nProceso de inferencia:")
    # Continuamos aplicando reglas mientras se infieran nuevos hechos
    while aplicado:
        aplicado = False
        for regla in reglas:
            # Si la condición de la regla está en los hechos y la conclusión no,
            # entonces inferimos la conclusión y la agregamos a los hechos
            if regla["condicion"] in nuevos_hechos and regla["conclusion"] not in nuevos_hechos:
                print(f"  - Aplicando: Si '{regla['condicion']}' entonces '{regla['conclusion']}'")
                nuevos_hechos.add(regla["conclusion"])
                aplicado = True  # Se aplicó al menos una regla en esta iteración
    return nuevos_hechos  # Retornamos todos los hechos inferidos

# Ejecutamos el motor de inferencia con las reglas y hechos seleccionados
hechos_inferidos = motor_inferencia(reglas, hechos)

# Mostramos los hechos iniciales seleccionados por el usuario
print("\nHechos iniciales seleccionados:")
for hecho in hechos:
    print(f"- {hecho}")

# Mostramos todos los hechos inferidos (incluyendo los iniciales)
print("\nTodos los hechos inferidos:")
for hecho in hechos_inferidos:
    print(f"- {hecho}")