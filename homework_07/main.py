from models.vehicle_base import VehicleBase
from models.ship import Ship
from models.car import Car
from models.vb import VB

def main():
    vb = VehicleBase(10)
    vb.mowe() # Любой транспорт

    v2 = VB(4, 2)
    v2.mowe() # Горный двухколесный велосипед

    ship = Ship(100,200)
    ship.mowe() # Корабль

    car = Car(weight=800,started=0,fuel=50,fuel_consumption=3)
    car.mowe() # Автомобиль
    print("Пример №1: если топлива было 50 литров, а расход 5 л/10 км, то проехав 10 км, у нас топлива 0 литров")
    car = Car(weight=800, started=0, fuel=50, fuel_consumption=5)
    car.start()
    s = 10  # дистанция 10 километров
    car.move(s)
    print("")

    print("Пример №2: если топлива было 10 литров, а расход 3 л/км, то проехав 2 км, топлива должно остаться 4 литра")
    car = Car(weight=800, started=0, fuel=10, fuel_consumption=3)
    car.start()
    s = 2  # дистанция 2 километра
    car.move(s)

    print("Пример №3: если топлива было 0 литров, а нужно срочно ехать!!!")
    car = Car(weight=800, started=0, fuel=0, fuel_consumption=5)
    car.start()

    print("Пример №4: если топлива было 10 литров, а расход 3 л/км, а необходимо проехать 5 км, то куда мы доедем ?")
    car = Car(weight=800, started=0, fuel=10, fuel_consumption=3)
    s = 5  # дистанция 5 километра
    car.move(s)


if __name__ == '__main__':
    main()


