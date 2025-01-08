#Microsoft Copilotからの出題(練習) ～数独処理～
x=[
    [0, 3, 0, 0, 8, 0, 0, 0, 0],
    [7, 4, 0, 0, 0, 1, 2 ,8, 0],
    [2, 0, 8, 0, 4, 9, 3, 0, 6],
    [0, 0, 3, 8, 0, 0, 0, 6, 2],
    [0, 9, 0, 0, 0, 0, 0, 0, 7],
    [0, 0, 1, 0, 0, 3, 0, 4, 8],
    [0, 8, 0, 1, 0, 0, 0, 0, 0],
    [0, 5, 0, 0, 2, 0, 0, 9, 0],
    [4, 0, 0, 7, 3, 5, 0, 2, 0]
]
def f(li):
    for i in range(9):
        for j in range(9):
            if li[i][j]==0:
                for k in range(1,10):
                    if not k in li[i] and not k in [li[l][j] for l in range(9)] and not k in [li[l][m] for l in range(i//3*3,i//3*3+3) for m in range(j//3*3,j//3*3+3)]:
                        li[i][j] = k
x = f(x)
for i in range(9):
    print(x[i])