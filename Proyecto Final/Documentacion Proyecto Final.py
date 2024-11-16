"""
------------------------------------------------------------
Este módulo implementa un reproductor de música con sistema de recomendaciones
basado en los géneros musicales y artistas. Incluye funcionalidades de
reproducción básica y un sistema de recomendaciones simple.

Características principales:
- Gestión de playlist mediante lista doblemente enlazada
- Sistema de recomendaciones basado en géneros y artistas
- Historial de reproducción limitado a 5 canciones

Autor: Santiago Mayorga
Fecha: 16/11/2024
"""

from typing import Optional, List
import random

class Cancion:
    """
    Clase canción
    
    Implementa una estructura de nodo para una lista doblemente enlazada,
    almacenando referencias a las canciones anterior y siguiente.

    Atributos:
        titulo (str): Título de la canción
        artista (str): Nombre del artista
        genero (str): Género musical
        duracion (int): Duración en segundos
        siguiente (Optional[Cancion]): Referencia a la siguiente canción
        anterior (Optional[Cancion]): Referencia a la canción anterior
    """
    
    def __init__(self, titulo: str, artista: str, genero: str, duracion: int):
        """
        Inicializa una nueva instancia de Cancion.

        Argunentos:
            titulo: Título de la canción
            artista: Nombre del artista
            genero: Género musical
            duracion: Duración en segundos
        """
        self.titulo = titulo
        self.artista = artista
        self.genero = genero
        self.duracion = duracion  # duración en segundos
        self.siguiente = None
        self.anterior = None
    
    def __str__(self) -> str:
        """
        Retorna una representación en string de la canción.
        """
        return f"{self.titulo} - {self.artista} ({self.genero})"

class SistemaRecomendacion:
    """
    Sistema de recomendaciones
    
    Implementa un sistema simple de recomendaciones basado en géneros
    y artistas similares, utilizando una base de datos simulada.
    """

    def __init__(self):
        """
        Inicializa el sistema de recomendación con una base de datos
        predefinida de canciones.
        """
        # Base de datos simulada de canciones para recomendaciones
        self.base_canciones = [
            Cancion("We Will Rock You", "Queen", "Rock", 128),
            Cancion("Don't Stop Me Now", "Queen", "Rock", 298),
            Cancion("Beat It", "Michael Jackson", "Pop", 258),
            Cancion("Billie Jean", "Michael Jackson", "Pop", 294),
            Cancion("Creep", "Radiohead", "Rock", 213),
            Cancion("Monastery", "Feid", "Reggaeton", 212),
            Cancion("Shape of You", "Ed Sheeran", "Pop", 234),
            Cancion("Que hay de malo", "Jerry Rivera", "Salsa", 320)
        ]
    
    def recomendar_canciones(self, cancion_actual: Cancion, historial: List[Cancion]) -> List[Cancion]:
        """
        Genera recomendaciones basadas en la canción actual y el historial.

        argumentos:
            cancion_actual: Canción que se está reproduciendo actualmente
            historial: Lista de últimas canciones reproducidas

        Returns:
            Lista de hasta 3 canciones recomendadas
        """
        recomendaciones = []
        
        # Buscar canciones del mismo género o artista
        for cancion in self.base_canciones:
            if (cancion.genero == cancion_actual.genero or 
                cancion.artista == cancion_actual.artista) and \
                cancion.titulo != cancion_actual.titulo and \
                cancion not in historial:
                recomendaciones.append(cancion)
        
        # Complementar con recomendaciones aleatorias si es necesario
        while len(recomendaciones) < 3:
            cancion_random = random.choice(self.base_canciones)
            if cancion_random not in recomendaciones and \
               cancion_random.titulo != cancion_actual.titulo and \
               cancion_random not in historial:
                recomendaciones.append(cancion_random)
        
        return recomendaciones[:3]

class ReproductorMusica:
    """
    Clase principal del reproductor de música.
    
    Implementa la funcionalidad basica del reproductor, incluyendo:
    - Gestión de playlist
    - Control de reproducción
    - Integración con sistema de recomendaciones
    """

    def __init__(self):
        """
        Inicializa un nuevo reproductor de música.
        """
        self.actual = None        # Canción en reproducción
        self.primera = None       # Primera canción de la playlist
        self.ultima = None        # Última canción de la playlist
        self.total_canciones = 0  # Contador de canciones
        self.historial = []       # Historial de reproducción (máx. 5)
        self.sistema_recomendacion = SistemaRecomendacion()

    def agregar_cancion(self, titulo: str, artista: str, genero: str, duracion: int) -> None:
        """
        Agrega una nueva canción al final de la playlist.

        argumentos:
            titulo: Título de la canción
            artista: Nombre del artista
            genero: Género musical
            duracion: Duración en segundos
        """
        nueva_cancion = Cancion(titulo, artista, genero, duracion)
        
        if not self.primera:
            # Si la playlist está vacía
            self.primera = nueva_cancion
            self.ultima = nueva_cancion
            self.actual = nueva_cancion
        else:
            # Agregar al final de la lista
            nueva_cancion.anterior = self.ultima
            self.ultima.siguiente = nueva_cancion
            self.ultima = nueva_cancion
        
        self.total_canciones += 1
        print(f"Canción agregada: {nueva_cancion}")
    
    def eliminar_cancion(self, titulo: str) -> None:
        """
        Elimina una canción de la playlist por su título.

        Argumentos:
            titulo: Título de la canción a eliminar
        """
        if not self.primera:
            print("No hay canciones en la lista")
            return
        
        actual = self.primera
        while actual:
            if actual.titulo == titulo:
                # Manejar enlaces de la lista doblemente enlazada
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
                
                # Actualizar canción actual si es necesario
                if self.actual == actual:
                    self.actual = actual.siguiente or self.primera
                
                self.total_canciones -= 1
                print(f"Canción eliminada: {actual}")
                return
            actual = actual.siguiente
        
        print(f"No se encontró la canción: {titulo}")
    
    def siguiente_cancion(self) -> Optional[Cancion]:
        """
        Avanza a la siguiente canción en la playlist.

        Returns:
            La siguiente canción o None si la playlist está vacía
        """
        if not self.actual:
            print("No hay canciones en la lista")
            return None
        
        # Navegar a la siguiente canción
        if self.actual.siguiente:
            self.actual = self.actual.siguiente
        else:
            self.actual = self.primera
        
        # Actualizar historial
        self.historial.append(self.actual)
        if len(self.historial) > 5:
            self.historial.pop(0)
        
        print("\n________________________________________________________________")
        print(f"Reproduciendo: {self.actual}")
        self.mostrar_recomendaciones()
        return self.actual
    
    def anterior_cancion(self) -> Optional[Cancion]:
        """
        Retrocede a la canción anterior en la playlist.

        Returns:
            La canción anterior o None si la playlist está vacía
        """
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
        """Muestra las recomendaciones basadas en la canción actual."""
        if self.actual:
            print("\nRecomendaciones basadas en tu música:")
            recomendaciones = self.sistema_recomendacion.recomendar_canciones(self.actual, self.historial)
            for i, cancion in enumerate(recomendaciones, 1):
                print(f"{i}. {cancion}")
    
    def mostrar_playlist(self):
        """Muestra todas las canciones añadidas a la playlist ."""
        if not self.primera:
            print("No hay canciones en la lista")
            return
        
        print("\nPlaylist completa:")
        actual = self.primera
        while actual:
            estado = "► " if actual == self.actual else "  "
            print(f"{estado}{actual}")
            actual = actual.siguiente

def main():
    """
    Función principal para demostrar el uso del reproductor de música.
    """
    reproductor = ReproductorMusica()
    
    # Agregar algunas canciones de ejemplo
    reproductor.agregar_cancion("Tengo fe", "Feid", "Reggaeton", 136)
    reproductor.agregar_cancion("Tusa", "Karol G", "Reggaeton", 194)
    reproductor.agregar_cancion("Hasta el Amanecer", "Nicky Jam", "Reggaeton", 238)
    
    # Mostrar playlist inicial
    reproductor.mostrar_playlist()
    
    # Probar navegación
    print("\nProbando navegación:")
    reproductor.siguiente_cancion()
    reproductor.siguiente_cancion()
    reproductor.anterior_cancion()
    
    # Eliminar una canción
    reproductor.eliminar_cancion("Tengo fe")
    
    # Mostrar playlist actualizada
    reproductor.mostrar_playlist()

if __name__ == "__main__":
    main()