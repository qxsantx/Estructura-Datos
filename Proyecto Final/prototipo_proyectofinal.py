import tkinter as tk
from tkinter import ttk, messagebox
import json
from datetime import datetime
import os

class Nodo:
    def __init__(self, pregunta=None, diagnostico=None, nivel_urgencia=None):
        self.pregunta = pregunta
        self.diagnostico = diagnostico
        self.nivel_urgencia = nivel_urgencia  # Nueva propiedad para urgencia
        self.izquierda = None
        self.derecha = None

class SistemaDiagnostico:
    def __init__(self):
        self.raiz = self.construir_arbol()
        self.historial = []
        self.cargar_historial()

    def construir_arbol(self):
        # Nodo raíz
        raiz = Nodo(pregunta="¿Tiene fiebre alta (más de 38.5°C)?")
        
        # Rama izquierda principal (sin fiebre alta)
        raiz.izquierda = Nodo(pregunta="¿Tiene dolor de cabeza?")
        
        # Sub-rama izquierda sin fiebre
        raiz.izquierda.izquierda = Nodo(pregunta="¿Siente fatiga?")
        raiz.izquierda.izquierda.izquierda = Nodo(
            diagnostico="Posible estrés",
            nivel_urgencia="Bajo"
        )
        raiz.izquierda.izquierda.derecha = Nodo(
            diagnostico="Posible deficiencia de vitaminas",
            nivel_urgencia="Bajo"
        )
        
        raiz.izquierda.derecha = Nodo(pregunta="¿El dolor es pulsante?")
        raiz.izquierda.derecha.izquierda = Nodo(
            diagnostico="Posible tensión muscular",
            nivel_urgencia="Bajo"
        )
        raiz.izquierda.derecha.derecha = Nodo(
            diagnostico="Posible migraña",
            nivel_urgencia="Medio"
        )
        
        # Rama derecha principal (con fiebre alta)
        raiz.derecha = Nodo(pregunta="¿Tiene dificultad para respirar?")
        
        raiz.derecha.izquierda = Nodo(pregunta="¿Tiene dolor muscular?")
        raiz.derecha.izquierda.izquierda = Nodo(
            diagnostico="Posible infección viral",
            nivel_urgencia="Medio"
        )
        raiz.derecha.izquierda.derecha = Nodo(
            diagnostico="Posible influenza",
            nivel_urgencia="Alto"
        )
        
        raiz.derecha.derecha = Nodo(pregunta="¿Tiene dolor en el pecho?")
        raiz.derecha.derecha.izquierda = Nodo(
            diagnostico="Posible neumonía",
            nivel_urgencia="Alto"
        )
        raiz.derecha.derecha.derecha = Nodo(
            diagnostico="EMERGENCIA MÉDICA",
            nivel_urgencia="Crítico"
        )
        
        return raiz

    def guardar_diagnostico(self, diagnostico, nivel_urgencia, sintomas):
        registro = {
            'fecha': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'diagnostico': diagnostico,
            'nivel_urgencia': nivel_urgencia,
            'sintomas': sintomas
        }
        self.historial.append(registro)
        
        # Guardar en archivo JSON
        with open('historial_diagnosticos.json', 'w') as f:
            json.dump(self.historial, f, indent=4)

    def cargar_historial(self):
        try:
            with open('historial_diagnosticos.json', 'r') as f:
                self.historial = json.load(f)
        except FileNotFoundError:
            self.historial = []

class InterfazGrafica:
    def __init__(self):
        self.sistema = SistemaDiagnostico()
        self.sintomas_registrados = []
        self.crear_ventana()

    def crear_ventana(self):
        self.ventana = tk.Tk()
        self.ventana.title("Sistema de Diagnóstico Médico")
        self.ventana.geometry("800x600")

        # Marco principal
        self.marco_principal = ttk.Frame(self.ventana, padding="10")
        self.marco_principal.pack(fill=tk.BOTH, expand=True)

        # Título
        ttk.Label(
            self.marco_principal,
            text="Sistema de Diagnóstico Médico",
            font=('Helvetica', 16, 'bold')
        ).pack(pady=10)

        # Marco para el diagnóstico
        self.marco_diagnostico = ttk.LabelFrame(
            self.marco_principal,
            text="Diagnóstico",
            padding="10"
        )
        self.marco_diagnostico.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # Etiqueta para preguntas
        self.etiqueta_pregunta = ttk.Label(
            self.marco_diagnostico,
            text="Presione 'Iniciar' para comenzar el diagnóstico",
            wraplength=500
        )
        self.etiqueta_pregunta.pack(pady=20)

        # Botones de respuesta
        self.marco_botones = ttk.Frame(self.marco_diagnostico)
        self.marco_botones.pack(pady=10)

        self.btn_si = ttk.Button(
            self.marco_botones,
            text="Sí",
            command=lambda: self.procesar_respuesta('s'),
            state=tk.DISABLED
        )
        self.btn_si.pack(side=tk.LEFT, padx=5)

        self.btn_no = ttk.Button(
            self.marco_botones,
            text="No",
            command=lambda: self.procesar_respuesta('n'),
            state=tk.DISABLED
        )
        self.btn_no.pack(side=tk.LEFT, padx=5)

        # Botón de inicio
        self.btn_iniciar = ttk.Button(
            self.marco_diagnostico,
            text="Iniciar Diagnóstico",
            command=self.iniciar_diagnostico
        )
        self.btn_iniciar.pack(pady=10)

        # Marco para el historial
        self.marco_historial = ttk.LabelFrame(
            self.marco_principal,
            text="Historial de Diagnósticos",
            padding="10"
        )
        self.marco_historial.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # Tabla de historial
        self.crear_tabla_historial()

    def crear_tabla_historial(self):
        # Crear Treeview
        columnas = ('Fecha', 'Diagnóstico', 'Nivel de Urgencia')
        self.tabla = ttk.Treeview(
            self.marco_historial,
            columns=columnas,
            show='headings'
        )

        # Configurar columnas
        for col in columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=150)

        # Agregar scrollbar
        scrollbar = ttk.Scrollbar(
            self.marco_historial,
            orient=tk.VERTICAL,
            command=self.tabla.yview
        )
        self.tabla.configure(yscrollcommand=scrollbar.set)

        # Empaquetar elementos
        self.tabla.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Cargar historial
        self.actualizar_tabla_historial()

    def actualizar_tabla_historial(self):
        # Limpiar tabla
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        # Agregar registros del historial
        for registro in self.sistema.historial:
            self.tabla.insert(
                '',
                'end',
                values=(
                    registro['fecha'],
                    registro['diagnostico'],
                    registro['nivel_urgencia']
                )
            )

    def iniciar_diagnostico(self):
        self.nodo_actual = self.sistema.raiz
        self.sintomas_registrados = []
        self.mostrar_pregunta()
        self.btn_iniciar.config(state=tk.DISABLED)
        self.btn_si.config(state=tk.NORMAL)
        self.btn_no.config(state=tk.NORMAL)

    def mostrar_pregunta(self):
        if self.nodo_actual.pregunta:
            self.etiqueta_pregunta.config(text=self.nodo_actual.pregunta)
        else:
            self.mostrar_diagnostico()

    def procesar_respuesta(self, respuesta):
        if self.nodo_actual.pregunta:
            # Registrar síntoma
            self.sintomas_registrados.append(
                f"{self.nodo_actual.pregunta}: {'Sí' if respuesta == 's' else 'No'}"
            )
            
            # Moverse al siguiente nodo
            if respuesta == 's':
                self.nodo_actual = self.nodo_actual.derecha
            else:
                self.nodo_actual = self.nodo_actual.izquierda

            self.mostrar_pregunta()

    def mostrar_diagnostico(self):
        diagnostico = self.nodo_actual.diagnostico
        nivel_urgencia = self.nodo_actual.nivel_urgencia
        
        # Mostrar resultado
        mensaje = f"""
        DIAGNÓSTICO PRELIMINAR:
        {diagnostico}
        
        Nivel de Urgencia: {nivel_urgencia}
        
        {'¡BUSQUE ATENCIÓN MÉDICA INMEDIATA!' if nivel_urgencia in ['Alto', 'Crítico'] else 'Consulte a su médico cuando sea posible.'}
        """
        
        self.etiqueta_pregunta.config(text=mensaje)
        
        # Guardar diagnóstico
        self.sistema.guardar_diagnostico(
            diagnostico,
            nivel_urgencia,
            self.sintomas_registrados
        )
        
        # Actualizar tabla
        self.actualizar_tabla_historial()
        
        # Resetear botones
        self.btn_si.config(state=tk.DISABLED)
        self.btn_no.config(state=tk.DISABLED)
        self.btn_iniciar.config(state=tk.NORMAL)

    def iniciar(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    interfaz = InterfazGrafica()
    interfaz.iniciar()