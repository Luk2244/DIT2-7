# รับชื่อจากผู้ใช้
name = input("Input your name: ")

# รับปี พ.ศ. จากผู้ใช้
year_buddhist = int(input("Input BC Bom (ปี พ.ศ.): "))

# คำนวณอายุจากปี พ.ศ. และปีปัจจุบัน
current_year = 2568  # ปี พ.ศ. ปัจจุบัน
age = current_year - year_buddhist

# แสดงผลลัพธ์ที่ต้องการ
print(f"Input you name {name} ")
print(f"Input BC Bom .ศ. {year_buddhist} ")
print(f"Thenge {age} age")