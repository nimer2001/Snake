class Snake:
    def __init__(self, snake_x, snake_y, length):
        self.snake_x = snake_x
        self.snake_y = snake_y
        self.length = length
        self.my_list = []
        for i in range(self.length-1, -1, -1):
            self.my_list.append((self.snake_x, self.snake_y-i))

    def move(self, snake_move, flag):
        if snake_move == "Right":
            self.my_list.append((self.my_list[-1][0]+1, self.my_list[-1][1]))
            if flag is False:
                self.my_list.pop(0)
            self.length += 1
        if snake_move == "Left":
            self.my_list.append((self.my_list[-1][0]-1, self.my_list[-1][1]))
            if flag is False:
                self.my_list.pop(0)
            self.length += 1
        if snake_move == "Up":
            self.my_list.append((self.my_list[-1][0], self.my_list[-1][1] + 1))
            if flag is False:
                self.my_list.pop(0)
            self.length += 1
        if snake_move == "Down":
            self.my_list.append((self.my_list[-1][0], self.my_list[-1][1]-1))
            if flag is False:
                self.my_list.pop(0)
            self.length += 1

    def get_snake_length(self):
        return self.length

    def get_coord(self):
        return self.my_list
