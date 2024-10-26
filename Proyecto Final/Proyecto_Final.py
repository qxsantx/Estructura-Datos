class Nodo:
    def __init__(self, pregunta=None, diagnostico=None):
        self.pregunta = pregunta  # Pregunta en nodos internos
        self.diagnostico = diagnostico  # Diagnóstico en nodos hoja
        self.izquierda = None  # Respuesta "No"
        self.derecha = None    # Respuesta "Sí"
        
class ArbolDiagnostico:
    def __init__(self):
        self.raiz = self.construir_arbol()
    
    def construir_arbol(self):
        # Crear el árbol de decisión médica
        raiz = Nodo(pregunta="¿Tiene fiebre?")
        
        # Rama izquierda (sin fiebre)
        raiz.izquierda = Nodo(pregunta="¿Tiene dolor de cabeza?")
        raiz.izquierda.izquierda = Nodo(pregunta="¿Tiene fatiga?")
        raiz.izquierda.izquierda.izquierda = Nodo(diagnostico="Posible estrés. Recomendación: Descanso y técnicas de relajación.")
        raiz.izquierda.izquierda.derecha = Nodo(diagnostico="Posible falta de sueño. Recomendación: Mejorar hábitos de sueño.")
        raiz.izquierda.derecha = Nodo(pregunta="¿La luz le molesta?")
        raiz.izquierda.derecha.izquierda = Nodo(diagnostico="Posible tensión. Recomendación: Analgésicos y descanso.")
        raiz.izquierda.derecha.derecha = Nodo(diagnostico="Posible migraña. Recomendación: Consultar neurólogo.")
        
        # Rama derecha (con fiebre)
        raiz.derecha = Nodo(pregunta="¿Tiene tos?")
        raiz.derecha.izquierda = Nodo(pregunta="¿Tiene dolor muscular?")
        raiz.derecha.izquierda.izquierda = Nodo(diagnostico="Posible infección viral leve. Recomendación: Reposo y abundante líquido.")
        raiz.derecha.izquierda.derecha = Nodo(diagnostico="Posible gripe. Recomendación: Reposo, antipiréticos y consulta médica.")
        raiz.derecha.derecha = Nodo(pregunta="¿Tiene dificultad para respirar?")
        raiz.derecha.derecha.izquierda = Nodo(diagnostico="Posible bronquitis. Recomendación: Consulta médica urgente.")
        raiz.derecha.derecha.derecha = Nodo(diagnostico="Posible neumonía. Recomendación: Acudir a emergencias.")
        
        return raiz
    
    def diagnosticar(self):
        nodo_actual = self.raiz
        
        while nodo_actual.diagnostico is None:
            respuesta = input(f"{nodo_actual.pregunta} (s/n): ").lower()
            
            if respuesta == 's':
                nodo_actual = nodo_actual.derecha
            elif respuesta == 'n':
                nodo_actual = nodo_actual.izquierda
            else:
                print("Por favor, responde 's' para sí o 'n' para no.")
                continue
                
        print("\nDIAGNÓSTICO PRELIMINAR:")
        print(nodo_actual.diagnostico)

# Ejemplo de uso
def main():
    print("Sistema de Diagnóstico Médico Básico")
    print("=====================================")
    print("Responde a las siguientes preguntas con 's' (sí) o 'n' (no)\n")
    
    sistema = ArbolDiagnostico()
    sistema.diagnosticar()

if __name__ == "__main__":
    main()