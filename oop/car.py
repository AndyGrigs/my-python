class Car:

    def __init__(self, brand, model, year) -> None:
        self.brand = brand
        self.model = model
        self.year = year
        self.is_engine_on = False

    def start_engine(self):
        self.is_engine_on = True
        print(f"{self.brand} {self.model}'s engine started.")

    def stop_engine(self):
        self.is_engine_on = False
        print(f"{self.brand} {self.model}'s engine stopped.")

    def drive(self, distance):
        if self.is_engine_on:
            print(f"Driving {distance} km.")
        else:
            print("Engine must be turned on before driving.")

my_car = Car("Toyota", "Corolla", 2020)

# Виклик методів для екземпляра my_car
my_car.start_engine()
print(f"My car is a {my_car.year} {my_car.brand} {my_car.model}.")
my_car.drive(100)
my_car.stop_engine()