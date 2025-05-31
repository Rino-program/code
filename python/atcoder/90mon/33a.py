# coding: utf-8
# 033 - Not Too Bright
import sys
h, w = tuple(map(int, input().split()))
if h == 1:
  print(w)
  sys.exit()
elif w == 1:
  print(h)
  sys.exit()
maze = [["." for j in range(w)] for i in range(h)]
new_maze = []

new_maze.append(["0"]*(len(maze[0])+2))

for i in maze:
    n = ["0"]
    for j in i:
        n += [j]
    n += ["0"]
    new_maze.append(n)

new_maze.append(["0"]*(len(maze[0])+2))

s = 0

for i in range(1, h + 1):
    for j in range(1, w + 1):
        li = []
        n = 0
        for k in range(-1, 2):
            for m in range(-1, 2):
                if new_maze[i + k][j + m] == "#":
                    n = 1
                    break
            if n == 1:
                break
        if n == 0:
            new_maze[i][j] = "#"
            s += 1
print(s)
