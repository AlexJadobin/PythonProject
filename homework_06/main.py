class Car:
    def __init__(self, weight, started, fuel, fuel_consumption):    # инициализация
        self.weight = weight    # int, вес автомобиля
        self.started = started  # bool, состояние “заведён” или нет
        self.fuel = fuel        # int, условное количество оставшегося топлива
        self.fuel_consumption = fuel_consumption    # int, условное значение, расхода топлива на единицу расстояния
    def start(self):
        if not(self.started):
            if self.fuel > 0:
                self.started = True
                print('Двигатель заведен, Автомобиль готов, топливо:', self.fuel, 'литров, можно ехать')
                print('Хорошо покатались')
                print('---')
            else:
                raise LowFuelError("Исключение. Топлива нет, толкаем авто до заправки")

    def move(self,distance):
        if self.fuel < self.fuel_consumption * distance + 4:
            raise NotEnoughFuel('недостаточно топлива на поездку',self.fuel,'литров, необходимо',self.fuel_consumption * distance, 'литров')
        else:
            self.fuel -= self.fuel_consumption * distance
            print('Проехали ', distance, ' км, Остаток топлива : ',self.fuel, ' литра(ов)')
            print('---')

# объявление исключений
class LowFuelError(Exception):
    pass

class NotEnoughFuel(Exception):
    pass

print("Пример №1: если топлива было 60 литров, а расход 5 л/10 км, то проехав 10 км у нас остаётся топлива 10 литров")
car = Car(weight=800,started=0,fuel=60,fuel_consumption=5)
car.start()
s = 10  # дистанция 10 километров
car.move(s)
print("")

print("Пример №2: если топлива было 10 литров, а расход 3 л/км, то проехав 2 км, топлива должно остаться 4 литра")
car = Car(weight=800,started=0,fuel=10,fuel_consumption=3)
car.start()
s = 2  # дистанция 2 километра
car.move(s)

print("Пример №3: если топлива было 0 литров, а нужно срочно ехать!!!")
car = Car(weight=800,started=0,fuel=0,fuel_consumption=5)
car.start()

print("Пример №4: если топлива было 10 литров, а расход 3 л/км, а необходимо проехать 5 км, то куда мы доедем ?")
car = Car(weight=800,started=0,fuel=10,fuel_consumption=3)
s = 5  # дистанция 5 километра
car.move(s)