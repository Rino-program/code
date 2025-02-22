# ポンゲームを作ってみる
# 作成開始日：2025/02/22
# 作成者：花音♬
# 協同作成者(AI)：GitHub Copilot

# 改善点リスト
"""
〜重要〜
スペルミス:boll→ball
〜改善〜
1. 反射の時にもう少し乱数を加えて予測を少し難しくする
2. ボールを少しずつ加速させる。ただし、プレイヤーが跳ね返した時のみ。また、一試合ごとにリセットさせる
3. 一人用にほどほどに勝てそうな対戦相手(bot)を作る
4. 演出をもっと考える(追加)
5. ボールが斜めにしか動かない
"""

import pygame
import sys
import random

# 初期化
pygame.init()

# 画面を作成
screen = pygame.display.set_mode((800, 600))

# タイトル
pygame.display.set_caption("Pong Game")

# 時間管理
clock = pygame.time.Clock()

# 色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 物体
player_A = pygame.Rect(50, 250, 10, 100)
player_B = pygame.Rect(740, 250, 10, 100)
boll = pygame.Rect(395, 295, 20, 20)

# 速度
boll_speed = 3
boll_dx = boll_speed
boll_dy = boll_speed

# スコア
score = {"player_A": 0, "player_B": 0}
font = pygame.font.Font(None, 74)

# 本編
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # キー入力
    keys = pygame.key.get_pressed()
    # プレイヤーA
    if keys[pygame.K_w]:
        player_A.y -= 7
    if keys[pygame.K_s]:
        player_A.y += 7
    # プレイヤーB
    if keys[pygame.K_UP]:
        player_B.y -= 7
    if keys[pygame.K_DOWN]:
        player_B.y += 7

    # プレイヤーAの移動
    if player_A.top <= 0:
        player_A.top = 0
    if player_A.bottom >= 600:
        player_A.bottom = 600
    # プレイヤーBの移動
    if player_B.top <= 0:
        player_B.top = 0
    if player_B.bottom >= 600:
        player_B.bottom = 600

    # ボールの移動
    boll.x += boll_dx
    boll.y += boll_dy
    # ボールの当たり判定
    if boll.top <= 0 or boll.bottom >= 600:
        boll_dy *= -1
    if boll.colliderect(player_A):
        boll_dx = boll_speed
    if boll.colliderect(player_B):
        boll_dx = -boll_speed
    if boll.left <= 0:
        score["player_B"] += 1
        boll.x = 395
        boll.y = 295
        boll_dx = boll_speed * random.choice((1, -1))
        boll_dy = boll_speed * random.choice((1, -1))
    if boll.right >= 800:
        score["player_A"] += 1
        boll.x = 395
        boll.y = 295
        boll_dx = boll_speed * random.choice((1, -1))
        boll_dy = boll_speed * random.choice((1, -1))

    # 画面の更新など
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player_A)
    pygame.draw.rect(screen, WHITE, player_B)
    pygame.draw.ellipse(screen, WHITE, boll)
    score_surface = font.render(f"{score['player_A']} : {score['player_B']}", True, WHITE)
    screen.blit(score_surface, (300, 10))
    pygame.display.flip()
    clock.tick(60)

# 終了
pygame.quit()
sys.exit()
