#Andrés Felipe Chamorro Pérez

from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class MaterialBiblioteca(ABC):
    def __init__(self, titulo):
        self.__titulo = titulo
        self.__disponible = True

    def get_titulo(self):
        return self.__titulo

    def esta_disponible(self):
        return self.__disponible

    def prestar(self):
        self.__disponible = False

    def devolver(self):
        self.__disponible = True

    @abstractmethod
    def calcular_fecha_devolucion(self, fecha_prestamo):
        pass

    @abstractmethod
    def obtener_tipo(self):
        pass

    @abstractmethod
    def obtener_detalles(self):
        pass


class Libro(MaterialBiblioteca):
    def calcular_fecha_devolucion(self, fecha_prestamo):
        return fecha_prestamo + timedelta(days=15)

    def obtener_tipo(self):
        return "Libro"

    def obtener_detalles(self):
        return f"{self.get_titulo()} ({self.obtener_tipo()})"


class Revista(MaterialBiblioteca):
    def calcular_fecha_devolucion(self, fecha_prestamo):
        return fecha_prestamo + timedelta(days=7)

    def obtener_tipo(self):
        return "Revista"

    def obtener_detalles(self):
        return f"{self.get_titulo()} ({self.obtener_tipo()})"


class MaterialAudiovisual(MaterialBiblioteca):
    def calcular_fecha_devolucion(self, fecha_prestamo):
        return fecha_prestamo + timedelta(days=3)

    def obtener_tipo(self):
        return "Material Audiovisual"

    def obtener_detalles(self):
        return f"{self.get_titulo()} ({self.obtener_tipo()})"


class Usuario:
    def __init__(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre


class Prestamo:
    def __init__(self, usuario, material):
        self.usuario = usuario
        self.material = material
        self.fecha_prestamo = datetime.now().date()
        self.fecha_devolucion = material.calcular_fecha_devolucion(self.fecha_prestamo)
        material.prestar()

    def __str__(self):
        return (f"Usuario: {self.usuario.get_nombre()} | "
                f"Material: {self.material.obtener_detalles()} | "
                f"Fecha préstamo: {self.fecha_prestamo} | "
                f"Fecha devolución: {self.fecha_devolucion}")



libro = Libro("Cien años de soledad")
revista = Revista("National Geographic")
audiovisual = MaterialAudiovisual("El Padrino")

usuario1 = Usuario("Juan Camilo Impata")
usuario2 = Usuario("Andrés Felipe Chamorro")

prestamo1 = Prestamo(usuario1, libro)
prestamo2 = Prestamo(usuario2, revista)

print("\n--- Préstamos realizados ---")
print(prestamo1)
print(prestamo2)

print("\n--- Disponibilidad de materiales ---")
for material in [libro, revista, audiovisual]:
    print(f"{material.get_titulo()}: {material.esta_disponible()}")
