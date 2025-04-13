import pygame
import random


# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 800

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Snake settings
SNAKE_BLOCK = 20
SNAKE_SPEED = 15

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Man")

# Clock
clock = pygame.time.Clock()

# Fonts
font_style = pygame.font.SysFont("bahnschrift", 30)
score_font = pygame.font.SysFont("comicsansms", 35)


def draw_gradient_background():
    for i in range(0, HEIGHT, 2):
        pygame.draw.line(screen, (0, i % 255, i % 255), (0, i), (WIDTH, i))


def draw_snake(block_size, snake_list):
    for i, block in enumerate(snake_list):
        color_intensity = int(255 * (i / len(snake_list)))
        color = (0, color_intensity, 0)  # Gradient green
        pygame.draw.rect(screen, color, [block[0], block[1], block_size, block_size])


def draw_food(x, y, block_size):
    for offset in range(3):
        pygame.draw.rect(screen, (255, 140, 0), [x + offset, y + offset, block_size - offset * 2, block_size - offset * 2], 2)


def display_score(score):
    value = score_font.render(f"Score: {score}", True, YELLOW)
    screen.blit(value, [10, 10])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [WIDTH / 6, HEIGHT / 3])


def game_over_screen(score):
    screen.fill(BLACK)
    message("Game Over! Press Q to Quit or C to Play Again", RED)
    display_score(score)
    pygame.display.update()


def gameLoop():
    game_over = False
    game_close = False

    x1 = WIDTH // 2
    y1 = HEIGHT // 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = random.randrange(0, WIDTH - SNAKE_BLOCK, SNAKE_BLOCK)
    foody = random.randrange(0, HEIGHT - SNAKE_BLOCK, SNAKE_BLOCK)

    while not game_over:
        while game_close:
            game_over_screen(Length_of_snake - 1)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -SNAKE_BLOCK
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = SNAKE_BLOCK
                    x1_change = 0

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change

        # Set background to plain white
        screen.fill(WHITE)

        # Draw food
        draw_food(foodx, foody, SNAKE_BLOCK)

        snake_Head = [x1, y1]
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for block in snake_List[:-1]:
            if block == snake_Head:
                game_close = True

        draw_snake(SNAKE_BLOCK, snake_List)
        display_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = random.randrange(0, WIDTH - SNAKE_BLOCK, SNAKE_BLOCK)
            foody = random.randrange(0, HEIGHT - SNAKE_BLOCK, SNAKE_BLOCK)
            Length_of_snake += 1

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()



# Start the game
gameLoop()
