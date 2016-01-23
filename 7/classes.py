

class Car:

    def __init__(self, gas):
        self.gas = gas
        print("Car has {} Gas.".format(self.gas)

    def start(self):
        if self.gas > 0:
            print("Engine Start.")
        else:
            print("No Gas to Start.")

    def drive(self):
        if self.gas > 0:
            self.gas -= 1
            print("{} Gas.".format(self.gas))
            print("Brrrooom!  " * 9)
        else:
            print("Engine Stopped, Car Stopped.")


# Start and Drive the Car until it runs out of gas.
# Arrance y Maneja el auto hasta que se quede sin combustible.
my_car = Car()
my_car.start()

for index in range(5):
    my_car.drive()

assert my_car.gas == 0
