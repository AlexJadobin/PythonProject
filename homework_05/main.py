# 3
class VehicleBase:
    pass
def __init__(self, weight):
    self.weight = weight
v1 = VehicleBase()
print(isinstance(v1, VehicleBase))
v1.weight = 10
#v1.weight = '10'
print('weight = ', v1.weight)
# 4
class Ship(VehicleBase):
    def __init__(self, weight, max_weight):
        super.__init__(weight, max_weight)
    def set_sail(self):
        print('Поднять паруса')
# 5
class Plane(VehicleBase):
    def __init__(self, weight, max_weight, cargo):
        super(Plane, self).__init__(weight, max_weight, cargo)
        self.cargo = 0

    def add_cargo(self, int_num):
        self.int_num = int_num
        self.cargo = self.cargo + self.int_num
        return self.int_num









