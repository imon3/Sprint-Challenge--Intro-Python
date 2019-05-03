# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
# BASE CLASS


class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model


class FlightVehicle(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)


class Starship(FlightVehicle):
    def __init__(self, make, model):
        super().__init__(make, model)
