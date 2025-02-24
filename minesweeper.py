import pygame
import random

# 初期化
pygame.init()

# 画面設定
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("マインスイーパー")

# 色
GREEN_YELLOW = (173, 255, 47)
LIGHT_GREEN = (208, 255, 136)
GREEN_SET = [GREEN_YELLOW, LIGHT_GREEN]
GREEN_YELLOW_WHITE = (201, 255, 100)
LIGHT_GREEN_WHITE = (229, 255, 158)
GREEN_SET_WHITE = [GREEN_YELLOW_WHITE, LIGHT_GREEN_WHITE]
BEIGE = (231, 208, 169)
EKURU_BEIGE = (244, 224, 196)
BEIGE_WHITE = (251, 228, 189)
EKURU_BEIGE_WHITE = (255, 244, 216)
BEIGE_SET = [BEIGE, EKURU_BEIGE]
BEIGE_SET_WHITE = [BEIGE_WHITE, EKURU_BEIGE_WHITE]

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GRAY = (192, 192, 192)

BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
LIGHT_BLUE = (24, 235, 249)
OCHER = (184, 136, 59)
PURPLE = (255, 0, 255)
MATCHA = (173, 179, 103)
BROWN = (134, 74, 43)

NUMBER_SET = [BLUE, GREEN, RED, LIGHT_BLUE, OCHER, PURPLE, MATCHA, BROWN]

# フォント
font = pygame.font.SysFont(None, 80)
font2 = pygame.font.SysFont(None, 40)

# ゲームオーバー時,クリア時各種
message1 = "GAME OVER"
message2 = "CLEAR!!"
gameover = font.render(message1, True, RED)
clear = font.render(message2, True, BLUE)
gameover_width, gameover_height = font.size(message1)
clear_width, clear_height = font.size(message2)
button = pygame.Rect(480, 540, 100, 40)
reset = font2.render("RESET", True, BLACK)

# 1辺
LEN = 9
BOMBS = 10

# 盤面 75-525
board = [[0 for _ in range(LEN)] for __ in range(LEN)]
opend = [[0 for _ in range(LEN)] for __ in range(LEN)]

# 状態 0: 初期, 1: プレイ中, 2: ゲームオーバー
state = 0

# 開けたマスの数
open_number = 0
rest_flags = BOMBS

# 時間
time = 0

# マウス
mouse_x, mouse_y = 0, 0
down_x, down_y = 0, 0
rl = 0
# フレームレート管理用
clock = pygame.time.Clock()

# 開ける処理(開けたマスが0マスなら四方8マスを開ける, 爆弾を開けたら0を返す)
def open(i, j):
    global open_number
    if opend[i][j] == 0:
        opend[i][j] = 1
        if board[i][j] == 0:
            if 0 < j: # 左
                open(i, j-1)
            if j < LEN - 1: # 右
                open(i, j+1)
            if 0 < i: # 上
                open(i-1, j)
            if i < LEN - 1: # 下
                open(i+1, j)
            if 0 < j and 0 < i: # 左上
                open(i-1, j-1)
            if 0 < j and i < LEN - 1: # 左下
                open(i+1, j-1)
            if j < LEN - 1 and 0 < i: # 右上
                open(i-1, j+1)
            if j < LEN - 1 and i < LEN - 1: # 右下
                open(i+1, j+1)
        if board[i][j] == -1:
            return 0
        open_number += 1
    return 1


running = True
while running:
    # 初期化
    down_x, down_y = 0, 0
    screen.fill(BLACK)
 
    # イベント処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            down_x, down_y = event.pos
            rl = event.button # 1で左クリック、3で右クリック
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # 初期状態のクリック処理    
    if state == 0 and 75 <= down_x < 525 and 75 <= down_y < 525:
        state = 1
        open_x = (down_x - 75) // 50
        open_y = (down_y - 75) // 50
        if rl == 1:
            # 盤面生成
            bomb_options = [i for i in range(LEN*LEN) if not (open_y - 1 <= i // LEN <= open_y + 1 and open_x - 1 <= i % LEN <= open_x + 1)]
            bomb_list = random.sample(bomb_options, BOMBS)
            for i in bomb_list:
                board[i // 9][i % 9] = -1
            for i in range(LEN):
                for j in range(LEN):
                    if board[i][j] != -1:
                        if 0 < j: # 左
                            if board[i][j-1] == -1: board[i][j] += 1
                        if j < LEN - 1: # 右
                            if board[i][j+1] == -1: board[i][j] += 1
                        if 0 < i: # 上
                            if board[i-1][j] == -1: board[i][j] += 1
                        if i < LEN - 1: # 下
                            if board[i+1][j] == -1: board[i][j] += 1
                        if 0 < j and 0 < i: # 左上
                            if board[i-1][j-1] == -1: board[i][j] += 1
                        if 0 < j and i < LEN - 1: # 左下
                            if board[i+1][j-1] == -1: board[i][j] += 1
                        if j < LEN - 1 and 0 < i: # 右上
                            if board[i-1][j+1] == -1: board[i][j] += 1
                        if j < LEN - 1 and i < LEN - 1: # 右下
                            if board[i+1][j+1] == -1: board[i][j] += 1
            open(open_y, open_x)
        if rl == 3:
            if opend[open_y][open_x] == 2:
                opend[open_y][open_x] = 0
                rest_flags += 1
            else:
                opend[open_y][open_x] = 2
                rest_flags -= 1
    
    # プレイ中のクリック処理
    elif state == 1 and 75 <= down_x < 525 and 75 <= down_y < 525:
        open_x = (down_x - 75) // 50
        open_y = (down_y - 75) // 50
        if opend[open_y][open_x] == 0:
            if rl == 1:
                if not open(open_y, open_x):
                    state = 2
            elif rl == 3:
                opend[open_y][open_x] = 2
                rest_flags -= 1
        elif opend[open_y][open_x] == 2 and rl == 3:
            opend[open_y][open_x] = 0
            rest_flags += 1

    # ゲームオーバー時,クリア時のクリック処理
    elif (state == 2 or state == 3) and 480 <= down_x <= 580 and 540 <= down_y <= 580:
        state = 0
        open_number = 0
        time = 0
        rest_flags = BOMBS
        board = [[0 for _ in range(LEN)] for __ in range(LEN)]
        opend = [[0 for _ in range(LEN)] for __ in range(LEN)]

    # 盤面描画
    for i in range(LEN):
        for j in range(LEN):
            xofj = 75 + 50 * j
            yofi = 75 + 50 * i
            if opend[i][j] == 0 or opend[i][j] == 2:
                if i == (mouse_y - 75) // 50 and j == (mouse_x - 75) // 50:
                    pygame.draw.rect(screen, GREEN_SET_WHITE[(i+j) % 2], (xofj, yofi, 50, 50))
                else:
                    pygame.draw.rect(screen, GREEN_SET[(i+j) % 2], (xofj, yofi, 50, 50))
                if opend[i][j] == 2:
                    pygame.draw.polygon(screen, RED, [(xofj + 10, yofi + 10), (xofj + 10, yofi + 20), (xofj + 40, yofi + 15)], 0)
                    pygame.draw.rect(screen, RED, (xofj + 9, yofi + 10, 2, 30))
            if opend[i][j] == 1:
                if board[i][j] == 0:
                    pygame.draw.rect(screen, BEIGE_SET[(i+j) % 2], (xofj, yofi, 50, 50))
                elif board[i][j] >= 1:
                    if i == (mouse_y - 75) // 50 and j == (mouse_x - 75) // 50:
                        pygame.draw.rect(screen, BEIGE_SET_WHITE[(i+j) % 2], (xofj, yofi, 50, 50))
                    else:
                        pygame.draw.rect(screen, BEIGE_SET[(i+j) % 2], (xofj, yofi, 50, 50))
                    text = font.render(str(board[i][j]), True, NUMBER_SET[board[i][j] - 1])
                    screen.blit(text, (xofj + 10, yofi))
                else:
                    pygame.draw.rect(screen, RED, (xofj, yofi, 50, 50))
                    pygame.draw.circle(screen, BLACK, (xofj + 25, yofi + 25), 10, width=0)

    # 時間, ハタ数表示
    time_message = "time:" + str(time // 30).zfill(3)
    time_text = font.render(time_message, True, WHITE)
    screen.blit(time_text, (330, 20))
    flag_x, flag_y = 100, 20
    pygame.draw.polygon(screen, RED, [(flag_x + 10, flag_y + 10), (flag_x + 10, flag_y + 20), (flag_x + 40, flag_y + 15)], 0)
    pygame.draw.rect(screen, RED, (flag_x + 9, flag_y + 10, 2, 30))
    flag_text = font.render(":" + str(rest_flags), True, WHITE)
    screen.blit(time_text, (330, 20))
    screen.blit(flag_text, (150, 20))

    # ゲームオーバー時表示
    if state == 2:
        screen.blit(gameover, (300 - gameover_width / 2, 530))
        if 480 <= mouse_x <= 580 and 540 <= mouse_y <= 580: 
            pygame.draw.rect(screen, WHITE, button)
        else:
            pygame.draw.rect(screen, LIGHT_GRAY, button)
        screen.blit(reset, (485, 545))
    
    # クリア時表示
    if state == 3:
        screen.blit(clear, (300 - clear_width / 2, 530))
        if 480 <= mouse_x <= 580 and 540 <= mouse_y <= 580: 
            pygame.draw.rect(screen, WHITE, button)
        else:
            pygame.draw.rect(screen, LIGHT_GRAY, button)
        screen.blit(reset, (485, 545))

    # クリア処理
    if open_number == LEN * LEN - BOMBS:
        state = 3

    # プレイ中ならば時間を進める
    if state == 1:
        time += 1

    pygame.display.flip()
    pygame.display.update()

    # 30FPSに設定
    clock.tick(30)

# 終了処理
pygame.quit()