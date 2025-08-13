from datetime import datetime
current_year = datetime.now().year
name = input(("Your Firstname : "))
last = input(("Your Lastname : "))
birth_year = int(input("Enter your birth year (e.g., 1990): "))
age = current_year - birth_year
print(name ,last , "your age is ",age)