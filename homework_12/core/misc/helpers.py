def is_prostye(n):  # функция проверки числа на вхождение в простые чиста
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for j in range(3, n, 2):
        if n % j == 0:
            return False
    return True

def filter_numbers(*num):
    return list(filter(is_prostye, num))
print('Выбор простых чисел: ', filter_numbers(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17))