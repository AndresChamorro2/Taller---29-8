from abc import ABC, abstractmethod
from typing import List
from datetime import datetime


class Vehiculo(ABC):
    @abstractmethod
    def descripcion(self) -> str:
        pass

    @abstractmethod
    def precio_final(self) -> int:
        pass


class VehiculoBase(Vehiculo):
    def __init__(self, marca: str, modelo: str, año: int, precio_base: int, estado: str):
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año
        self.__precio_base = precio_base
        self.__estado = estado.lower()
        self.__vendido = False

    @property
    def año(self): return self.__año
    @property
    def precio_base(self): return self.__precio_base
    @property
    def estado(self): return self.__estado
    @property
    def marca(self): return self.__marca
    @property
    def modelo(self): return self.__modelo
    @property
    def vendido(self): return self.__vendido

    def vender(self):
        if self.__vendido:
            raise ValueError("El vehículo ya fue vendido.")
        self.__vendido = True

    def calcular_precio_estado(self, precio: float) -> float:
        if self.__estado == "nuevo":
            return precio
        elif self.__estado == "usado":
            año_actual = datetime.now().year
            antiguedad = año_actual - self.__año
            descuento = 0.10 * precio + (0.01 * (antiguedad // 2)) * precio
            return max(precio - descuento, precio * 0.5)
        else:
            return precio


class Auto(VehiculoBase):
    def __init__(self, marca, modelo, año, precio_base, estado, puertas: int):
        super().__init__(marca, modelo, año, precio_base, estado)
        self.__puertas = puertas

    def descripcion(self) -> str:
        return f"{self.marca} {self.modelo} ({self.año}) - {self.__puertas} puertas - {self.estado.upper()}"

    def precio_final(self) -> int:
        precio = self.precio_base + (0.19 * self.precio_base)
        return int(self.calcular_precio_estado(precio))


class Motocicleta(VehiculoBase):
    def __init__(self, marca, modelo, año, precio_base, estado, cilindraje: int):
        super().__init__(marca, modelo, año, precio_base, estado)
        self.__cilindraje = cilindraje

    def descripcion(self) -> str:
        return f"{self.marca} {self.modelo} ({self.año}) - {self.__cilindraje}cc - {self.estado.upper()}"

    def precio_final(self) -> int:
        precio = self.precio_base + (0.12 * self.precio_base)
        return int(self.calcular_precio_estado(precio))


class Concesionario:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self._inventario: List[Vehiculo] = []

    def agregar_vehiculo(self, v: Vehiculo):
        self._inventario.append(v)

    def listar_inventario(self):
        print(f"\n📋 Inventario en {self.nombre}")
        if not self._inventario:
            print("No hay vehículos en el inventario.")
            return
        for i, v in enumerate(self._inventario, 1):
            estado = "VENDIDO" if getattr(v, "vendido", False) else "DISPONIBLE"
            print(f"{i}. {v.descripcion()} — {estado} — Precio: ${v.precio_final():,} COP")

    def vender_vehiculo(self, indice: int):
        if indice < 1 or indice > len(self._inventario):
            raise IndexError("Índice fuera de rango.")
        veh = self._inventario[indice - 1]
        veh.vender()
        print(f"\n✅ Se vendió: {veh.descripcion()} por ${veh.precio_final():,} COP")


def menu():
    c = Concesionario("Autos Colombia S.A.")

    while True:
        print("\n--- MENÚ CONCESIONARIO ---")
        print("1. Agregar Auto")
        print("2. Agregar Motocicleta")
        print("3. Listar Inventario")
        print("4. Vender Vehículo")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            año = int(input("Año: "))
            precio = int(input("Precio base en COP: "))
            estado = input("Estado (nuevo/usado): ").lower()
            puertas = int(input("Número de puertas: "))
            c.agregar_vehiculo(Auto(marca, modelo, año, precio, estado, puertas))
            print("✅ Auto agregado.")

        elif opcion == "2":
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            año = int(input("Año: "))
            precio = int(input("Precio base en COP: "))
            estado = input("Estado (nuevo/usado): ").lower()
            cilindraje = int(input("Cilindraje (cc): "))
            c.agregar_vehiculo(Motocicleta(marca, modelo, año, precio, estado, cilindraje))
            print("✅ Motocicleta agregada.")

        elif opcion == "3":
            print("\n=== LISTADO SOLO DE INVENTARIO ===")
            c.listar_inventario()

        elif opcion == "4":
            if not c._inventario:
                print("\n⚠️ No hay vehículos para vender.")
                continue
            print("\n=== PROCESO DE VENTA ===")
            for i, v in enumerate(c._inventario, 1):
                estado = "VENDIDO" if v.vendido else "DISPONIBLE"
                print(f"{i}. {v.descripcion()} — {estado}")
            indice = int(input("Número de vehículo a vender: "))
            try:
                c.vender_vehiculo(indice)
            except Exception as e:
                print(f"⚠️ Error: {e}")

        elif opcion == "5":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("⚠️ Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    menu()
