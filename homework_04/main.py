# занятие №4 , задание №1, вариант №1
# выбор списка простых чисел и формирование списка кубов простых чисел
sps_prost = []
kub_sps_prost =[]
f = 70
def prostye(n):
    for j in range(1, n+1):
        for i in range(2, j+1):
            if j % i == 0 and i != j:
                break
            else:
                if i == j:
                    sps_prost.append(j)
                    a = j ** 3
                    kub_sps_prost.append(a)
    return

prostye(f)

print("задание №1, вариант №1: выбор простых чисел до значения =", f, 'в список sps_prost')
print(sps_prost)
print('--')
print("расчёт кубов простых чисел до значения =", f, 'в список kub_sps_prost')
print(kub_sps_prost)
print('____________')



# №4, задание №1, вариант №2
def kub_number(*numbers, power=3):
    return [num ** power for num in numbers]

print("задание №1, вариант №2: расчет и печать кубов целых чисел ")
print(kub_number(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
print('--')

# №4, задание №1, вариант №3
kub_sps = []
def kub_number(*numbers, power=3):
    for j in numbers:
        i = j ** power
        kub_sps.append(i)
    return

kub_number(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
print("задание №1, вариант №3: расчет, формирование списка [kub_sps] кубов целых чисел и печать списка")
print(kub_sps)
print('____________')



# №4, задание 2, исправление замечания Сурена
def is_prostye(n):  # функция проверки числа на вхождение в простые чиста
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for j in range(3, n, 2):
        if n % j == 0:
            return False
    return True

print('____________')
print('задание №2, исправленная функция по замечанию Сурена')
ODD = "chet"
EVEN = "nechet"
PRIME = "prost"
def filter_numbers(*num, key):
    vixod_filters = [] # создан пустой выход
    if key == ODD:
        for i in num:
	        if i % 2 == 0:
	            vixod_filters.append(i)
        return vixod_filters

    if key == EVEN:
         for i in num:
            if i % 2 != 0:
                vixod_filters.append(i)
         return vixod_filters

    if key == PRIME:
        return list(filter(is_prostye, num))

print('Выбор простых чисел: ', filter_numbers(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17, key=PRIME))
print('Выбор четных чисел: ', filter_numbers(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17, key=ODD))
print('Выбор нечетных чисел: ', filter_numbers(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17, key=EVEN))