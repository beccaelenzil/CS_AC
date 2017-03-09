class ScoreKeeper():
    def __init__(self):
        self.score = 0
        self.remaining_lives = 3
        self.remaining_trips = 3

    def get_remaining_lives(self):
        return self.remaining_lives

    def get_score(self):
        return self.score

    def increment_score(self):
        self.score += 1

    def die(self):
        self.remaining_lives -= 1

    def reduce_trips(self):
        self.remaining_trips -= 1

    def out_of_trips(self):
        return self.remaining_trips == 0

    def loss(self):
        return self.remaining_lives == 0
