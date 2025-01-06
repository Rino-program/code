import pygame
import random
import time

# 初期化
pygame.init()

# 画面サイズ
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("8192ゲーム")

# 日本語フォント設定
font_path = "C:/Windows/Fonts/msgothic.ttc"  # 日本語フォントファイルのパス
font = pygame.font.Font(font_path, 36)

# 色の定義
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

def reset_game():
    global count, result_text, running, reset_timer
    count = 0
    result_text = ""
    running = True
    reset_timer = None

reset_game()

# メインループ
while True:
    screen.fill(WHITE)
    
    # イベント処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if running:
                if event.key == pygame.K_b:  # 'b'キーで青を選択
                    i = 0
                elif event.key == pygame.K_g:  # 'g'キーで緑を選択
                    i = 1
                else:
                    continue
                
                x = random.randint(0, 1)
                if count == 0 and 2468 == random.randint(1, 8192):
                    result_text = "あなたは8192分の1を当てました!(裏ルート)"
                    running = False
                elif i == x:
                    result_text = "成功です。(一致)"
                    count += 1
                    if count == 13:
                        result_text = "ゲームクリア！"
                        running = False
                else:
                    result_text = "失敗です。(不一致)"
                    running = False
                if not running:
                    reset_timer = time.time() + 2  # 2秒後にリセット

    # テキスト描画
    count_text = font.render(f"{count+1}回目。あと{13-count}回です。", True, (0, 0, 0))
    prob_text = font.render(f"当たれば確率は 1/{2**(count+1)} です。", True, (0, 0, 0))
    screen.blit(count_text, (20, 20))
    screen.blit(prob_text, (20, 60))
    
    if result_text:
        result_display = font.render(result_text, True, (0, 0, 0))
        screen.blit(result_display, (20, 100))
        if "失敗" in result_text or "裏ルート" in result_text:
            reset_text = font.render("もう一度プレイするには 'r' キーを押してください。", True, (0, 0, 0))
            screen.blit(reset_text, (20, 140))
        elif reset_timer:
            remaining_time = int(reset_timer - time.time())
            reset_text = font.render(f"リセットまであと {remaining_time} 秒", True, (0, 0, 0))
            screen.blit(reset_text, (20, 140))
            if remaining_time <= 0:
                reset_game()
    
    pygame.display.flip()