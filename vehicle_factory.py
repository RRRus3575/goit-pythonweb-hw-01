from abc import ABC, abstractmethod
import logging

# Налаштування логування
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


# Абстрактний базовий клас Vehicle
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self) -> None:
        pass


# Класи транспорту
class Car(Vehicle):
    def __init__(self, model: str) -> None:
        self.model = model

    def start_engine(self) -> None:
        logging.info(f"{self.model} engine started!")


class Motorcycle(Vehicle):
    def __init__(self, model: str) -> None:
        self.model = model

    def start_engine(self) -> None:
        logging.info(f"{self.model} engine started!")


# Абстрактний базовий клас Factory
class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, model: str) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self, model: str) -> Motorcycle:
        pass


# Фабрики
class USVehicleFactory(VehicleFactory):
    def create_car(self, model: str) -> Car:
        return Car(f"{model} (US Spec)")

    def create_motorcycle(self, model: str) -> Motorcycle:
        return Motorcycle(f"{model} (US Spec)")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, model: str) -> Car:
        return Car(f"{model} (EU Spec)")

    def create_motorcycle(self, model: str) -> Motorcycle:
        return Motorcycle(f"{model} (EU Spec)")


# Використання фабрик для створення транспортних засобів
def main() -> None:
    # Створення фабрики для США
    us_factory = USVehicleFactory()
    us_car = us_factory.create_car("Ford Mustang")
    us_motorcycle = us_factory.create_motorcycle("Harley-Davidson")

    us_car.start_engine()
    us_motorcycle.start_engine()

    logging.info("-" * 40)

    # Створення фабрики для Європи
    eu_factory = EUVehicleFactory()
    eu_car = eu_factory.create_car("BMW M3")
    eu_motorcycle = eu_factory.create_motorcycle("Ducati Panigale")

    eu_car.start_engine()
    eu_motorcycle.start_engine()


# Запуск функції
if __name__ == "__main__":
    main()
