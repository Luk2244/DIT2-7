from datetime import datetime
name =input("ชื่อ:")
birthday = int(input("ปีเกิด"))
today = datetime.now().year
age = today - birthday
print("สวัสดี",name)
print("คุณมีอายุ",age,"ปี")