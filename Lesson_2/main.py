# №2
print("задание №2 и №3: печать строки в различных форматах")
print("--")
string = "Быстрый коричнивый лис прыгает над ленивой собакой"
print(string)
print("--")

# №3
newstring = ["Быстрый", "коричневый", "лис", "прыгает", "над", "ленивой", "собакой"]
for elem in newstring:
    print(elem)
print("--")

print(string.split())
print("--")
for elem in string.split():
    print(elem)
print("--")

new1string = (string.split())
for elem in newstring:
    print(elem)
print("--")

for s in string:
    print(s)
print("--")

print(list(string))
print("--")

# №4
print("задание №4, №5, №6: создание строки из 100 значений от 0 до 99 и печать квадратов этих значений")
str1 = []
str1 = list(range(0, 100))
print("--")

# №5
def kvadrat(list):
    kvadrat_str1 = []
    for i in  list:
        kvadrat_str1.append(i**2)
        if i == 99:
            print(kvadrat_str1)
    return kvadrat_str1

# №6
kvadrat(str1)
print("--")

#7  работа со словарями
moy_dict = {
    1: "один",
    2: "два",
    3: "три"
    }
print("moy_dict ", moy_dict)
print("--")


print("мой m_dict ", moy_dict)
moy_dict["numbers"] = list(range(0, 100))
print(moy_dict)
print ("--")

def kvadrat():
    for i in range(0, 100):
        if i % 10 != 0:
            print(i * i, end="\t")
kvadrat()
print (" ")
print ("---")







