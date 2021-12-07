# 1
def get_prost(y):
    for i in range(2, y):
        if y % i == 0:
            return False
    return True

for chislo in range(1, 200):
    if get_prost(chislo):
        print(chislo, end=', ')
print("--")

# №2

d = 'пойду строить самый большой дом в городе'
string_d = set(d)
result = ''
for y in string_d:
    if d.count(y) == 1:
        result += y
print(result)

