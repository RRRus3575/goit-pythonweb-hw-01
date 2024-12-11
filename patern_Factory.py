from abc import ABC, abstractmethod

#Абстрактний базовий класс Vehicle

class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass


#Класи транспорту

class Car(Vehicle):
    def __init__(self, model):
        self.model = model

    def start_engine(self):
        print(f"{self.model} engine started!")

class Motorcycle(Vehicle):
    def __init__(self, model):
        self.model = model

    def start_engine(self):
        print(F"{self.model} engine started!")

#Абстрактний базовий класс Factory

class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self):
        pass
    def create_motorcycle(self):
        pass

#Фабрики

class USVehicleFactory(VehicleFactory):
    def create_car(self, model):
        return Car(f"{model} (US Spec)")
    def create_motorcycle(self, model):
        return Motorcycle(f"{model} (US Spec)")

class EUVehicleFactory(VehicleFactory):
    def create_car(self, model):
        return Car(f"{model} (EU Spec)")
    def create_motorcycle(self, model):
        return Motorcycle(f"{model} (EU Spec)")


# Використання фабрик для створення транспортних засобів

def main():
    # Створення фабрики для США
    us_factory = USVehicleFactory()
    us_car = us_factory.create_car("Ford Mustang")
    us_motorcycle = us_factory.create_motorcycle("Harley-Davidson")

    us_car.start_engine()  
    us_motorcycle.start_engine()  

    print("-" * 40)

    # Створення фабрики для Європи
    eu_factory = EUVehicleFactory()
    eu_car = eu_factory.create_car("BMW M3")
    eu_motorcycle = eu_factory.create_motorcycle("Ducati Panigale")

    eu_car.start_engine()  
    eu_motorcycle.start_engine()  


#Запуск функції

if __name__ == "__main__":
    main()