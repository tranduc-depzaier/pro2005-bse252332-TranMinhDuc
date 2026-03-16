#1
weight = float(input("nhap can nang (kg): "))
height = float(input("nhap chieu cao (m): "))
bmi = weight / (height * height)
print(f"bmi : {round(bmi, 2)}")
#2
n = input("nhap so:")
tong = sum (int(chu_so) for chu_so in n if chu_so.isdigit())
print(f"tong cac  chu so la: {tong}")
#3
name = " phunG tHanh dO"
name_standardized = " ".join(name.split()).title()
print(f"ket qua: '{name_standardized}'")
#4
s = input("nhap chuoi: ")
res = {
    "in hoa": 0, "in thuong": 0, "so": 0, "khoang trang": 0, "dac biet": 0, "nguyen am": 0, "phu am": 0}
vowels = "chathieuCHI"
for char in s:
    if char.isupper(): res[vowels] +=1
    if char.islower(): res[vowels] +=1
    if char.isdigit(): res[vowels] +=1
    if char.isspace(): res[vowels] +=1
    if not char.isalnum() and not char.isspace(): res["dac biet"] +=1
    if char.isalpha(): res["nguyen am"] +=1
    else: res["phu am"] +=1
    for k, v in res.items():
        print(f"{k}: {v}")
#5
class User:
    def __init__(self, id):
        self._id = id
    @property
    def id(self):
        return self._id
user = User(101)
print(user.id)
#6
class Product:
    def __init__(self, price):
        self.price = price
    @property
    def price(self):
        return self._price
    @price.better
    def price(self, value):
        if value > 0:
            self._price = value
        else:
            print("gia lon hon 0")
            self._price = 0
    def __str__(self):
         return f"Product Price: {self._price}"
p = Product(500)
print(p)
#7
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def form_string(cls, data_str):
        name, age = data_str.split("-")
        return cls(name, int(age))
p = Person.from_string("nam_36")
print(f"ten: {p.name}, tuoi: {p.age}")
#8
class vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return vector(self.x + other.x, self.y + other.y)
    def __str__(self):
        return f"vector({self.x}, {self.y}"
v1 = vector(1, 2)
v2 = vector(3, 4)
print(v1 + v2)
#9
class animal:
    def __init__(self, name):
        self.name = name
    def sound(self):
        pass
class dog(animal):
    def __init__(self, name):
        super().__init__(name)
    def sound(self):
        print(f"{self.name} keu: meow moew")
my_dog = dog("tiendat")
my_dog.sound()
#10
class SinhVien:
    def __init__(self, diem):
        self.diem = diem
    def __eq__(self, other):
        if isinstance(other, SinhVien):
            return self.diem == other.diem
        return False
sv1 = SinhVien(8.5)
sv2 = SinhVien(8.5)
sv3 = SinhVien(7.0)
print(f"sv1 == sv2: {sv1 == sv2}")
print(f"sv1 == sv3: {sv1 == sv3}")
#11
class SinhVien:
    dem = 0
    def __init__(self, diem):
        self.diem = diem
        SinhVien.dem += 1
    @classmethod
    def so_luong_sv(cls):
        return f"Số sinh viên đã tạo: {cls.dem}"
sv1 = SinhVien(9)
sv2 = SinhVien(8)
sv3 = SinhVien(10)
print(SinhVien.so_luong_sv())











