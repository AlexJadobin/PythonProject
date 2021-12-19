# Занятие №5
# 3
class VehicleBase:
    def __init__(self, weight):
        self.weight = weight
    def mowe(self):
        print("Выполняю движение")
    def __str__(self):
        return (f"вес={self.weight}")

v1 = VehicleBase(50)
print(isinstance(v1, VehicleBase))
print('weight = ', v1.weight)
v1.mowe()
print('--')
# 4
class Ship(VehicleBase):
    def __init__(self, weight, max_weight):
        self.weight = weight
        self.max_weight = max_weight
    def set_sail(self):
        print('Поднять паруса')
    def mowe(self):
        print("Плыву по морю")
    def __str__(self):
        return ( f"вес={self.weight}"
                 f" максимальный вес={self.max_weight}"
                 )

ship1 =Ship(100,150)
print(ship1)
ship1.set_sail()
ship1.mowe()
print('--')

# 5
class Plane(Ship):
    def __init__(self, weight, max_weight, cargo):
        super().__init__(weight, max_weight)
        self.cargo = cargo

    def add_cargo(cargo):
        cargo = [2, 4, 6, 8, 10, 12]
        for n in cargo:
            n_sum = n + 3
            print(Plane)
            print(f"{n} + 3, = {int(n_sum)}")

    def mowe(self):
        print('Лечу по воздуху')

plane1 = Plane(50,100,10)
print(plane1)
plane1.mowe()
plane1.add_cargo()











