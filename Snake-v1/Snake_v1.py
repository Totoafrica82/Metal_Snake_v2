import pygame
import random

pygame.init()

# Colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Screen dimensions
dis_width = 800
dis_height = 600

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Metal Snake Game by Tomasz Syrylo')

clock = pygame.time.Clock()

# Game settings
snake_block = 10
snake_speed = 20

font_style = pygame.font.SysFont(None, 35)

def draw_text(text, color, x, y):
    text_surface = font_style.render(text, True, color)
    dis.blit(text_surface, (x, y))

def game_loop():
    global snake_speed  # Declare snake_speed as global

    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    level = 1
    level_change_threshold = 10

    while not game_over:
        while game_close:
            dis.fill(black)
            draw_text("You Lost! Press C to Play Again or Q to Quit", red, dis_width / 6, dis_height / 4)
            draw_text("Your Score: " + str(length_of_snake - 1), white, dis_width / 3, dis_height / 3)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                key_actions = {
                    pygame.K_LEFT: (-snake_block, 0),
                    pygame.K_RIGHT: (snake_block, 0),
                    pygame.K_UP: (0, -snake_block),
                    pygame.K_DOWN: (0, snake_block)
                }
                if event.key in key_actions:
                    x1_change, y1_change = key_actions[event.key]

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        for x in snake_list:
            pygame.draw.rect(dis, white, [x[0], x[1], snake_block, snake_block])

        draw_text("Your Score: " + str(length_of_snake - 1), red, 10, 10)
        draw_text("Level: " + str(level), red, dis_width - 100, 10)

        pygame.display.update()

        if length_of_snake - 1 >= level * level_change_threshold:
            level += 1
            snake_speed += 5  # Increase snake speed for each level

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1
            min_distance = 10
            foodx = round(random.randrange(min_distance, dis_width - min_distance - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(min_distance, dis_height - min_distance - snake_block) / 10.0) * 10.0


        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
