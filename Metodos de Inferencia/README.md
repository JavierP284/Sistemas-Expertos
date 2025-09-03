# Motores de Inferencia

Los **motores de inferencia** son el núcleo lógico de los sistemas expertos y de muchos programas de inteligencia artificial.  
Su función es **razonar a partir de hechos y reglas** para generar conclusiones o recomendaciones.

---

## Aplicaciones actuales
- Sistemas de diagnóstico médico.  
- Motores de reglas en empresas (ej. **Drools**, **CLIPS**, **Jess**).  
- Chatbots e IA conversacional.  
- Detección de fraudes y seguridad informática.  

---

## Métodos de inferencia
- **Encadenamiento hacia adelante (Forward chaining):**  
  Parte de hechos iniciales y aplica reglas hasta obtener nuevas conclusiones.  

- **Encadenamiento hacia atrás (Backward chaining):**  
  Parte de una hipótesis y busca si los hechos y reglas la confirman.  

---

## Reglas clásicas de lógica
- **Modus Ponens (MP):**  
  Si *P → Q* y *P* es verdadero, entonces *Q* es verdadero.  
  > Ejemplo: Si llueve, entonces la calle estará mojada → Llueve → La calle está mojada.  

- **Modus Tollens (MT):**  
  Si *P → Q* y *Q* es falso, entonces *P* es falso.  
  > Ejemplo: Si hay fuego, entonces habrá humo → No hay humo → No hay fuego.  

---

## Conclusión
Aunque hoy existen técnicas avanzadas como el **machine learning**,  
los motores de inferencia siguen siendo esenciales porque permiten **explicar de forma lógica y transparente cómo se llega a una conclusión**.
