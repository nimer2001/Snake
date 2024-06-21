from game_parameters import *
from game_display import GameDisplay
from snake import *
from apple import *
from bomb import *
from copy import deepcopy
from typing import *


def main_loop(gd: GameDisplay) -> None:
    snake = Snake(WIDTH//2, HEIGHT//2, 3)
    bomb = [init_bomb(snake)]
    apple_list = []
    init_apple(apple_list, snake, bomb[0], 3)
    score = 0
    gd.show_score(score)
    old_key = "Up"
    snake_move = "Up"
    pls_len = 0
    flag = False
    new_apple = [False]
    radius = [0]
    draw_snake(gd, snake, bomb[0])
    gd.draw_cell(bomb[0].get_bomb()[0][0], bomb[0].get_bomb()[0][1], "red")
    for i in range(3):
        gd.draw_cell(apple_list[i].get_coord()[0], apple_list[i].get_coord()[1], "green")
    gd.end_round()
    while True:
        key_clicked = gd.get_key_clicked()
        if flag is True:
            pls_len += 3
        if key_clicked:
            if key_clicked == "Up" and old_key != "Down":
                snake_move = "Up"
                old_key = "Up"
                if pls_len > 0:
                    snake.move(snake_move, True)
                    if hit_edges(snake):
                        snake.my_list.pop(-1)
                        draw(gd, snake, bomb, apple_list, new_apple, radius)
                        gd.end_round()
                        break
                    pls_len -= 1
                else:
                    snake.move(snake_move, False)
                    if hit_edges(snake):
                        snake.my_list.pop(-1)
                        draw(gd, snake, bomb, apple_list, new_apple, radius)
                        gd.end_round()
                        break
            elif key_clicked == "Down" and old_key != "Up":
                snake_move = "Down"
                old_key = "Down"
                if pls_len > 0:
                    snake.move(snake_move, True)
                    if hit_edges(snake):
                        snake.my_list.pop(-1)
                        draw(gd, snake, bomb, apple_list, new_apple, radius)
                        gd.end_round()
                        break
                    pls_len -= 1
                else:
                    snake.move(snake_move, False)
                    if hit_edges(snake):
                        snake.my_list.pop(-1)
                        draw(gd, snake, bomb, apple_list, new_apple, radius)
                        gd.end_round()
                        break
            elif key_clicked == "Right" and old_key != "Left":
                snake_move = "Right"
                old_key = "Right"
                if pls_len > 0:
                    snake.move(snake_move, True)
                    if hit_edges(snake):
                        snake.my_list.pop(-1)
                        draw(gd, snake, bomb, apple_list, new_apple, radius)
                        gd.end_round()
                        break
                    pls_len -= 1
                else:
                    snake.move(snake_move, False)
                    if hit_edges(snake):
                        snake.my_list.pop(-1)
                        draw(gd, snake, bomb, apple_list, new_apple, radius)
                        gd.end_round()
                        break
            elif key_clicked == "Left" and old_key != "Right":
                snake_move = "Left"
                old_key = "Left"
                if pls_len > 0:
                    snake.move(snake_move, True)
                    if hit_edges(snake):
                        snake.my_list.pop(-1)
                        draw(gd, snake, bomb, apple_list, new_apple, radius)
                        gd.end_round()
                        break
                    pls_len -= 1
                else:
                    snake.move(snake_move, False)
                    if hit_edges(snake):
                        snake.my_list.pop(-1)
                        draw(gd, snake, bomb, apple_list, new_apple, radius)
                        gd.end_round()
                        break
            else:
                if pls_len > 0:
                    snake.move(snake_move, True)
                    if hit_edges(snake):
                        snake.my_list.pop(-1)
                        draw(gd, snake, bomb, apple_list, new_apple, radius)
                        gd.end_round()
                        break
                    pls_len -= 1
                else:
                    snake.move(snake_move, False)
                    if hit_edges(snake):
                        snake.my_list.pop(-1)
                        draw(gd, snake, bomb, apple_list, new_apple, radius)
                        gd.end_round()
                        break
        else:
            if pls_len > 0:
                snake.move(snake_move, True)
                if hit_edges(snake):
                    snake.my_list.pop(-1)
                    draw(gd, snake, bomb, apple_list, new_apple, radius)
                    gd.end_round()
                    break
                pls_len -= 1
            else:
                snake.move(snake_move, False)
                if hit_edges(snake):
                    snake.my_list.pop(-1)
                    draw(gd, snake, bomb, apple_list, new_apple, radius)
                    gd.end_round()
                    break
        if did_hit(snake) or collision_bomb_with_snake(bomb[0], snake):
            draw(gd, snake, bomb, apple_list, new_apple, radius)
            gd.end_round()
            break
        update_bomb(bomb, radius, gd, apple_list, snake, new_apple)
        if did_hit(snake) or collision_bomb_with_snake(bomb[0], snake):
            draw(gd, snake, bomb, apple_list, new_apple, radius)
            gd.end_round()
            break
        score, flag = eat_apple(snake, apple_list, gd, score)
        update_apples(apple_list, snake, bomb[0])
        draw(gd, snake, bomb, apple_list, new_apple, radius)
        gd.end_round()


def draw(gd, snake, bomb, apple_list, new_apple, radius):
    draw_snake(gd, snake, bomb[0])
    draw_bomb(bomb, radius, gd)
    draw_apple(apple_list, gd)


def draw_bomb(bomb, radius, gd):
    if bomb[0].get_bomb_time() > 0:
        gd.draw_cell(bomb[0].get_bomb()[0][0], bomb[0].get_bomb()[0][1], "red")
    elif bomb[0].get_bomb_time() == 0 and radius == 0:
        gd.draw_cell(bomb.get_bomb()[0][0], bomb.get_bomb()[0][1], "orange")
    else:
        for row, col in bomb[0].get_bomb():
            gd.draw_cell(row, col, "orange")


def update_bomb(bomb, radius, gd, apple_list, snake, new_apple):
    if bomb[0].get_bomb_time() > 0:
        new_apple[0] = True
    bomb_explosion(bomb[0], gd, radius[0])

    if bomb[0].get_bomb_time() == 0:
        radius[0], bomb[0] = hit_bomb(bomb[0], gd, radius[0], snake)
        if bomb_hit_apple(bomb[0], apple_list):
            if new_apple[0] is True or len(apple_list) < 3:
                init_apple(apple_list, snake, bomb[0], 1)
                new_apple[0] = False


def draw_snake(gd:GameDisplay, snake, bomb):
    for cell in snake.my_list:
        if cell not in bomb.get_bomb():
            gd.draw_cell(cell[0],  cell[1], "black")


def draw_apple(apple_list, gd: GameDisplay):
    for i in range(len(apple_list)):
        gd.draw_cell(apple_list[i].get_coord()[0], apple_list[i].get_coord()[1], "green")


def eat_apple(snake, apple_list: List[Apple], gd: GameDisplay,  score):
    flag = False
    for i in range(len(apple_list)):
        if snake.my_list[-1][0] == apple_list[i].get_coord()[0] and snake.my_list[-1][1] == apple_list[i].get_coord()[1]:
            flag = True
            score += apple_list[i].get_score()
            gd.show_score(score)
    return score, flag


def init_bomb(snake):
    x, y, radius, time = get_random_bomb_data()
    while (x, y) in snake.get_coord():
        x, y, radius, time = get_random_bomb_data()
    return Bomb(x, y, radius, time)


def init_apple(apple_list, snake, bomb, number_apples):
    for i in range(number_apples):
        x, y, score = get_random_apple_data()
        my_apple = Apple(x, y, score)
        while collision_apples(apple_list, snake, bomb, my_apple) is True:
            x, y, score = get_random_apple_data()
            my_apple = Apple(x, y, score)
        apple_list.append(my_apple)


def collision_apples(apple_list, snake, bomb, my_apple):
    if collision_with_snake(my_apple, snake) or collision_with_apples(my_apple, apple_list) or \
            collision_with_bomb(my_apple, bomb):
        return True
    return False


def collision_with_snake(my_apple, snake):
    if my_apple.get_coord() in snake.my_list:
        return True
    return False


def collision_with_apples(my_apple, apple_list):
    for i in range(len(apple_list)):
        if apple_list[i].get_coord() == my_apple.get_coord():
            for j in range(i+1, len(apple_list)):
                if apple_list[j].get_coord() == my_apple.get_coord():
                    return True
    return False


def collision_with_bomb(my_apple, bomb):
    if my_apple.get_coord() in bomb.get_bomb():
        return True
    return False


def did_hit(snake):
    my_new_list = deepcopy(snake.my_list)
    head = my_new_list[-1]
    my_new_list.pop(-1)
    if head in my_new_list:
        return True
    return False


def hit_edges(snake):
    if snake.my_list[-1][0] >= WIDTH or snake.my_list[-1][0] <= -1 or snake.my_list[-1][1] >= HEIGHT or \
            snake.my_list[-1][1] <= -1:
        return True
    return False


def collision_bomb_with_snake(bomb, snake):
    for i in range(len(snake.my_list)):
        if snake.my_list[i] in bomb.get_bomb():
            return True
    return False


def bomb_explosion(bomb, gd: GameDisplay, radius):
    if bomb.get_bomb_time() > 0:
        bomb.set_bomb_time(bomb.get_bomb_time() - 1)


def hit_bomb(bomb, gd: GameDisplay, radius, snake):
    if radius <= bomb.get_bomb_radius():
        lst = []
        for row in range(WIDTH):
            for col in range(HEIGHT):
                if abs(bomb.get_bomb_x_y()[0] - row) + abs(bomb.get_bomb_x_y()[1] - col) == radius:
                    lst.append((row,col))
        bomb.bomb_coord = lst
        return radius + 1, bomb
    bomb = init_bomb(snake)
    return 0, bomb


def update_apples(apple_list, snake, bomb):
    flag = False
    for i in range(len(apple_list)):
        if snake.my_list[-1][0] == apple_list[i].get_coord()[0] and snake.my_list[-1][1] == apple_list[i].get_coord()[1]:
            flag = True
        if flag:
            while True:
                if collision_apples(apple_list, snake, bomb, apple_list[i]):
                    new_apple_coord = get_random_apple_data()
                    apple_list[i].set_coord(new_apple_coord[0], new_apple_coord[1])
                else:
                    break


def bomb_hit_apple(bomb, apple_list):
    for apple in range(len(apple_list)):
        if apple_list[apple].get_coord() in bomb.get_bomb():
            apple_list.pop(apple)
            return True
    return False
