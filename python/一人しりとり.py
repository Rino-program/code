def siritori():
    inp=input("最初の文字を入力:")
    while inp[-1]!="ん":
        inp_keep=inp
        inp=input(f"「{inp_keep[-1]}」で始まる次の文字を入力: ")
        while inp[0]!=inp_keep[-1]:
            print("しりとりになっていません。")
            inp=input(f"「{inp_keep[-1]}」で始まる文字を再入力してください: ")
        if inp[-1]=="ん":
            break
    print("「ん」が最後に付きました。しりとりを終わります。")
siritori()