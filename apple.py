class Apple:

    def __init__(self, apple_x, apple_y, score):
        self.apple_x = apple_x
        self.apple_y = apple_y
        self.score = score

    def get_coord(self):
        return self.apple_x, self.apple_y

    def set_coord(self, other_x, other_y):
        self.apple_x = other_x
        self.apple_y = other_y

    def get_score(self):
        return self.score


