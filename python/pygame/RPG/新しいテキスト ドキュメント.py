import pygame
import sys
import random

# 初期化
pygame.init()

# 画面サイズ
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("革命的ブロック崩し")

# 色の定義
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)
orange = (255, 165, 0)
purple = (160, 32, 240)
pink = (255, 192, 203)
colors = [green, yellow, orange, purple, red, blue]

# パドルの設定
paddle_width = 100
paddle_height = 10
paddle_x = (screen_width - paddle_width) // 2
paddle_y = screen_height - 30
paddle_speed = 10
paddle_color = white

# ボールの設定
ball_size = 10
ball_speed = 5
balls = [{"x": screen_width // 2, "y": screen_height // 2, "dx": ball_speed, "dy": -ball_speed, "color": red}]

# ブロックの設定
block_rows = 5
block_columns = 10
block_width = screen_width // block_columns
block_height = 20
blocks = []
special_blocks = []
boss = None

def create_blocks():
    blocks.clear()
    special_blocks.clear()
    for row in range(block_rows):
        for col in range(block_columns):
            if random.random() > 0.3:  # ランダムにブロックを配置
                block = pygame.Rect(col * block_width, row * block_height, block_width, block_height)
                blocks.append(block)
                if random.random() > 0.9:  # 特別なブロックの配置
                    special_blocks.append(block)

def spawn_boss():
    global boss
    boss = {"rect": pygame.Rect(screen_width // 2 - 50, 50, 100, 30), "health": 10}

create_blocks()

# スコアの設定
score = 0
combo = 0
font = pygame.font.Font(None, 36)

# HPの設定
player_hp = 3

# パワーアップアイテムの設定
power_up_types = ["widen_paddle", "add_ball", "increase_score", "change_paddle_color", "slow_ball", "heal"]
power_up_base_chance = 0.3
power_up_chance = power_up_base_chance
power_up_speed = 3
power_ups = []

def spawn_power_up(x, y):
    power_up_type = random.choice(power_up_types)
    power_up = {"rect": pygame.Rect(x, y, 20, 20), "type": power_up_type}
    power_ups.append(power_up)

def avoid_overlap_with_balls(new_rect):
    for ball in balls:
        ball_rect = pygame.Rect(ball["x"], ball["y"], ball_size, ball_size)
        if new_rect.colliderect(ball_rect):
            return False
    return True

def change_paddle_color():
    global paddle_color
    paddle_color = random.choice(colors)

def slow_down_balls():
    for ball in balls:
        ball["dx"] *= 0.5
        ball["dy"] *= 0.5

def speed_up_balls():
    for ball in balls:
        ball["dx"] *= 2
        ball["dy"] *= 2

def check_combo():
    global combo
    combo += 1
    if combo > 1:
        return combo * 10  # コンボボーナス
    return 0

def reset_ball():
    global balls
    balls = [{"x": screen_width // 2, "y": screen_height // 2, "dx": ball_speed, "dy": -ball_speed, "color": red}]

# メインループ
level = 1
running = True
slow_ball_active = False
slow_ball_start_time = 0
slow_ball_duration = 5000  # 5秒

while running:
    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # キー入力の処理
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < screen_width - paddle_width:
        paddle_x += paddle_speed

    # ボールの移動
    for ball in balls:
        ball["x"] += ball["dx"]
        ball["y"] += ball["dy"]

        # 壁との衝突判定
        if ball["x"] <= 0 or ball["x"] >= screen_width - ball_size:
            ball["dx"] = -ball["dx"]
        if ball["y"] <= 0:
            ball["dy"] = -ball["dy"]

        # パドルとの衝突判定
        paddle_rect = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)
        ball_rect = pygame.Rect(ball["x"], ball["y"], ball_size, ball_size)
        if ball_rect.colliderect(paddle_rect):
            ball["dy"] = -ball["dy"]

        # ブロックとの衝突判定
        for block in blocks[:]:
            if ball_rect.colliderect(block):
                blocks.remove(block)
                ball["dy"] = -ball["dy"]
                score += 10 + check_combo()
                if block in special_blocks:
                    # 特別なブロックの効果
                    score += 100
                    special_blocks.remove(block)
                if random.random() < power_up_chance:
                    new_power_up_rect = pygame.Rect(block.x, block.y, 20, 20)
                    if avoid_overlap_with_balls(new_power_up_rect):
                        spawn_power_up(block.x, block.y)
                break

        # ボスとの衝突判定
        if boss and ball_rect.colliderect(boss["rect"]):
            boss["health"] -= 1
            ball["dy"] = -ball["dy"]
            if boss["health"] <= 0:
                boss = None
                score += 500

    # パワーアップアイテムの移動と取得
    for power_up in power_ups[:]:
        power_up["rect"].y += power_up_speed
        if power_up["rect"].colliderect(paddle_rect):
            if power_up["type"] == "widen_paddle":
                paddle_width += 20
            elif power_up["type"] == "add_ball":
                balls.append({"x": paddle_x + paddle_width // 2, "y": paddle_y - ball_size, "dx": ball_speed, "dy": -ball_speed, "color": random.choice(colors)})
            elif power_up["type"] == "increase_score":
                score += 50
            elif power_up["type"] == "change_paddle_color":
                change_paddle_color()
            elif power_up["type"] == "slow_ball":
                slow_down_balls()
                slow_ball_active = True
                slow_ball_start_time = current_time
            elif power_up["type"] == "heal":
                player_hp = min(player_hp + 1, 3)  # HPを1回復（最大3）
            power_ups.remove(power_up)
        elif power_up["rect"].y > screen_height:
            power_ups.remove(power_up)

    # パワーアップ効果の終了
    if slow_ball_active and current_time - slow_ball_start_time > slow_ball_duration:
        speed_up_balls()
        slow_ball_active = False

    # 画面クリア
    screen.fill(black)

    # スコアとコンボの描画
    score_text = font.render(f"Score: {score}", True, white)
    combo_text = font.render(f"Combo: {combo}", True, white)
    hp_text = font.render(f"HP: {player_hp}", True, white)
    screen.blit(score_text, (10, 10))
    screen.blit(combo_text, (10, 50))
    screen.blit(hp_text, (10, 90))

    # パドルの描画
    paddle_rect.width = paddle_width
    pygame.draw.rect(screen, paddle_color, paddle_rect)

    # ボールの描画
    for ball in balls:
        ball_rect = pygame.Rect(ball["x"], ball["y"], ball_size, ball_size)
        pygame.draw.ellipse(screen, ball["color"], ball_rect)

    # ブロックの描画
    for block in blocks:
        pygame.draw.rect(screen, blue, block)

    # 特別なブロックの描画
    for block in special_blocks:
        pygame.draw.rect(screen, red, block)

    # ボスの描画
    if boss:
        pygame.draw.rect(screen, purple, boss["rect"])
        boss_health_text = font.render(f"Boss Health: {boss['health']}", True, white)
        screen.blit(boss_health_text, (screen_width // 2 - boss_health_text.get_width() // 2, 10))

    # パワーアップアイテムの描画
    for power_up in power_ups:
        if power_up["type"] == "widen_paddle":
            color = green
        elif power_up["type"] == "add_ball":
            color = yellow
        elif power_up["type"] == "increase_score":
            color = orange
        elif power_up["type"] == "change_paddle_color":
            color = purple
        elif power_up["type"] == "slow_ball":
            color = white
        elif power_up["type"] == "heal":
            color = pink
        pygame.draw.rect(screen, color, power_up["rect"])

    # ゲームオーバー判定
    if all(ball["y"] >= screen_height for ball in balls):
        player_hp -= 1
        if player_hp > 0:
            reset_ball()
        else:
            text = font.render("Game Over", True, white)
            screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height() // 2))
            pygame.display.flip()
            pygame.time.wait(3000)
            running = False

    # ゲームクリア判定
    if not blocks and not boss:
        level += 1
        ball_speed += 1
        power_up_chance = power_up_base_chance + (level * 0.05)  # レベルアップごとにパワーアップの出現確率を増加
        for ball in balls:
            ball["dx"] = ball_speed if ball["dx"] > 0 else -ball_speed
            ball["dy"] = ball_speed if ball["dy"] > 0 else -ball_speed
        if level % 3 == 0:  # 3レベルごとにボスが登場
            spawn_boss()
        else:
            create_blocks()
        text = font.render(f"Level {level}", True, white)
        screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(2000)

    # 画面更新
    pygame.display.flip()

    # フレームレート
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()