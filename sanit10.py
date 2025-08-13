from datetime import datetime

current year = datetime,now(),year

name = input ("yourname")

birth year = int(input ("Enter your birth year (e.g., 1990):

age current year birth year

6 print (name, "your age is ",age)
Sanit
from datetime import date

birth = input("กรอกวันเกิด (yyyy-mm-dd): ")
birth_date = date.fromisoformat(birth)
today = date.today()

age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
print(f"คุณอายุ {age} ปี")