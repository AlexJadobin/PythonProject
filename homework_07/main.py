from models.vehicle_base import VehicleBase
from models.ship import Ship
from models.car import Car

def main():
    ship = Ship()
    ship.move() # Корабль

    car = Car()
    car.move() # Автомобиль

if __name__ == '__main__':
    main()


