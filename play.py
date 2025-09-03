from generator import generate_numbers, generate_target
from display import show_numbers
from player import get_expression
from checker import check_answer
from score import ScoreBoard

def play():
    numbers = generate_numbers()
    target = generate_target()
    scoreboard = ScoreBoard()

    print("🎮 Welcome to Math Catch Game!")
    print(f"Target number: {target}")

    show_numbers(numbers)

    expr = get_expression(numbers)
    result, valid = check_answer(expr, numbers, target)

    if valid:
        print(f"✅ Good job! Your result = {result}")
        scoreboard.add_score("Player1", result, target)
    else:
        print("❌ Invalid or incorrect expression.")

    scoreboard.show()

if name == "main":
    play()