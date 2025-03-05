# スネークゲームを作ってみる
# とりあえずりんごなしのスネークゲームを作ってみる

# pygameの設定
import pygame
import sys

pygame.init()
pygame.display.set_caption("スネークゲーム")
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# ゲームの設定
snake = [(200, 200), (215, 200), (230, 200), (245, 200), (260, 200)]  # スネークの初期位置
snake_length = 5
snake_speed = 18
snake_direction = (15, 0)
snake_alive = True


def draw_snake():
    for segment in snake:
        pygame.draw.rect(screen, (255, 255, 255), (*segment, 15, 15))


def move_snake():
    global snake
    head = snake[-1]
    new_head = (head[0] + snake_direction[0], head[1] + snake_direction[1])
    snake = snake[1:] + [new_head]


def check_collision():
    head = snake[-1]
    if head[0] < 0 or head[0] >= 800 or head[1] < 0 or head[1] >= 600:
        return True
    return False


while snake_alive:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != (0, 15):
                snake_direction = (0, -15)
            if event.key == pygame.K_DOWN and snake_direction != (0, -15):
                snake_direction = (0, 15)
            if event.key == pygame.K_LEFT and snake_direction != (15, 0):
                snake_direction = (-15, 0)
            if event.key == pygame.K_RIGHT and snake_direction != (-15, 0):
                snake_direction = (15, 0)

    move_snake()
    draw_snake()

    if check_collision():
        snake_alive = False

    pygame.display.update()
    clock.tick(snake_speed)

while True:
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 74)
    text = font.render("Game Over", True, (255, 255, 255))
    text_rect = text.get_rect(center=(400, 300))
    screen.blit(text, text_rect)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()