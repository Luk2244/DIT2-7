def check_answer(expr, numbers, target):
    try:
        result = eval(expr)
    except Exception:
        return None, False

    # เช็คว่าใช้เลขที่มีให้จริง ๆ
    used_digits = [int(x) for x in expr if x.isdigit()]
    nums_copy = numbers[:]
    for d in used_digits:
        if d in nums_copy:
            nums_copy.remove(d)
        else:
            return None, False  # ใช้เลขที่ไม่มี

    # ตรวจว่าเข้าเป้า (หรือใกล้เคียง ±2)
    if result == target or abs(result - target) <= 2:
        return result, True
    return result, False