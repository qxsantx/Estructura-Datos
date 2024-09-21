class Animal:
    def __init__(self, nombre, tipo, edad):
        self.nombre = nombre
        self.tipo = tipo
        self.edad = edad
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Tipo: {self.tipo}, Edad: {self.edad} años"

class Nodo:
    def __init__(self, animal):
        self.animal = animal
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, animal):
        if self.cabeza is None:
            self.cabeza = Nodo(animal)
            print(f"{animal.nombre} ({animal.tipo}) ha sido agregado a la lista.")
            return
        
        actual = self.cabeza
        while actual is not None:
            if actual.animal.nombre == animal.nombre and actual.animal.tipo == animal.tipo:
                print(f"{animal.nombre} ({animal.tipo}) ya está en la lista, no se agregará.")
                return
            if actual.siguiente is None:
                break
            actual = actual.siguiente
        
        actual.siguiente = Nodo(animal)
        print(f"{animal.nombre} ({animal.tipo}) ha sido agregado a la lista.")

    def mostrar_con_bucle(self):
        actual = self.cabeza
        if actual is None:
            print("La lista de animales está vacía.")
            return
        print("Lista de animales (con bucle):")
        while actual is not None:
            print(actual.animal)
            actual = actual.siguiente

    def mostrar_con_recursion(self, nodo):
        if nodo is None:
            return
        print(nodo.animal)
        self.mostrar_con_recursion(nodo.siguiente)

def agregar_animales_a_lista():
    zoologico = ListaEnlazada()

    while True:
        nombre = input("Ingrese el nombre del animal (o 'salir' para terminar): ")
        if nombre.lower() == 'salir':
            break

        tipo = input("Ingrese el tipo de animal: ")
        edad = input("Ingrese la edad del animal: ")
        
        animal = Animal(nombre, tipo, edad)  
        zoologico.agregar(animal)  

    return zoologico  

zoologico = agregar_animales_a_lista()

print("Mostrando animales con un bucle:")
zoologico.mostrar_con_bucle()

print("Mostrando animales con recursión:")
zoologico.mostrar_con_recursion(zoologico.cabeza)