#1
n = int(input("Nhập một số nguyên: "))
if n < 0:
    print("Lỗi: Vui lòng nhập một số không âm!")
else:
    remainder = n % 2
    print(f"Phần dư của {n} khi chia cho 2 là: {remainder}")
#2
s = input("Nhập một chuỗi: ")
print(f"Chiều dài của chuỗi là: {len(s)}")
print(f"Chuỗi sau khi chuyển thành chữ hoa: {s.upper()}")
#3
i = 1
tong = 0
print("Các số lẻ từ 1 đến 30 là:")
while i <= 30:
    if i % 2 != 0:
        print(i, end=" ")
        tong += i
    i += 1
print(f"\nTổng của các số lẻ trên là: {tong}")
#4
def tinh_tong_de_quy(n):
    if n == 1:
        return 1
    return n + tinh_tong_de_quy(n - 1)
n = int(input("Nhập n: "))
if n > 0:
    print(f"Tổng từ 1 đến {n} là: {tinh_tong_de_quy(n)}")
else:
    print("Vui lòng nhập số nguyên dương.")
#5
class Flower:
    def __init__(self, color):
        self._color = color  # Thuộc tính ẩn danh (protected)
    def get_color(self):
        return self._color
    def set_color(self, new_color):
        self._color = new_color
my_flower = Flower("Red")
print(f"Màu sắc ban đầu: {my_flower.get_color()}")
my_flower.set_color("Yellow")
print(f"Màu sắc sau khi thay đổi: {my_flower.get_color()}")
#6
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
numbers = [64, 25, 12, 22, 11]
sorted_numbers = selection_sort(numbers)
print(f"Dãy sau khi sắp xếp: {sorted_numbers}")
