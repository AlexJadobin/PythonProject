from pydantic import BaseModel
from exceptions import LowFuelError, ValueError
#from homework_08.exceptions import LowFuelError, ValueError

class VehicleBase(BaseModel):   # Класс транспортного средства
        color: str

class Car(VehicleBase):     # Класс Автомобиля
    fuel: int
    started: bool

    def start(self):    # Заводим двигатель, при этом меняем started c False на True
        if not(self.started):
           if self.fuel > 0:
               self.started = True
               print('Двигатель заведен, Автомобиль готов к движению, топливо:', self.fuel, 'литров, можно ехать')
           else:
               raise LowFuelError('Исключение. Топлива нет, толкаем авто до заправки')


    def stop(self):     # Команда остановить двигатель. Меняет started c True на False
        if self.started:
            self.started = False
            print('двигатель остановлен, started:', self.started)
            print('Хорошо покатались')
        else:
            print('не надо глушить уже остановленый двигатель')

class Plane(VehicleBase):   # Класс самолета
    cargo: int          # Вес груза
    max_cargo: int      # Допустимое максимальное значение груза
    dop_cargo: int      # Значение добавляемого груза
    #zagruzka: int       # Значение груза до разгрузки

    def add_cargo(self):    # Проводим погрузку самолета и ведем контроль возможного перегруза
        self.cargo = self.cargo + self.dop_cargo
        razgruz = self.cargo - self.max_cargo
        if self.cargo <= self.max_cargo:
            print('Вес груза после погрузки:', self.cargo, ', не превышает максимальное значение:', self.max_cargo, ', возможна догрузка:', abs(razgruz))
        else:
            print('Кажется, что последняя добавка груза была избыточной. похоже, что мы никуда не полетим')
            print('Необходимо c высадить часть пассажиров или в крайнем случае вынести их чемоданы, общим весом: ', razgruz)
            raise ValueError('Вес груза: ', self.cargo, ' превысил максимум: ', self.max_cargo, 'необходимо выгрузить: ', razgruz)

    def remove_all_cargo(self): # запоминаем значение self.cargo в переменную razgruz, затем обнуляем self.cargo и возвращаем переменную razgruz
        razgruz = self.cargo
        self.cargo = 0
        print('Вес доставленного груза в Аэропорт назначения составляет:', razgruz)
        return razgruz

def main():
# Пример 1: нормальный старта заправленного автомобиля и дальнейшей его остановки
    car = Car(color = 'White', started = False, fuel = 30)
    print(car)
    car.start()
    car.stop()
    print('---')
# Пример 2: попытка старта не заправленного автомобиля вызывает исключение и выход из программы
    #car = Car(color='White', started=False, fuel=0)
    #car.start()

# Пример 3: нормальная загрузка самолета, вывод информации о текущем весе груза,максимальном весе и значение возможной догрузки
    plane = Plane(color = 'White', cargo = 0, max_cargo = 30, dop_cargo = 20)
    print(plane)
    plane.add_cargo()
    print('---')
# Пример 4: попытка перегруза самолета вызывает исключение и выход из программы
    #plane.add_cargo()

# Разгрузка самолета после доставки груза в Аэропорт назначения
    plane.remove_all_cargo()
    print(plane)

if __name__ == '__main__':
    main()