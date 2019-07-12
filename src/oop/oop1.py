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

class Vehicle:
    pass

class GroundVehicle(Vehicle):
    pass
    #inherits from Vehicle

class Car(GroundVehicle):
    pass
    # inherits from GroundVehicle

class Motorcycle(GroundVehicle):
    pass
    # inherits from GroundVehicle

class FlightVehicle(Vehicle):
    pass
    # inherits from Vehicle

class Starship(FlightVehicle):
    pass
    # inherits from FlightVehicle

class Airplane(FlightVehicle):
    pass
    # inherits from FlightVehicle