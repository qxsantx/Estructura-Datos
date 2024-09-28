class Vehiculo:
    def __init__(self, marca:str, combustible:str):
        self.marc=marca
        self.combustible=combustible
    def encender(self ):
        pass
    def arrancar(self ):
        pass
    def __str__(self):
        return f"el vehiculo {self.marca} utilizamos {self.combustible}"
    
carro=Vehiculo("BMW", "corriente")
print(carro)
print(type(carro))

class Moto (Vehiculo):
    def __init__(self,marca:str,combustible:str):
        super.__init__(marca, combustible)
    pass
class Carro(Vehiculo):
    def __init__(self, marca: str, combustible: str):
        super().__init__(marca, combustible)
    pass
motocicleta=Moto("Yamaha", "corriente")
mi_carro=Carro("mazda", "extra")

