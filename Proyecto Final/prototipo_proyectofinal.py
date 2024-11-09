from typing import Optional, List
import random

class Cancion:
    def __init__(self, titulo: str, artista: str, genero: str, duracion: int):
        self.titulo = titulo
        self.artista = artista
        self.genero = genero
        self.duracion = duracion  # duración en segundos
        self.siguiente = None
        self.anterior = None
    
    def __str__(self):
        return f"{self.titulo} - {self.artista} ({self.genero})"

class SistemaRecomendacion:
    def __init__(self):
        # Base de datos simulada de canciones para recomendaciones
        self.base_canciones = [
            Cancion("Bohemian Rhapsody", "Queen", "Rock", 354),
            Cancion("Stairway to Heaven", "Led Zeppelin", "Rock", 482),
            Cancion("Beat It", "Michael Jackson", "Pop", 258),
            Cancion("Billie Jean", "Michael Jackson", "Pop", 294),
            Cancion("Sweet Child O' Mine", "Guns N' Roses", "Rock", 356),
            Cancion("Despacito", "Luis Fonsi", "Reggaeton", 229),
            Cancion("Shape of You", "Ed Sheeran", "Pop", 234),
            Cancion("Vivir Mi Vida", "Marc Anthony", "Salsa", 252)
        ]
    
    def recomendar_canciones(self, cancion_actual: Cancion, historial: List[Cancion]) -> List[Cancion]:
        """
        Implementa un sistema simple de recomendación basado en género y artista
        """
        recomendaciones = []
        
        # Buscar canciones del mismo género
        for cancion in self.base_canciones:
            if (cancion.genero == cancion_actual.genero or 
                cancion.artista == cancion_actual.artista) and \
                cancion.titulo != cancion_actual.titulo and \
                cancion not in historial:
                recomendaciones.append(cancion)
        
        # Si no hay suficientes recomendaciones, agregar algunas aleatorias
        while len(recomendaciones) < 3:
            cancion_random = random.choice(self.base_canciones)
            if cancion_random not in recomendaciones and \
               cancion_random.titulo != cancion_actual.titulo and \
               cancion_random not in historial:
                recomendaciones.append(cancion_random)
        
        return recomendaciones[:3]  # Devolver máximo 3 recomendaciones

class ReproductorMusica:
    def __init__(self):
        self.actual = None
        self.primera = None
        self.ultima = None
        self.total_canciones = 0
        self.historial = []
        self.sistema_recomendacion = SistemaRecomendacion()
    
    def agregar_cancion(self, titulo: str, artista: str, genero: str, duracion: int) -> None:
        nueva_cancion = Cancion(titulo, artista, genero, duracion)
        
        if not self.primera:
            self.primera = nueva_cancion
            self.ultima = nueva_cancion
            self.actual = nueva_cancion
        else:
            nueva_cancion.anterior = self.ultima
            self.ultima.siguiente = nueva_cancion
            self.ultima = nueva_cancion
        
        self.total_canciones += 1
        print(f"Canción agregada: {nueva_cancion}")
    
    def eliminar_cancion(self, titulo: str) -> None:
        if not self.primera:
            print("No hay canciones en la lista")
            return
        
        actual = self.primera
        while actual:
            if actual.titulo == titulo:
                if actual == self.primera:
                    self.primera = actual.siguiente
                    if self.primera:
                        self.primera.anterior = None
                elif actual == self.ultima:
                    self.ultima = actual.anterior
                    if self.ultima:
                        self.ultima.siguiente = None
                else:
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior
                
                if self.actual == actual:
                    self.actual = actual.siguiente or self.primera
                
                self.total_canciones -= 1
                print(f"Canción eliminada: {actual}")
                return
            actual = actual.siguiente
        
        print(f"No se encontró la canción: {titulo}")
    
    def siguiente_cancion(self) -> Optional[Cancion]:
        if not self.actual:
            print("No hay canciones en la lista")
            return None
        
        if self.actual.siguiente:
            self.actual = self.actual.siguiente
        else:
            self.actual = self.primera
        
        self.historial.append(self.actual)
        if len(self.historial) > 5:  # Mantener solo las últimas 5 canciones en el historial
            self.historial.pop(0)
        
        print(f"Reproduciendo: {self.actual}")
        self.mostrar_recomendaciones()
        return self.actual
    
    def anterior_cancion(self) -> Optional[Cancion]:
        if not self.actual:
            print("No hay canciones en la lista")
            return None
        
        if self.actual.anterior:
            self.actual = self.actual.anterior
        else:
            self.actual = self.ultima
        
        print(f"Reproduciendo: {self.actual}")
        self.mostrar_recomendaciones()
        return self.actual
    
    def mostrar_recomendaciones(self):
        if self.actual:
            print("\nRecomendaciones basadas en tu música:")
            recomendaciones = self.sistema_recomendacion.recomendar_canciones(self.actual, self.historial)
            for i, cancion in enumerate(recomendaciones, 1):
                print(f"{i}. {cancion}")
    
    def mostrar_playlist(self):
        if not self.primera:
            print("No hay canciones en la lista")
            return
        
        print("\nPlaylist completa:")
        actual = self.primera
        while actual:
            estado = "► " if actual == self.actual else "  "
            print(f"{estado}{actual}")
            actual = actual.siguiente

# Ejemplo de uso
def main():
    reproductor = ReproductorMusica()
    
    # Agregar algunas canciones
    reproductor.agregar_cancion("El Perdón", "Nicky Jam", "Reggaeton", 245)
    reproductor.agregar_cancion("La Bicicleta", "Carlos Vives", "Pop Latino", 234)
    reproductor.agregar_cancion("Hasta el Amanecer", "Nicky Jam", "Reggaeton", 238)
    
    # Mostrar playlist inicial
    reproductor.mostrar_playlist()
    
    # Probar navegación
    print("\nProbando navegación:")
    reproductor.siguiente_cancion()
    reproductor.siguiente_cancion()
    reproductor.anterior_cancion()
    
    # Eliminar una canción
    reproductor.eliminar_cancion("La Bicicleta")
    
    # Mostrar playlist actualizada
    reproductor.mostrar_playlist()

if __name__ == "__main__":
    main()