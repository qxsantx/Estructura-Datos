import webbrowser

class Nodo:
    def __init__(self, cancion):
        self.cancion = cancion
        self.anterior = None
        self.siguiente = None

class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar(self, cancion):
        nuevo_nodo = Nodo(cancion)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo

    def eliminar(self, cancion):
        actual = self.cabeza
        while actual:
            if actual.cancion == cancion:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                if actual == self.cabeza:  # Si es el nodo cabeza
                    self.cabeza = actual.siguiente
                if actual == self.cola:  # Si es el nodo cola
                    self.cola = actual.anterior
                return True  # Canción eliminada
            actual = actual.siguiente
        return False  # Canción no encontrada

    def siguiente(self, cancion_actual):
        actual = self.cabeza
        while actual:
            if actual.cancion == cancion_actual:
                return actual.siguiente.cancion if actual.siguiente else None
            actual = actual.siguiente
        return None

    def anterior(self, cancion_actual):
        actual = self.cabeza
        while actual:
            if actual.cancion == cancion_actual:
                return actual.anterior.cancion if actual.anterior else None
            actual = actual.siguiente
        return None

class ReproductorMusica:
    def __init__(self):
        self.playlist = ListaDobleEnlazada()
        self.cancion_actual = None

    def agregar_cancion(self, cancion):
        self.playlist.agregar(cancion)

    def eliminar_cancion(self, cancion):
        return self.playlist.eliminar(cancion)

    def reproducir_cancion(self, cancion):
        self.cancion_actual = cancion
        print(f"Reproduciendo: {cancion}")
        webbrowser.open(f"https://www.youtube.com/results?search_query={cancion}")

    def siguiente_cancion(self):
        cancion_siguiente = self.playlist.siguiente(self.cancion_actual)
        if cancion_siguiente:
            self.reproducir_cancion(cancion_siguiente)

    def anterior_cancion(self):
        cancion_anterior = self.playlist.anterior(self.cancion_actual)
        if cancion_anterior:
            self.reproducir_cancion(cancion_anterior)

# Ejemplo de uso
if __name__ == "__main__":
    reproductor = ReproductorMusica()
    reproductor.agregar_cancion("Feid - tengo fe")
    reproductor.agregar_cancion("blessd - soltera W")
    reproductor.agregar_cancion("Karol g - bichota")

    reproductor.reproducir_cancion("Feid - tengo fe")  # Inicia la reproducción de "Canción 1"
    reproductor.siguiente_cancion()               # Reproduce "Canción 2"
    reproductor.anterior_cancion()                # Reproduce "Canción 1" de nuevo
    reproductor.eliminar_cancion("blessd - soltera W")     # Elimina "Canción 2"
    reproductor.siguiente_cancion()               # Ahora reproduce "Canción 3"