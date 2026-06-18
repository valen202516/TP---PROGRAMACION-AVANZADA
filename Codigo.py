from abc import ABC, abstractmethod

# 1. Clase Base Abstracta
class Vehiculo(ABC):
    def __init__(self, id, velocidad, capacidad, costo_por_km):
        self.id = id
        self.velocidad = velocidad # km/h
        self.capacidad = capacidad # kg
        self.costo_por_km = costo_por_km

    @abstractmethod
    def calcular_costo(self, distancia):
        pass

    def calcular_tiempo(self, distancia):
        return distancia / self.velocidad

# 2. Clases Concretas
class Moto(Vehiculo):
    def __init__(self, id, capacidad=20): # Capacidad estándar moto
        super().__init__(id, velocidad=50, capacidad=capacidad, costo_por_km=1.5)

    def calcular_costo(self, distancia):
        return distancia * self.costo_por_km

class Auto(Vehiculo):
    def __init__(self, id, capacidad=100):
        super().__init__(id, velocidad=40, capacidad=capacidad, costo_por_km=3.0)

    def calcular_costo(self, distancia):
        return distancia * self.costo_por_km

class Camioneta(Vehiculo):
    def __init__(self, id, capacidad=500):
        super().__init__(id, velocidad=30, capacidad=capacidad, costo_por_km=5.0)

    def calcular_costo(self, distancia):
        return distancia * self.costo_por_km

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
            # Aquí podrías usar una excepción personalizada en el futuro
            raise ValueError(f"El vehículo {vehiculo.id} no tiene capacidad para {self.peso}kg")

# 4. Clase Gestor
class GestorLogistica:
    def __init__(self):
        self.vehiculos = []
        self.pedidos = []

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)
        
    def agregar_pedido(self, pedido):
        self.pedidos.append(pedido)

    def procesar_pedidos(self):
        print("\n--- Iniciando asignación de pedidos ---")
        for p in self.pedidos:
            asignado = False
            for v in self.vehiculos:
                try:
                    p.asignar_vehiculo(v)
                    costo = v.calcular_costo(p.distancia)
                    print(f"Pedido {p.id} ({p.peso}kg) asignado a {type(v).__name__} {v.id}. Costo: ${costo:.2f}")
                    asignado = True
                    break
                except ValueError:
                    continue
            if not asignado:
                print(f"Pedido {p.id}: No hay vehículos disponibles con capacidad suficiente.")

# Ejemplo de uso:
gestor = GestorLogistica()
gestor.agregar_vehiculo(Moto("MOTO-001"))
gestor.agregar_vehiculo(Auto("AUTO-001"))
gestor.agregar_vehiculo(Camioneta("CAM-001"))

gestor.agregar_pedido(Pedido("P-01", 10, 5))   # Moto
gestor.agregar_pedido(Pedido("P-02", 200, 10)) # Auto
gestor.agregar_pedido(Pedido("P-03", 600, 20)) # Ninguno (supera la capacidad de la camioneta)
gestor.agregar_pedido(Pedido("P-04", 400, 15)) # Camioneta

gestor.procesar_pedidos()
