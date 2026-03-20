#1
import os
def get_tenfile_with_ex(path):
    return os.path.basename(path)
def get_tenfile_only(path):
    return os.path.splitext(path)[0]
path = "d:\\music\\song gio.mp3"
print(get_tenfile_with_ex(path))
print(get_tenfile_only(path))
#2
a = input("nhap chuoi: " )
b = input("nhap ki tu: ")
print(f"so lan xuat hien: {a.count(b)}")
#3
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
n = int(input("Nhập n: "))
print(f"Giai thừa: {factorial(n)}")
#4
s = input("nhap chuoi: ")
if not s:
    print("loi ko dc de trong")
else:
    print(f"do dai: {len(s)}")
#5
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 100)
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(x, x**2)
ax1.set_title("y = x^2")
ax1.set_xlabel("x")
ax2.plot(x, np.sqrt(x))
ax2.set_title("y = sqrt(x)")
ax2.set_xlabel("x")
plt.tight_layout()
plt.show()
#6
s = input("nhap chuoi: ")
rev = ""
for char in s:
    rev = char + rev
    print(f"chuoi dao nguoc: {rev}")
#7
while True:
    pwd = input("nhap mk: ")
    if pwd == "python123":
        print("dung")
        break
    print("Sai r th ngu")
#8
    arr = []
    for i in range(5):
        s = input(f"Nhập chuỗi thứ {i + 1}: ")
        arr.append(s)
    n = len(arr)
    print("\n--- Quá trình sắp xếp ---")
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if len(arr[j]) < len(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        print(f"Bước {i + 1}: {arr}")
        if not swapped:
            break
    print("\nKết quả cuối cùng:", arr)
#9
class ElectronicDevice:
    def __init__(self, brand):
        self._brand = brand
    @property
    def brand(self): return self._brand
    @brand.setter
    def brand(self, value):
        if not value: raise ValueError("Brand không được rỗng")
        self._brand = value
    @staticmethod
    def info(): return "Thiết bị điện tử"
class Laptop(ElectronicDevice):
    count = 0
    def __init__(self, brand, ram):
        super().__init__(brand)
        self.ram = ram
    @property
    def ram(self): return self._ram
    @ram.setter
    def ram(self, value):
        if value < 0: raise ValueError("RAM không được âm")
        self._ram = value
    def check_valid(self, v):
        if v == 0: raise ValueError("Giá trị không hợp lệ")
    def __str__(self): return f"Laptop {self.brand} - RAM: {self.ram}GB"
    def __eq__(self, other): return self.ram == other.ram
    @classmethod
    def from_string(cls, data_str):
        brand, ram = data_str.split("-")
        return cls(brand, int(ram))
lt1 = Laptop("Dell", 16)
lt2 = Laptop.from_string("Asus-16")
print(lt1)
print(f"Hai máy bằng RAM? {lt1 == lt2}")
print(f"Static: {Laptop.info()}")
#10
def bai_10():
    list_s = [input(f"Nhập chuỗi {i + 1}: ") for i in range(5)]
    size = len(list_s)
    for i in range(size):
        for j in range(size - 1 - i):
            if len(list_s[j]) < len(list_s[j + 1]):
                list_s[j], list_s[j + 1] = list_s[j + 1], list_s[j]
        print(f"Step {i + 1}: {list_s}")
    print("Final List:", list_s)
#11
def menu():
    while True:
        print("\n--- MENU BÀI TẬP ---")
        print("1. Trích xuất tên tệp")
        print("2. Đếm ký tự")
        print("0. Thoát")
        choice = input("Chọn bài (0-11): ")
        if choice == '1':
            p = input("Nhập path: ")
            print(get_tenfile_only(p))
        elif choice == '2':
            # Gọi code bài 2
            pass
        elif choice == '0':
            break
        else:
            print("Lựa chọn không hợp lệ.")
if __name__ == "__main__":
    menu()