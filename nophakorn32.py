from datetime import datetime
current_year = datetime.now().year
name = input("Input your name: ")
bc_birth_year = int(input("Input BC born (B.E.): "))
ad_birth_year = bc_birth_year - 543
age = current_year - ad_birth_year
print(f"{name}, your age is {age}")
if age >= 19:
    print("You are 19 or older.")
else:
    print("You are younger than 19.")
    