from operator import contains


class Vehicle:
    def __init__(self, type):
        # Run validations to the recieved arguments
        self.type = type


class Car(Vehicle):
    def __init__(self, year, make, car_model, doors, roof):
        self.year = year
        self.make = make
        self.model = car_model
        self.doors = doors
        self.roof = roof


# Get Response
_type = input('What type of Vehicle is it?')

# Run type validator (Edit on Jun 26: I still have not gotten this part working, but everything else works)
if _type == 'car' or 'truck' or 'plane' or 'boat' or 'broomstick':

    _year = input(f'What is the Year of the Vehicle')
    _make = input(f'What is the Make of the Vehicle')
    _model = input(f'What is the Model of the Vehicle')
    _doors = input(f'Does the Vehicle have 2 or 4 doors?')
    _roof = input(f'Does the Vehicle have a sun roof or solid?')

    vehicle = Vehicle(_type)
    car = Car(_year, _make, _model, _doors, _roof)

    # Print Response
    print(f'Vehicle type: {vehicle.type}')
    print(f'Year: {car.year}')
    print(f'Make: {car.make}')
    print(f'Model: {car.model}')
    print(f'Doors: {car.doors}')
    print(f'Roof: {car.roof}')
else:
    print(f'{_type} is not an acceptable type')
