from vehicle_base import VehicleBase
class Ship(VehicleBase):
    def __init__(self, weight, max_weight):
        self.weight = weight
        self.max_weight = max_weight
    def mowe(self):	# Метод для корабля
        print("Плыву по морю")