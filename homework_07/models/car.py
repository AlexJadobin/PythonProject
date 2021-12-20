class Car:
    def __init__(self, weight, started, fuel, fuel_consumption):    # инициализация
        self.weight = weight    # int, вес автомобиля
        self.started = started  # bool, состояние “заведён” или нет
        self.fuel = fuel        # int, условное количество оставшегося топлива
        self.fuel_consumption = fuel_consumption    # 5. int, условное значение,
        # сколько единиц топлива расходуется на единицу расстояния
    def mowe(self):	# Метод для Авто
        print("Движение по дороге")