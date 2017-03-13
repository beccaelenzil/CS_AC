class ScoreKeeper():
    def __init__(self):
        self.score = 0
        self.remaining_lives = 3
        self.level = 1
        self.person_is_dead = 0
        self.delta = 1.5
        self.acceleration = 0.2
        self.velocity = -6
        self.lower_limit = 50
        self.upper_limit = 100
        self.level_up = False

    def get_remaining_lives(self):
        return self.remaining_lives

    def get_score(self):
        return self.score

    def get_level(self):
        return self.level

    def increment_level(self):
        self.level += 1
        self.delta +=0.5
        self.acceleration += 0.02
        self.velocity -= 0.2
        self.lower_limit += 5
        self.upper_limit += 5


    def increment_score(self):
        self.score += 1
        if self.score % 5 == 0:
            self.increment_level()
            self.level_up = True
        elif (self.score - 1) % 5 == 0:
            self.level_up = True
        else:
            self.level_up = False

    def die(self):
        if self.person_is_dead == 0:
            self.remaining_lives -= 1
            self.person_is_dead = 1
        else:
            self.person_is_dead +=1

    def is_person_alive(self):
        return self.person_is_dead == 0

    #def is_person_alive(self):
        #return self.person_is_dead == 0

    def should_person_be_regenerated(self):
        return self.person_is_dead > 60*5

    def should_buildings_move(self):
        return self.person_is_dead > 60*4

    #def person_is_dead(self):
        #self.person_is_dead += 1

    def regenerate_person(self):
        self.person_is_dead = 0

    def game_over(self):
        return self.remaining_lives == 0



