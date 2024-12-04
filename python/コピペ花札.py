import random

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

random.shuffle(hanafuda_tiles)

field = [hanafuda_tiles.pop() for _ in range(8)]

hands = [hanafuda_tiles[i*8:(i+1)*8] for i in range(4)]

deck = hanafuda_tiles

print(f"プレイヤー 1: {hands[0]}")

for i in range(1, 4):
    print(f"プレイヤー {i + 1}: {'[HIDDEN]'}")

print(f"場のカード: {field}")

roles_scores = {
    '五光': 10, '四光': 8, '雨四光': 7, '三光': 6,
    '猪鹿蝶': 5, '花見酒': 5, '月見酒': 5,
    '赤短': 5, '青短': 5, 'たね': 5, 'たん': 5, 'カス': 1,
}

def player1_turn():
    print(f"場のカード: {field}")
    print(f"手札: {hands[0]}")
    card = input("プレイするカードを選んでください (例: 松に鶴): ")
    if card in hands[0]:
        hands[0].remove(card)
        if any(card.split('に')[0] in f for f in field):
            print(f"場のカードと一致しました: {card}")
            field_card = next(f for f in field if card.split('に')[0] in f)
            field.remove(field_card)
            hands[0].extend([card, field_card])
        else:
            field.append(card)
        print(f"現在の場のカード: {field}")
    else:
        print("無効なカードです。もう一度選んでください。")
        player1_turn()

    if deck:
        drawn_card = deck.pop(0)
        print(f"引いたカード: {drawn_card}")
        if any(drawn_card.split('に')[0] in f for f in field):
            print(f"場のカードと一致しました: {drawn_card}")
            field_card = next(f for f in field if drawn_card.split('に')[0] in f)
            field.remove(field_card)
            hands[0].extend([drawn_card, field_card])
        else:
            field.append(drawn_card)
        print(f"現在の場のカード: {field}")

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

    for role in ['猪鹿蝶', '花見酒', '月見酒', '赤短', '青短']:
        if counts[role] >= 3:
            score += roles_scores[role]

    if counts['たね'] >= 10:
        score += roles_scores['たね']

    if counts['たん'] >= 5:
        score += roles_scores['たん']

    if counts['カス'] >= 10:
        score += (counts['カス'] - 9) * roles_scores['カス']

    return score

def play_game():
    for turn in range(12):
        for i in range(4):
            if i == 0:
                player1_turn()
            else:
                print(f"プレイヤー {i + 1} のターン")
                if hands[i]:
                    card = hands[i].pop()
                    if any(card.split('に')[0] in f for f in field):
                        field_card = next(f for f in field if card.split('に')[0] in f)
                        field.remove(field_card)
                        hands[i].extend([card, field_card])
                    else:
                        field.append(card)

                    if deck:
                        drawn_card = deck.pop(0)
                        if any(drawn_card.split('に')[0] in f for f in field):
                            field_card = next(f for f in field if drawn_card.split('に')[0] in f)
                            field.remove(field_card)
                            hands[i].extend([drawn_card, field_card])
                        else:
                            field.append(drawn_card)
                print(f"現在の場のカード: {field}")

play_game()

for i, hand in enumerate(hands):
    score = calculate_score(hand)
    print(f"プレイヤー {i + 1} の最終手札: {hand if i == 0 else '[HIDDEN]'}")
    print(f"プレイヤー {i + 1} の得点: {score} 点")
