class ScoreBoard:
    def __init__(self):
        self.scores = []

    def add_score(self, name, result, target):
        diff = abs(result - target)
        points = max(0, 10 - diff)
        self.scores.append((name, points))

    def show(self):
        print("\n๐ Scoreboard:")
        for name, points in self.scores:
            print(f"{name}: {points} points")