class Animal:
    def __init__(self, nombre, edad, tipo):
        self.nombre=nombre
        self.edad=edad
        self.tipo=tipo

    def __str__(self):
        return f"nombre:{self.nombre}, edad:{self.años}, tipo:{self.tipo}"
class Node:
    def __init__ (self, animal):
        self.animal=animal
        self.next=None

class Lista_enlazada:
    def __init__(self):
        self.cabeza=None
    
    def agregar_animal(self, animal):
        nuevo_nodo = Node(animal)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.next is not None:
                if nodo_actual.animal.nombre==animal.nombre:
                    print(f"el animal {animal.nombre} ya existe en la lista")
                    return
                nodo_actual=nodo_actual.next
            if nodo_actual.animal.nombre==animal.nombre:
                print(f"el animal {animal.nombre}ya existe en la lista")
    
    def buscar(self, dato):
        nodo_actual = self.cabeza
        posicion = 0
        while nodo_actual is not None:
            if nodo_actual.data == dato:
                return posicion +1 
            nodo_actual = nodo_actual.next
            posicion += 1
        return -1  
lista = Lista_enlazada()
lista.agregar_nodo("Aguila")
lista.agregar_nodo("Pantera")
lista.agregar_nodo("Vaca")
lista.agregar_nodo("Leon")
lista.agregar_nodo("Jirafa")

agg_animal=str(input("Que animal desea agregar: "))
if agg_animal==Lista_enlazada:
    print("el animal ya esta en el zoologico")
else:
    print("animal añadido")


