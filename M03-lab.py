class Vehicle:
    def __init__(self, type):
        self.type = input('What is the type of Vehicle?')


class Car(Vehicle):
    pass


print(issubclass(Car, Vehicle))
