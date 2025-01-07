# 迷路の解決: 迷路を表現した2次元リストを入力として受け取り、スタートからゴールまでの最短経路を見つけるプログラムを作成してください。
from copy import deepcopy as dc
maze = [
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0]
]
start = (0, 0)  # スタート地点 (行, 列)
end = (19, 19)    # ゴール地点 (行, 列)
trueend = ((end[0]+1, end[1]+1))
truestart = ((start[0]+1, start[1]+1))

stack = [(start[0] + 1, start[1] + 1)]
next_stack = []

new_maze = []

new_maze.append(["."]*(len(maze[0])+2))

for i in range(len(maze)):
    new_l = ["."]
    for j in range(len(maze[0])):
        if maze[i][j] == 0:
            new_l.append(0)
        else:
            new_l.append(".")
    new_l.append(".")
    new_maze.append(new_l)

new_maze.append(["."]*(len(maze[0])+2))

new_maze[stack[0][1]][stack[0][0]] = 's'

keep_maze = dc(new_maze)

distance = 1
while trueend not in stack:
    for x, y in stack:
        for i in range(4):
            if i == 0: # 上
                if new_maze[y - 1][x] == 0:
                    new_maze[y - 1][x] = distance
                    next_stack.append((x, y - 1))
            if i == 1: # 右
                if new_maze[y][x + 1] == 0:
                    new_maze[y][x + 1] = distance
                    next_stack.append((x + 1, y))
            if i == 2: # 下
                if new_maze[y + 1][x] == 0:
                    new_maze[y + 1][x] = distance
                    next_stack.append((x, y + 1))
            if i == 3: # 左
                if new_maze[y][x - 1] == 0:
                    new_maze[y][x - 1] = distance
                    next_stack.append((x - 1, y))
    stack = next_stack
    next_stack = []
    distance += 1

for i in new_maze:
    print(i)
x, y = trueend
distance = new_maze[y][x]
print(f"距離:{distance}")

# 逆順にたどる
while distance > 1:
    moved = False
    for i in range(4):
        if i == 0 and y > 0:  # 上
            if new_maze[y - 1][x] == distance - 1:
                y -= 1
                distance -= 1
                keep_maze[y][x] = 2
                break
        if i == 1 and x < len(new_maze[0]) - 1:  # 右
            if new_maze[y][x + 1] == distance - 1:
                x += 1
                distance -= 1
                keep_maze[y][x] = 2
                break
        if i == 2 and y < len(new_maze) - 1:  # 下
            if new_maze[y + 1][x] == distance - 1:
                y += 1
                distance -= 1
                keep_maze[y][x] = 2
                break
        if i == 3 and x > 0:  # 左
            if new_maze[y][x - 1] == distance - 1:
                x -= 1
                distance -= 1
                keep_maze[y][x] = 2
                break

for i in keep_maze:
    for j in i:
        if j == ".":
            i[i.index(j)] = 1
        elif j == "s":
            i[i.index(j)] = 3

keep_maze[trueend[1]][trueend[0]] = 4

# マップを出力
for row in keep_maze:
    print(' '.join(str(cell) for cell in row))