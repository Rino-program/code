# 練習問題 8: アナグラムの判定
# アナグラムとは、言葉の文字を並び替えて、別の言葉や文を作る遊びです。回文（上から読んでも下から読んでも同じ）と異なり、文字の順番を入れ替えるのが特徴です。例えば、「時計（とけい）」を並び替えて「毛糸（けいと）」を作るなどが挙げられます。
def f(txt_before, txt_after):
    return sorted(txt_before) == sorted(txt_after)

t1 = input("入力1:")
t2 = input("入力2:")
print("アナグラムです" if f(t1, t2) == True else "アナグラムではありません")

# 練習問題 9: 辞書内の特定キーの合計値
data = [{"score": 10}, {"score": 20}, {"score": 30}]
x = input("入力:")
print(sum(i[x] for i in data))