class Bomb:
    def __init__(self, bomb_x, bomb_y, radius, time):
        self.bomb_x_y = (bomb_x, bomb_y)
        self.bomb_coord = [(bomb_x, bomb_y)]
        self.bomb_time = time
        self.radius = radius

    def get_bomb_x_y(self):
        return self.bomb_x_y

    def get_bomb(self):
        return self.bomb_coord

    def get_bomb_time(self):
        return self.bomb_time

    def set_bomb_time(self,update_time):
        self.bomb_time = update_time

    def get_bomb_radius(self):
        return self.radius

    def set_bomb_radius(self, cur_radius):
        self.radius = cur_radius

