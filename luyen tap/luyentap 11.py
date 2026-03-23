#1
strings = [input(f"nhap chuoi {i+1}: ") for i in range(5)]
for i in range (1, len(strings)):
    key = strings[i]
    j = i - 1
    while j >= 0 and len(strings[j]) < len(key):
        strings[j + 1] = strings[j]
        j -= 1
    strings[j + 1] = key
    print(f"buoc {i}: {strings}")
#2
target = input("nhap chuoi can tim:")
low = 0
high = len(strings) - 1
index = -1
while low <= high:
    mid = (low + high) //2
    if strings[mid] == target:
        index = mid
        break
    elif strings[mid] > target:
        low = mid + 1
    else:
        high = mid - 1
print(f"vi tri {index}" if index != -1 else "ko tim thay")
#3
nums = list(map(int, input("nhap danh sach so"). split()))
evens = [x for x in nums if x % 2 == 0]
print(f"cac so chan: {evens}")
print(f"tong: {len(evens)}")
#4
import math
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True
lst = [6, 9, 3, 3, 2, 5]
lst.append(int(input("them phan tu: ")))
k = int(input("nhap k: "))
print(f"so lan xuat hien cua {k}: {lst.count(k)}")
print(f"tong so nguyen to: {sum(x for x in lst if is_prime(x))}")
lst.sort()
print(f"danh sach sau sap xep: {lst}")
lst.clear()
#5
d = {"name":"python", "year":"2026"}
key = input("nhap key can kiem tra")
print("ton tai" if key in d else "ko tim thay")
#6
data = {}
n = int(input("so luong ng:"))
for _ in range(n):
    name = input("ten:")
    age = int(input("tuoi:"))
    data[name] = age
avg_age =sum(data.values()) / len(data)
print(f"tuoi trung binh: {avg_age}")
#7
import csv
name = input("Nhân viên: ")
age = input("Tuổi: ")
id_nv = input("ID: ")
with open("info.txt", "w", encoding="utf-8") as f:
    f.write(f"{name}, {age}, {id_nv}")
with open("info.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age", "ID"])
    writer.writerow([name, age, id_nv])
print("Đã lưu file. (Lưu ý: Việc chụp ảnh màn hình cần thư viện ngoài như Pillow hoặc thao tác thủ công)")
#8
student = ("domixi", "36", "18")
name, age, gpa = student
print(f"ten: {name}\ntuoi: {age}\ngpa: {gpa}")
#9
def input_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row_input = input(f"Nhập hàng {i+1} (cách nhau bởi khoảng trắng): ").split()
        if not row_input or any(x == "" for x in row_input):
            raise ValueError("Lỗi: Giá trị nhập vào không được để trống!")
        matrix.append([int(x) for x in row_input])
    return matrix
try:
    r, c = map(int, input("Nhập số hàng và cột: ").split())
    print("Ma trận A:")
    A = input_matrix(r, c)
    print("Ma trận B:")
    B = input_matrix(r, c)
    res = [[A[i][j] + B[i][j] for j in range(c)] for i in range(r)]
    print("Kết quả cộng ma trận:")
    for row in res: print(row)
except ValueError as e:
    print(e)






