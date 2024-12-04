import random

# 花札の種類を定義
hanafuda_tiles = [
    '松に鶴', '松に赤短冊', '松にカス', '松にカス',
    '梅に鶯', '梅に赤短冊', '梅にカス', '梅にカス',
    '桜に幕', '桜に赤短冊', '桜にカス', '桜にカス',
    '藤に不如帰', '藤に短冊', '藤にカス', '藤にカス',
    '菖蒲に八橋', '菖蒲に短冊', '菖蒲にカス', '菖蒲にカス',
    '牡丹に蝶', '牡丹に短冊', '牡丹にカス', '牡丹にカス',
    '萩に猪', '萩に短冊', '萩にカス', '萩にカス',
    '芒に月', '芒に雁', '芒にカス', '芒にカス',
    '菊に盃', '菊に青短冊', '菊にカス', '菊にカス',
    '紅葉に鹿', '紅葉に青短冊', '紅葉にカス', '紅葉にカス',
    '柳に小野道風', '柳に燕', '柳に青短冊', '柳にカス',
    '桐に鳳凰', '桐にカス', '桐にカス', '桐にカス'
]

# 札をシャッフル
random.shuffle(hanafuda_tiles)

# 4人に分配
hands = [hanafuda_tiles[i::4] for i in range(4)]
field = []

# 各プレイヤーの手札を出力（分類せずにそのまま）
for i, hand in enumerate(hands):
    print(f"Player {i + 1}: {hand}")

# 役の点数を定義
roles_scores = {
    '五光': 10, '四光': 8, '雨四光': 7, '三光': 6,
    '猪鹿蝶': 5, '花見酒': 5, '月見酒': 5,
    '赤短': 5, '青短': 5, 'たね': 5, 'たん': 5, 'カス': 1,
    'てし': 5, 'くっつき': 3, 'ぶっく': 5
}

# ゲームの進行をシミュレート
def play_game():
    for turn in range(12):  # 12ターン（仮定）
        for i in range(4):  # 4人のプレイヤー
            if hands[i]:
                # プレイヤーが札を引く
                card = hands[i].pop()
                print(f"Player {i + 1} plays {card}")
                field.append(card)
                print(f"Current field: {field}")
            else:
                print(f"Player {i + 1} has no cards left")

            # 簡単なルールでペアができたら取得（仮定）
            # 実際のゲームでは詳細なルールに基づいて処理
            pairs = [(f, c) for f in field for c in field if f != c and f.split('に')[0] == c.split('に')[0]]
            if pairs:
                print(f"Pairs formed: {pairs}")
                for pair in pairs:
                    if pair[0] in field and pair[1] in field:
                        field.remove(pair[0])
                        field.remove(pair[1])
                        hands[i].extend(pair)  # 取得した札をプレイヤーに追加

# 役の判定と点数計算
def calculate_score(hand):
    score = 0
    card_count = {
        '五光': ['松に鶴', '桐に鳳凰', '芒に月', '桜に幕', '柳に小野道風'],
        '猪鹿蝶': ['萩に猪', '紅葉に鹿', '牡丹に蝶'],
        '花見酒': ['桜に幕', '菊に盃'],
        '月見酒': ['芒に月', '菊に盃'],
        '赤短': ['松に赤短冊', '梅に赤短冊', '桜に赤短冊'],
        '青短': ['菊に青短冊', '紅葉に青短冊', '柳に青短冊'],
        'たね': ['松に鶴', '梅に鶯', '桜に幕', '藤に不如帰', '菖蒲に八橋', '牡丹に蝶', '萩に猪', '芒に雁', '菊に盃', '紅葉に鹿', '柳に燕', '桐に鳳凰'],
        'たん': ['松に赤短冊', '梅に赤短冊', '桜に赤短冊', '藤に短冊', '菖蒲に短冊', '牡丹に短冊', '萩に短冊', '芒に短冊', '菊に青短冊', '紅葉に青短冊', '柳に青短冊'],
        'カス': ['カス'],
        'てし': ['松に鶴', '桐に鳳凰', '芒に月', '桜に幕', '柳に小野道風'],
        'くっつき': ['松に赤短冊', '梅に赤短冊', '桜に赤短冊', '菊に青短冊', '紅葉に青短冊', '柳に青短冊'],
        'ぶっく': ['松に赤短冊', '梅に赤短冊', '桜に赤短冊', '菊に青短冊', '紅葉に青短冊', '柳に青短冊']
    }

    counts = {role: 0 for role in roles_scores.keys()}

    for card in hand:
        for role, tiles in card_count.items():
            if card in tiles:
                counts[role] += 1

    if counts['五光'] == 5:
        score += roles_scores['五光']
    elif counts['四光'] == 4:
        if '柳に小野道風' in hand:
            score += roles_scores['雨四光']
        else:
            score += roles_scores['四光']
    elif counts['三光'] == 3:
        score += roles_scores['三光']
    
    if counts['てし'] == 4:
        score += roles_scores['てし']

    for role in ['猪鹿蝶', '花見酒', '月見酒', '赤短', '青短', 'くっつき']:
        if counts[role] >= 3:
            score += roles_scores[role]

    if counts['たね'] >= 10:
        score += roles_scores['たね']

    if counts['たん'] >= 5:
        score += roles_scores['たん']

    if counts['ぶっく'] >= 3:
        score += roles_scores['ぶっく']

    if counts['カス'] >= 10:
        score += (counts['カス'] - 9) * roles_scores['カス']

    return score

# ゲームを実行
play_game()

# 最終結果と点数計算
for i, hand in enumerate(hands):
    score = calculate_score(hand)
    print(f"Player {i + 1}'s final hand: {hand}")
    print(f"Player {i + 1}'s score: {score} points")
