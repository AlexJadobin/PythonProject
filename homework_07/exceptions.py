# объявление исключений
class LowFuelError(Exception):
    pass
print('Объявлен класс LowFuelError')

class NotEnoughFuel(Exception):
    pass
print('Объявлен класс NotEnoughFuel')