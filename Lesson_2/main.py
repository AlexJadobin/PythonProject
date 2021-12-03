# №2
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

