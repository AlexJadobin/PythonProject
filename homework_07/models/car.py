from homework_07.exceptions import LowFuelError
from homework_07.exceptions import NotEnoughFuel

class Car:
    def __init__(self, weight, started, fuel, fuel_consumption):    # инициализация
        self.weight = weight    # int, вес автомобиля
        self.started = started  # bool, состояние “заведён” или нет
        self.fuel = fuel        # int, условное количество оставшегося топлива
        self.fuel_consumption = fuel_consumption    # 5. int, условное значение,
        # сколько единиц топлива расходуется на единицу расстояния
    def mowe(self):	# Метод для Авто
        print("Я Автомобиль, Двигаюсь по дороге")
    def start(self):
        try:
            if not(self.started):
                if self.fuel > 0:
                    self.started = 1
                    print('двигатель заведен')
                    #return True
                else:
                    raise LowFuelError
        except(LowFuelError):
            print('Исключение. Топлива нет, толкаем авто до заправки')
            return False
        else:
            print('Автомобиль готов, топливо:',self.fuel,'литров, можно ехать')
        finally:
            print('Хорошо покатались')
            print('---')

    def move(self,distance):
        try:
            if self.fuel < self.fuel_consumption * distance:
                raise NotEnoughFuel
        except(NotEnoughFuel):
            print('Исключение: недостаточно топлива на поездку',self.fuel,'литров, необходимо',self.fuel_consumption * distance, 'литров, а лучше полный бак!!!')
            print('---------')
        else:
            self.fuel -= self.fuel_consumption * distance
            print('Проехали ', distance, ' км, Остаток топлива : ',self.fuel, ' литра(ов)')
            print('---')

#car = Car(weight=800,started=0,fuel=10,fuel_consumption=3)
#car.mowe()