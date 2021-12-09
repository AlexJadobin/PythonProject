# занятие №4 , задание №1  выбор списка простых чисел и формирование списка кубов простых чисел
sps_prost = [1]
kub_sps_prost =[1]
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

print("выбор простых чисел до значения =", f, 'в список sps_prost')
print(sps_prost)
print('--')
print("расчёт кубов простых чисел до значения =", f, 'в список kub_sps_prost')
print(kub_sps_prost)
print('____________')

# №4 вариант №2
def kub_number(*numbers, power=3):
    return [num ** power for num in numbers]

print("расчет и печать кубов целых чисел ")
print(kub_number(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
print('--')

# №4 вариант №3
kub_sps = []
def kub_number(*numbers, power=3):
    for j in numbers:
        i = j ** power
        kub_sps.append(i)
    return

kub_number(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
print("расчет, формирование списка [kub_sps] кубов целых чисел и печать списка")
print(kub_sps)
print('____________')



# задание №2, вариант №1

print('____________')
print('задание №2, вариант №1')
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# четные числа
def filter_odd(vxod_num):
    if (vxod_num % 2) == 0:
        return True
    else:
        return False

vixod_filter = filter(filter_odd, numbers)
print("Четные числа: ", list(vixod_filter))

# нечетные чисела
def filter_odd(vxod_num):
    if (vxod_num % 2) > 0:
        return True
    else:
        return False

vixod_filter = filter(filter_odd, numbers)
print("Нечетные числа: ", list(vixod_filter))

# простые числа
def filter_odd(vxod_num):
    for i in range(2, vxod_num):
        if vxod_num % i == 0:
            return False
        else:
            return True

vixod_filter = filter(filter_odd, numbers)
print("Простые числа: ", list(vixod_filter))


# задание №2, вариант №2
# filter types

print('____________')
print('задание №2, вариант №2')
ODD = "chet"
EVEN = "nechet"
PRIME = "prost"

def filter_numbers(y):
    if x == PRIME:
        for j in range(1, y + 1):
            # print('цикл 1 j=', j, ' n=', n)
            for i in range(2, j + 1):
                # print('вложенный цикл 2 i=', i, ' j=', j)
                if j % i == 0 and i != j:
                    break
                else:
                    if i == j:
                        vixod_filters.append(j)
                        # print('значение i= ', i, 'значение j= ', j)
        # print(sps_prost)

    else:
        for i in range(1, y):
	        if i % 2 == 0:
	            if x == ODD:
		            vixod_filters.append(i)
		            continue
	            if x == EVEN:
		            continue
	        else:
	            if x == ODD:
		            continue
	            if x == EVEN:
		            vixod_filters.append(i)
		            continue

    return

num = 80
#num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# четные
vixod_filters = []
x = ODD
filter_numbers(num)
print('выбор четных чисел ', vixod_filters)

# нечетные
vixod_filters = []
x = EVEN
filter_numbers(num)
print('выбор нечетных чисел ', vixod_filters)

# простые
vixod_filters = [1]
x = PRIME
filter_numbers(num)
print('выбор простых чисел ', vixod_filters)