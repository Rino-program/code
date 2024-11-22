#条件分岐の練習
#git test
x=input("数字を入力")
try:
    x=int(x)
    if x==10:
        print("１０です")
    elif x>10:
        print("１０より大きいです")
    else:
        print("１０より小さいです")
except:
    print("エラー（数字ではない可能性があります）")
print("最終結果：x=={},type(x)=={},error=={}".format(x,type(x)))