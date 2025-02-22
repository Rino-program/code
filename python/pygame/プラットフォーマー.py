# 改良１慣性の法則の適応
import pygame

# 初期化
pygame.init()

# 画面設定
width, height = 1000, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("プラットフォーマー")

# 四角の初期設定
rect_color = (93, 192, 0)         # 赤色
rect_x, rect_y = 700, 500          # 初期位置
rect_width, rect_height = 15, 15
speed = 0.3                      # 移動速度

# フレームレート管理用
clock = pygame.time.Clock()

# 色々な変数
friction = {"x": 0.08, "y": 0.08} # 摩擦係数
acceleration = {"x": 0, "y": 0} # 加速度
maxspeed = 9                   # 最大速度

# 重力とジャンプの設定
gravity = 0.5
jump_strength = 15
is_jumping = False

# 地面の設定
ground_y = 400

# プラットフォームの設定
platforms = [
    pygame.Rect(200, 400, 100, 10),
    pygame.Rect(400, 300, 100, 10),
    pygame.Rect(600, 200, 200, 10)
]

running = True
while running:
    # イベント処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # キーの状態を取得
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and acceleration["x"] > -maxspeed:
        acceleration["x"] -= speed
    if keys[pygame.K_RIGHT] and acceleration["x"] < maxspeed:
        acceleration["x"] += speed
    if keys[pygame.K_UP] and not is_jumping:
        is_jumping = True
        acceleration["y"] = -jump_strength

    # 位置の更新
    rect_x += acceleration["x"]
    rect_y += acceleration["y"]

    # 地面との衝突判定
    if rect_y >= ground_y:
        rect_y = ground_y
        is_jumping = False
        acceleration["y"] = 0

    # プラットフォームとの衝突判定
    for platform in platforms:
        rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)
        if rect.colliderect(platform):
            # プレイヤーがプラットフォームの上に乗る場合
            if acceleration["y"] > 0 and rect.bottom <= platform.bottom:
                rect_y = platform.top - rect_height
                is_jumping = False
                acceleration["y"] = 0
            # プレイヤーがプラットフォームの下にぶつかる場合
            elif acceleration["y"] < 0 and rect.top >= platform.top:
                rect_y = platform.bottom
                acceleration["y"] = 0
            # プレイヤーがプラットフォームの左側にぶつかる場合
            elif acceleration["x"] > 0 and rect.right >= platform.left:
                rect_x = platform.left - rect_width
                acceleration["x"] = 0
            # プレイヤーがプラットフォームの右側にぶつかる場合
            elif acceleration["x"] < 0 and rect.left <= platform.right:
                rect_x = platform.right
                acceleration["x"] = 0

    # 摩擦を適応
    if acceleration["x"] > 0:
        acceleration["x"] -= friction["x"]
        if acceleration["x"] < 0:  # 逆符号になったら 0
            acceleration["x"] = 0
    elif acceleration["x"] < 0:
        acceleration["x"] += friction["x"]
        if acceleration["x"] > 0:  # 逆符号になったら 0
            acceleration["x"] = 0

    if is_jumping:
        acceleration["y"] += gravity

    # 画面更新処理
    screen.fill((255, 255, 255))  # 背景を白で塗りつぶす
    pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, rect_height))

    # プラットフォームの描画
    for platform in platforms:
        pygame.draw.rect(screen, (0, 0, 0), platform)

    pygame.display.update()

    # 60FPSに設定
    clock.tick(60)

# 終了処理
pygame.quit()
