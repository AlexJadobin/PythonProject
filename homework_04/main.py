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

