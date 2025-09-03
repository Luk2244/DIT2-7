import time, random

def show_numbers(numbers):
    print("\nNumbers are running: ")
    for _ in range(10):  # จำลองเลขวิ่ง
        show = random.sample(numbers, len(numbers))
        print(" ".join(str(x) for x in show), end="\r")
        time.sleep(0.3)
    print("\nYour numbers:", numbers)