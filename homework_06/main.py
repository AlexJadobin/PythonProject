class Car:
    def __init__(self, weight, started, fuel, fuel_consumption):    # инициализация
        self.weight = weight    # int, вес автомобиля
        self.started = started  # bool, состояние “заведён” или нет
        self.fuel = fuel        # int, условное количество оставшегося топлива
        self.fuel_consumption = fuel_consumption    # 5. int, условное значение,
        # сколько единиц топлива расходуется на единицу расстояния
    def start(self):
        if self.started == 'заведено':
            print('Можно ехать')
            return True
        else:
            print('Авто не заведен, ехать нельзя, необходимо проверить уровень топлива')
            self.started = False
        if self.started == False:
            if self.fuel > 0:
                self.started = True
                print('Топлива имеется, авто заведен')
                return True
            else:
                print('Авто не завелся, так как остаток топлива =  ', self.fuel)
moy_car = Car(800,'незаведено',25,10)
print(moy_car.start())





