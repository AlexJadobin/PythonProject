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

# 5
class Plane(Ship):
    def __init__(self, weight, max_weight, cargo):
        super().__init__(weight, max_weight)
        self.cargo = cargo

    def add_cargo(self, dogruz):
        self.cargo += dogruz
        #print(Plane)
        #print(f"{n} + 3, = {int(n_sum)}")
        print('После догрузки: ', str(dogruz), ' общий вес груза стал = ', str(self.cargo), 'вызов метода add_cargo')

    def mowe(self):
        print('Лечу по воздуху')


def main(): # функция main
    ship1 = Ship(100, 150)
    print(ship1)
    ship1.set_sail()
    ship1.mowe()
    print('--')
    plane1 = Plane(50,100,10) # груз равен 10
    print(plane1)
    plane1.mowe()
    plane1.add_cargo(5) # после отработки метода, вес груза cargo должен увеличиться на 5
    plane1.add_cargo(4)  # после отработки метода, вес груза cargo должен увеличиться на 4
    plane1.add_cargo(6)  # после отработки метода, вес груза cargo должен увеличиться на 6

main()  # вызов фукции, вывод информации.











