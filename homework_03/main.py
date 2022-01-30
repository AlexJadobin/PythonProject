# занятие №3, задание №1, вариант №1
print("-Вариант №1-")

def get_prost(y):
    for i in range(2, y):
        if y % i == 0:
            return False
    return True

prost_str = []
n = 200
for chislo in range(2, n):
    if get_prost(chislo):
        #print(chislo, end=', ')
        prost_str.append(chislo)
print("список простых чисел до n=", n)
print(prost_str)
print("---------")

print("-Вариант №2-")

# занятие №3, задание №1, вариант №2
sps_prost = []
f = 200
def prostye(n):
    for j in range(1, n+1):
        #print('цикл 1 j=', j, ' n=', n)
        for i in range(2, j+1):
            #print('вложенный цикл 2 i=', i, ' j=', j)
            if j % i == 0 and i != j:
                break
            else:
                if i == j:
                    sps_prost.append(j)
                    #print('значение i= ', i, 'значение j= ', j)
    #print(sps_prost)
    return sps_prost

prostye(f)
print("поиск простых чисел до значения =", f)
print(sps_prost)
print('____________')

# задание №2
d = 'пойду строить самый большой дом в городе'
string_d = set(d)
print('разложение строки d в множество с удалением повторяющихся символов set(d)')
print(string_d)
print('--')
result = ''
for y in string_d:
    if d.count(y) == 1:
        result += y
print('result уникальные символы в d.count(y)= ', result)

