#1
a = 10
b = 4
result = (a**2 + b**2)/(a - b)
print(result)
#2
import math
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
print(f"Lũy thừa a^b: {a**b}")
print(f"Căn bậc 2 a: {math.sqrt(a)}")
print(f"Chia lấy nguyên: {a // b}")
print(f"Chia lấy dư: {a % b}")
print(f"Làm tròn a: {round(a)}")
#3
n = int(input("nhap so(1-9: "))
for i in range(1, 10):
    print(f"{n}: x {i} = {n * i}")
#4
for i in range(1, 100):
    if i % 3 != 0:
        print(i, end=" ")
#5
import random
m, n = 3, 4
matrix = [[random.randint(1, 100) for _ in range(n)] for _ in range(m)]
print("Ma trận:", matrix)
r = int(input("Hiện hàng: "))
print(matrix[r])
c = int(input("Hiện cột: "))
print([row[c] for row in matrix])
print("Max:", max(max(row) for row in matrix))
#6
s = "5; 7; 8; -2; 8; 11; 13; 9; 10"
nums = [int(x) for x in s.split("; ")]
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True
for n in nums: print(n)
print("Số chẵn:", len([x for x in nums if x % 2 == 0]))
print("Số âm:", len([x for x in nums if x < 0]))
print("Số nguyên tố:", len([x for x in nums if is_prime(x)]))
print("Trung bình:", sum(nums) / len(nums))
#7
class student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
sv1 = student("tran minh duc", 10)
sv2 = student("do mixi", 1.5)
print(f"tao sinh vien: {sv1.name} and {sv2.name}")
#8
class Student:
    def __init__(self, name, score):
        self.name = name
        if 0 <= score <= 10:
            self.score = score
        else:
            self.score = 0
            print(f"Lỗi: Điểm của {name} không hợp lệ (phải từ 0-10). Đã đặt về 0.")
sv_tot = Student("duc", 15)
sv_loi = Student("streamer ng tay", 5)
#9
class student:
    def __init__(self, name, score):
        self.name = name
        self.score = score if 0<= score <= 10 else 0
    def display(self):
        print(f"sinh vien{self.name} co diem la{self.score}")
sv1 = student("minh duc", 10)
sv2 = student("do mixue", 1.5)
sv1.display()
sv2.display()
#10
code = input("ma sp: ")
name = input("ten sp: ")
price = input("gia: ")
with open("products.txt", "a", encoding="utf-8") as f:
    f.write(f"{code};{name};{price}\n")
print("da luu sp")





