# 迷路の最短経路をアニメーション表示（Pygame版）
import pygame
import sys
import time
from copy import deepcopy as dc

# --- 迷路データ（元のリストをそのまま使います） ---
maze = [
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0],
    [1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0]
]
start = (0, 0)
end = (29, 29)

# --- パラメータ ---
CELL = 20
WALL_COLOR = (40, 40, 40)
SPACE_COLOR = (240, 240, 240)
PATH_COLOR = (255, 120, 120)
VISITED_COLOR = (120, 200, 255)
START_COLOR = (120, 255, 120)
GOAL_COLOR = (255, 220, 60)
BORDER_COLOR = (0, 0, 0)

ROWS = len(maze)
COLS = len(maze[0])
WIDTH = (COLS + 2) * CELL
HEIGHT = (ROWS + 2) * CELL

# --- 壁で囲む処理 ---
def wall_maze(maze, start, end):
    new_maze = []
    new_maze.append(["."] * (len(maze[0]) + 2))
    for i in range(len(maze)):
        new_l = ["."]
        for j in range(len(maze[0])):
            if maze[i][j] == 0:
                new_l.append(0)
            else:
                new_l.append(".")
        new_l.append(".")
        new_maze.append(new_l)
    new_maze.append(["."] * (len(maze[0]) + 2))
    return new_maze

# --- 描画 ---
def draw_maze(screen, maze, route=None, visited=None, path_idx=None):
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            cell = maze[y][x]
            px = x * CELL
            py = y * CELL
            rect = pygame.Rect(px, py, CELL, CELL)
            if cell == ".":
                pygame.draw.rect(screen, WALL_COLOR, rect)
            elif cell == 0:
                pygame.draw.rect(screen, SPACE_COLOR, rect)
            else:  # visited cell (distance number or 's')
                pygame.draw.rect(screen, VISITED_COLOR, rect)
            pygame.draw.rect(screen, BORDER_COLOR, rect, 1)
    # 経路描画
    if visited:
        for (x, y) in visited:
            pygame.draw.rect(screen, VISITED_COLOR, pygame.Rect(x * CELL, y * CELL, CELL, CELL))
    if route:
        for i, (x, y) in enumerate(route):
            color = PATH_COLOR if (path_idx is None or i <= path_idx) else VISITED_COLOR
            pygame.draw.rect(screen, color, pygame.Rect(x * CELL, y * CELL, CELL, CELL))
    # スタート・ゴール
    pygame.draw.rect(screen, START_COLOR, pygame.Rect(truestart[0] * CELL, truestart[1] * CELL, CELL, CELL))
    pygame.draw.rect(screen, GOAL_COLOR, pygame.Rect(trueend[0] * CELL, trueend[1] * CELL, CELL, CELL))

# --- 探索・経路復元 ---
def bfs_with_animation(screen, new_maze, truestart, trueend):
    stack = [truestart]
    next_stack = []
    visited = set([truestart])
    new_maze[truestart[1]][truestart[0]] = 's'
    keep_maze = dc(new_maze)
    distance = 1
    prev = {truestart: None}
    finished = False
    route = None

    while not finished:
        check = False
        for x, y in stack:
            for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if new_maze[ny][nx] == 0:
                    new_maze[ny][nx] = distance
                    next_stack.append((nx, ny))
                    prev[(nx, ny)] = (x, y)
                    visited.add((nx, ny))
                    check = True
                    if (nx, ny) == trueend:
                        finished = True
        stack = next_stack
        next_stack = []
        distance += 1
        # 描画
        draw_maze(screen, new_maze, route=None, visited=visited)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        time.sleep(0.04)
        if not check:
            print("スタートとゴールがつながっていません。")
            return None, None
    # 経路復元
    path = []
    p = trueend
    while p and p in prev:
        path.append(p)
        p = prev[p]
    path = path[::-1]
    return new_maze, path

# --- メイン処理 ---
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("迷路の最短経路アニメーション")
    clock = pygame.time.Clock()

    trueend = (end[0]+1, end[1]+1)
    truestart = (start[0]+1, start[1]+1)
    new_maze = wall_maze(maze, start, end)

    # 探索
    result_maze, path = bfs_with_animation(screen, new_maze, truestart, trueend)
    if not path:
        pygame.quit()
        sys.exit()

    # 経路アニメーション
    for idx in range(len(path)):
        draw_maze(screen, result_maze, route=path, path_idx=idx)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        time.sleep(0.07)

    # 完成表示
    while True:
        draw_maze(screen, result_maze, route=path, path_idx=len(path)-1)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        clock.tick(30)
