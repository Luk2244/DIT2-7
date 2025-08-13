from datetime import datetime

# รับข้อมูลจากผู้ใช้
full_name = input("กรุณาใส่ชื่อ-นามสกุล: ")
birth_date_str = input("กรุณาใส่วันเดือนปีเกิด (ตัวอย่าง: วัน/เดือน/ปี เช่น 13/08/2000): ")

# แปลงจาก string เป็น datetime
birth_date = datetime.strptime(birth_date_str, "%d/%m/%Y")

# วันที่ปัจจุบัน
today = datetime.today()

# คำนวณอายุ
age = today.year - birth_date.year
# ตรวจสอบว่าวันเกิดของปีนี้ยังมาไม่ถึงหรือไม่
if (today.month, today.day) < (birth_date.month, birth_date.day):
    age -= 1

# แสดงผล
print(f"\nข้อมูลส่วนตัว:")
print(f"ชื่อ-นามสกุล: {full_name}")
print(f"วันเกิด: {birth_date.strftime('%d/%m/%Y')}")
print(f"อายุ: {age} ปี")