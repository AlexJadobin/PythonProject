class VehicleBase:
    def __init__(self, weight):
        self.weight = weight
    def mowe(self):  # Метод для любого транспорта
        print("Я Транспорт, Выполняю движение")

#v1 = VehicleBase(10)
#v1.mowe()