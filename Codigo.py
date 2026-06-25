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
    def __init__(self, id, capacidad=350):
        super().__init__(id, velocidad=40, capacidad=capacidad, costo_por_km=3.0)

    def calcular_costo(self, distancia):
        return distancia * self.costo_por_km

class Camioneta(Vehiculo):
    def __init__(self, id, capacidad=500):
        super().__init__(id, velocidad=30, capacidad=capacidad, costo_por_km=5.0)

    def calcular_costo(self, distancia):
        return distancia * self.costo_por_km
    

# tarifas (usando strategy method)

class IEstrategiaTarifa(ABC):
    @abstractmethod
    def calcular_tarifa(self, costo_base):
        pass

class TarifaEstandar(IEstrategiaTarifa):
    def calcular_tarifa(self, costo_base):
        return costo_base

class TarifaUrgente(IEstrategiaTarifa):
    def calcular_tarifa(self, costo_base):
        return costo_base * 1.5  # recargo del 50%

class TarifaEco(IEstrategiaTarifa):
    def calcular_tarifa(self, costo_base):
        return costo_base * 0.8  # descuento del 20%

# 3. Clase Pedido
class Pedido:
    def __init__(self, id, peso, distancia, estrategia_tarifa=None):
        self.id = id
        self.peso = peso
        self.distancia = distancia
        self.vehiculo_asignado = None
        self.estrategia_tarifa = estrategia_tarifa or TarifaEstandar()

    def asignar_vehiculo(self, vehiculo):
        if vehiculo.capacidad >= self.peso:
            self.vehiculo_asignado = vehiculo
        else:
            # Aquí podrías usar una excepción personalizada en el futuro
            raise ValueError(f"El vehículo {vehiculo.id} no tiene capacidad para {self.peso}kg")
        
    def calcular_costo_total(self):
        if not self.vehiculo_asignado:
            raise ValueError("No hay vehículo asignado")
        costo_base = self.vehiculo_asignado.calcular_costo(self.distancia)
        return self.estrategia_tarifa.calcular_tarifa(costo_base)

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
                    costo_total = p.calcular_costo_total()
                    print(f"Pedido {p.id} ({p.peso}kg) asignado a {type(v).__name__} {v.id}. Costo con tarifa: ${costo_total:.2f}")
                    asignado = True
                    break
                except ValueError:
                    continue
            if not asignado:
                print(f"Pedido {p.id}: No hay vehículos disponibles con capacidad suficiente.")

# Ejemplo de uso:
"""gestor = GestorLogistica()
gestor.agregar_vehiculo(Moto("MOTO-001"))
gestor.agregar_vehiculo(Auto("AUTO-001"))
gestor.agregar_vehiculo(Camioneta("CAM-001"))

gestor.agregar_pedido(Pedido("P-01", 10, 5))   # Moto
gestor.agregar_pedido(Pedido("P-02", 200, 10)) # Auto
gestor.agregar_pedido(Pedido("P-03", 600, 20)) # Ninguno (supera la capacidad de la camioneta)
gestor.agregar_pedido(Pedido("P-04", 400, 15)) # Camioneta

gestor.procesar_pedidos() """

# Crear vehículos
moto = Moto("MOTO-001")
auto = Auto("AUTO-001")
camioneta = Camioneta("CAM-001")

# Crear gestor
gestor = GestorLogistica()
gestor.agregar_vehiculo(moto)
gestor.agregar_vehiculo(auto)
gestor.agregar_vehiculo(camioneta)

# Crear pedidos con distintas estrategias de tarifa
pedido1 = Pedido("P-01", peso=10, distancia=5, estrategia_tarifa=TarifaEstandar())   # Moto con tarifa estándar
pedido2 = Pedido("P-02", peso=200, distancia=10, estrategia_tarifa=TarifaUrgente())  # Auto con tarifa urgente
pedido3 = Pedido("P-03", peso=400, distancia=15, estrategia_tarifa=TarifaEco())      # Camioneta con tarifa eco
pedido4 = Pedido("P-04", peso=600, distancia=20, estrategia_tarifa=TarifaEstandar()) # Ningún vehículo (supera capacidad)

# Agregar pedidos al gestor
gestor.agregar_pedido(pedido1)
gestor.agregar_pedido(pedido2)
gestor.agregar_pedido(pedido3)
gestor.agregar_pedido(pedido4)

# Procesar pedidos
gestor.procesar_pedidos()

