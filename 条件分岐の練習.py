
x=input("数字を入力")
error=0
try:
    x=int(x)
except:
    print("エラー（数字ではない可能性があります）")
    error=1
try:
    if x==10:
        print("１０です")
    elif x>10:
        print("１０より大きいです")
    else:
        print("１０より小さいです")
except:
    if error==0:
        print("エラー（数字ではない可能性があります）")
print("最終結果：x=={},type(x)=={},error=={}".format(x,type(x),error))