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



