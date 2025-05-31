from copy import deepcopy
x = input() # 目標
n = 0
t = ""
queue = [t]
queue_top = set()
queue_top_n = set()
next_queue = []
while x not in queue:
    next_queue = []
    n += 1
    for i in queue:
        b = ""
        if len(i) < len(x):
            if i not in queue_top:
                next_queue.append(i + "0")
        if i:
            for j in i:
                if j == "9":
                    b += "0"
                else:
                    b += str(int(j) + 1)
            if i not in queue_top:
                next_queue.append(b)
    queue_top = queue_top | (queue_top_n & set(next_queue))
    queue_top_n = queue_top_n | set(next_queue)
    # 集合に入ってるものは次のキューに入れない
    c = 0
    for i in range(len(next_queue)):
        if next_queue[i - c] in queue_top:
            next_queue.pop(i - c)
            c += 1
    queue = deepcopy(next_queue)
    print(n, len(queue), queue[:15])
    if len(queue) > 100000000:
        print("Too many iterations")
        break
print(n)