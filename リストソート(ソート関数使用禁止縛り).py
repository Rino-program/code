def li(x):
  if len(x)<2:
    return x
  for i in range(len(x)-1):
    if x[i] < x[i+1] or x[i] == x[i+1]:
      pass
    elif x[i] > x[i+1]:
      x.insert(i,x[i+1])
print(li(list(map(int,input("リストを入力してください。").split(",")))))
