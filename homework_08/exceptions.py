# объявление исключений
class LowFuelError(Exception):
    pass
    #print('Закончилось топливо')   # вводил для трассировки выполнения программы

class ValueError(Exception):
    pass
    #print('Превышен лимит груза')