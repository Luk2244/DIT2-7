from datetime import datetime, date
birth_input = input("ป้อนวันเดือนปีเกิด (รูปแบบ: DD/MM/YYYY): ")

birth_date = datetime.strptime(birth_input, "%d/%m/%Y").date()

today = date.today()

age = today.year - birth_date.year

if (today.month, today.day) < (birth_date.month, birth_date.day):
    age -= 1
print(f"คุณเกิดวันที่: {birth_date.strftime('%d %B %Y')}
print(f"อายุของคุณคือ: {age} ปี")