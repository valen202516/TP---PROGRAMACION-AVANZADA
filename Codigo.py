from abc import ABC, abstractmethod

# 1. Clase Base Abstracta (Herencia)
class Vehiculo(ABC):
    def __init__(self, id, velocidad, capacidad):
        self.id = id
        self.velocidad = velocidad # km/h
        self.capacidad = capacidad # kg

    @abstractmethod
    def calcular_costo(self, distancia):
        pass

    def calcular_tiempo(self, distancia):
        return distancia / self.velocidad

# 2. Clases Concretas (Polimorfismo)
class Dron(Vehiculo):
    def calcular_costo(self, distancia):
        return distancia * 0.5  # Costo bajo, rápido

class Bicicleta(Vehiculo):
    def calcular_costo(self, distancia):
        return 0  # Costo nulo (ecológico)

# 3. Clase Pedido
class Pedido:
    def __init__(self, id, peso, distancia):
        self.id = id
        self.peso = peso
        self.distancia = distancia
        self.vehiculo_asignado = None

    def asignar_vehiculo(self, vehiculo):
        if vehiculo.capacidad >= self.peso:
            self.vehiculo_asignado = vehiculo
        else:
            raise Exception(f"El vehículo {vehiculo.id} no tiene capacidad para {self.peso}kg")

# 4. Clase Gestor (La que administra todo)
class GestorLogistica:
    def __init__(self):
        self.vehiculos = []
        self.pedidos = []

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def procesar_pedidos(self):
        for p in self.pedidos:
            # Lógica simple de asignación
            for v in self.vehiculos:
                try:
                    p.asignar_vehiculo(v)
                    print(f"Pedido {p.id} asignado a {v.id}")
                    break
                except Exception as e:
                    continue
