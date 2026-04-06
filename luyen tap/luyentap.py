#1
a = int(input())
b = int(input())
print(a + b)
print(a - b)
print(a * b)
print(a / b)
#2
def greet(name="Student"):
    print(f"Hello, {name}!")
greet()
greet("Duc")
#3
def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    return n * giai_thua(n - 1)
n = int(input())
print(giai_thua(n))
#4
diem1 = float(input())
diem2 = float(input())
diem3 = float(input())
dtb = (diem1 + diem2 + diem3) / 3
if dtb >= 8:
    print("Gioi")
elif dtb >= 6.5:
    print("Kha")
elif dtb >= 5.0:
    print("Trung binh")
else:
    print("Yeu")
#5
def count_vowels(s):
    vowels = "aeiou"
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count
s = input()
print(count_vowels(s))
#6
colors = ["Red", "Blue", "Green", "Yellow", "Black"]
colors.remove("Red")
print(colors)
#7
def tinh_trung_binh_dict(d):
    if not d:
        return 0
    return sum(d.values()) / len(d)
students = {"An": 8, "Binh": 7, "Chi": 9}
print(tinh_trung_binh_dict(students))
#8
class Product:
    def __init__(self, price=0):
        self._price = price
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            print("Error: Price < 0")
        else:
            self._price = value
p = Product()
p.price = float(input())
print(p.price)
#9
noidung = input()
f = open("data.txt", "w")
f.write(noidung)
f.close()
#10
a = input()
b = input()
s = f"{a}---{b}"
print(s)