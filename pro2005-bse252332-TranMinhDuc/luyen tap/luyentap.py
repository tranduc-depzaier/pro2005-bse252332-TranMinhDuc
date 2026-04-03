#1
PI = 3.14
r = float(input("Nhập bán kính hình tròn: "))
chu_vi = 2 * PI * r
print(f"Chu vi hình tròn là: {chu_vi}")
#2
names = []
for i in range(5):
    name = input(f"Nhập tên người thứ {i+1}: ")
    names.append(name)
print("Danh sách ban đầu:", names)
if len(names) >= 2:
    del names[1]
    print("Danh sách sau khi xóa người thứ hai:", names)
#3
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

arr = list(map(int, input("Nhập các số tự nhiên (cách nhau bởi dấu cách): ").split()))

odd_numbers = [x for x in arr if x % 2 != 0]
print(f"Các số lẻ: {odd_numbers} - Tổng số lượng: {len(odd_numbers)}")

prime_numbers = [x for x in arr if is_prime(x)]
print(f"Các số nguyên tố: {prime_numbers}")
#4
class Book:
    def __init__(self, name, price):
        self._name = name
        self._price = price
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        self._price = value
my_book = Book("Lập trình Python", 50000)
print(f"Giá của sách: {my_book.price}")
#5
data = [
    ("Book 1", 30000),
    ("Book 2", 50000),
    ("Book 3", 100000)
]
tong = 900000
with open("books.txt", "w", encoding="utf-8") as f:
    for name, price in data:
        f.write(f"{name};{price}\n")
    f.write(f"Tong;{tong}")
print("Đã tạo file books.txt thành công.")
#6
layers = {
    "layer-11": {
        "layer-21": 90,
        "layer-22": {
            "layer 31": 43
        }
    },
    "layer-12": 35
}
print("Giá trị layer-12:", layers["layer-12"])
val_31 = layers["layer-11"]["layer-22"]["layer 31"]
print("Giá trị layer-31:", val_31)
