numbers = []

print("ใส่ตัวเลข 5 ตัวเลข:")
for i in range(5):
    num = int(input(f"เลขที่ {i + 1}: "))
    numbers.append(num)

numbers.sort()

print("ลำดับจากน้อยไปมาก:")
print(numbers)