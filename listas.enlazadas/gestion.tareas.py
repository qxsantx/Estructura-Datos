class Tarea:
    def __init__(self, descripcion: str, prioridad: int, fecha_vencimiento: str, tarea: str):
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.fecha_vencimiento = fecha_vencimiento  
        self.tarea = tarea  

    def __str__(self):
        return f"Tarea: {self.tarea}, Descripción: {self.descripcion}, Prioridad: {self.prioridad}, Fecha de vencimiento: {self.fecha_vencimiento}"

class Node:
    def __init__(self, tarea):
        self.tarea = tarea
        self.siguiente = None

class ListaDeTareas:
    def __init__(self):
        self.cabeza = None

    def es_vacio(self):
        return self.cabeza is None

    def agregar_tarea(self, tarea):
        nueva_tarea = Node(tarea)  

        if self.cabeza is None:
            self.cabeza = nueva_tarea
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nueva_tarea
        
        # Imprimimos solo una vez después de agregar la tarea, ya sea en el inicio o al final
        print(f"{tarea.tarea} ha sido agregada a la lista.")

    def mostrar_tareas(self):
        if self.cabeza is None:
            print("No hay tareas en la lista.")
            return
        
        actual = self.cabeza
        while actual is not None:
            print(actual.tarea)  
            actual = actual.siguiente

    def buscar_tarea(self, nombre_tarea):
        if self.cabeza is None:
            print("No hay tareas en la lista.")
            return None
        
        actual = self.cabeza
        while actual is not None:
            if actual.tarea.tarea == nombre_tarea:  # Comparamos por el nombre de la tarea
                return actual.tarea
            actual = actual.siguiente
        
        return None

    def eliminar_tarea(self, nombre_tarea):
        if self.cabeza is None:
            print("No hay tareas para eliminar.")
            return False
        
        if self.cabeza.tarea.tarea == nombre_tarea:  # Si la tarea a eliminar es la primera
            print(f"Tarea '{self.cabeza.tarea.tarea}' completada y eliminada.")
            self.cabeza = self.cabeza.siguiente
            return True
        
        actual = self.cabeza
        while actual.siguiente is not None:
            if actual.siguiente.tarea.tarea == nombre_tarea:  # Buscamos la tarea
                print(f"Tarea '{actual.siguiente.tarea.tarea}' completada y eliminada.")
                actual.siguiente = actual.siguiente.siguiente
                return True
            actual = actual.siguiente
        
        print(f"Tarea '{nombre_tarea}' no encontrada para eliminar.")  # Mensaje claro si no se encuentra
        return False

def agregar_tarea_a_la_lista():
    lista_tareas = ListaDeTareas()

    while True:
        tarea_nombre = input("Ingrese el nombre de la tarea (o 'salir' para terminar): ")
        if tarea_nombre.lower() == 'salir':
            break

        descripcion = input("Ingrese la descripción de la tarea: ")
        prioridad = int(input("Ingrese el nivel de prioridad (1 es alto, 2 es mediano, 3 es bajo): "))
        fecha_vencimiento = input("Ingrese la fecha de vencimiento (ejemplo: 2024-09-30): ")

        nueva_tarea = Tarea(descripcion, prioridad, fecha_vencimiento, tarea_nombre)

        lista_tareas.agregar_tarea(nueva_tarea)

    return lista_tareas

def buscar_y_eliminar_en_bucle(lista_tareas):
    while True:
        print("\nTareas actuales:")
        lista_tareas.mostrar_tareas()

        nombre_tarea = input("\nIngrese el nombre de la tarea a buscar y eliminar (o 'salir' para terminar): ")
        if nombre_tarea.lower() == 'salir':
            break

        tarea_encontrada = lista_tareas.buscar_tarea(nombre_tarea)
        if tarea_encontrada:
            print(f"Tarea encontrada: {tarea_encontrada}")
            confirmacion = input(f"¿Desea eliminar la tarea '{nombre_tarea}'? (si/no): ").lower()
            if confirmacion == 'si':
                lista_tareas.eliminar_tarea(nombre_tarea)
            else:
                print(f"Tarea '{nombre_tarea}' no eliminada.")
        else:
            print(f"Tarea '{nombre_tarea}' no encontrada.")

lista_tareas = agregar_tarea_a_la_lista()

buscar_y_eliminar_en_bucle(lista_tareas)

print("\nTareas restantes:")
lista_tareas.mostrar_tareas()