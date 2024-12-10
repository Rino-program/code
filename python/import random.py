import random

class Card:
    def __init__(self, month, type, name):
        self.month = month
        self.type = type
        self.name = name

    def __repr__(self):
        return f"{self.month}月-{self.name}"

def create_deck():
    cards = [
        Card(1, '光', '松に鶴'), Card(1, '短冊', '松に赤短'), Card(1, 'カス', '松カス'), Card(1, 'カス', '松カス'),
        Card(2, 'タネ', '梅に鴬'), Card(2, '短冊', '梅に赤短'), Card(2, 'カス', '梅カス'), Card(2, 'カス', '梅カス'),
        Card(3, '光', '桜に幕'), Card(3, '短冊', '桜に赤短'), Card(3, 'カス', '桜カス'), Card(3, 'カス', '桜カス'),
        Card(4, 'タネ', '藤にホトトギス'), Card(4, '短冊', '藤に赤短'), Card(4, 'カス', '藤カス'), Card(4, 'カス', '藤カス'),
        Card(5, 'タネ', '菖蒲に八橋'), Card(5, '短冊', '菖蒲に青短'), Card(5, 'カス', '菖蒲カス'), Card(5, 'カス', '菖蒲カス'),
        Card(6, 'タネ', '牡丹に蝶'), Card(6, '短冊', '牡丹に青短'), Card(6, 'カス', '牡丹カス'), Card(6, 'カス', '牡丹カス'),
        Card(7, 'タネ', '萩に猪'), Card(7, '短冊', '萩に赤短'), Card(7, 'カス', '萩カス'), Card(7, 'カス', '萩カス'),
        Card(8, '光', '芒に月'), Card(8, 'タネ', '芒に雁'), Card(8, 'カス', '芒カス'), Card(8, 'カス', '芒カス'),
        Card(9, 'タネ', '菊に盃'), Card(9, '短冊', '菊に青短'), Card(9, 'カス', '菊カス'), Card(9, 'カス', '菊カス'),
        Card(10, 'タネ', '紅葉に鹿'), Card(10, '短冊', '紅葉に青短'), Card(10, 'カス', '紅葉カス'), Card(10, 'カス', '紅葉カス'),
        Card(11, '光', '柳に小野道風'), Card(11, 'タネ', '柳に燕'), Card(11, 'カス', '柳カス'), Card(11, 'カス', '柳カス'),
        Card(12, '光', '桐に鳳凰'), Card(12, 'カス', '桐カス'), Card(12, 'カス', '桐カス'), Card(12, 'カス', '桐カス')
    ]
    random.shuffle(cards)
    return cards

def deal_hands(deck):
    player_hand = deck[:8]
    cpu_hand = deck[8:16]
    field = deck[16:22]
    deck = deck[22:]
    return player_hand, cpu_hand, field, deck

def check_yaku(hand):
    yaku = {'光': 0, 'タネ': 0, '短冊': 0, 'カス': 0, '猪鹿蝶': 0}
    for card in hand:
        if card.name in ['牡丹に蝶', '萩に猪', '紅葉に鹿']:
            yaku['猪鹿蝶'] += 1
        yaku[card.type] += 1
    
    score = 0
    if yaku['光'] == 5:
        score += 10
    elif yaku['光'] == 4 and any(card.name == '柳に小野道風' for card in hand):
        score += 7
    elif yaku['光'] == 4:
        score += 7
    elif yaku['光'] == 3:
        score += 5
    if yaku['猪鹿蝶'] == 3:
        score += 5
    if yaku['タネ'] >= 5:
        score += yaku['タネ']-4
    if yaku['短冊'] >= 5:
        score += yaku['短冊']-4
    if yaku['カス'] >= 10:
        score += yaku['カス']-9
    if score >= 7:
        score *= 2
    print("役の判定:", yaku)
    print("得点:", score)
    
    return score

def player_turn(hand, field, player_taken, deck):
    print("あなたの手札:", hand)
    print("場のカード:", field)
    
    while True:
        try:
            choice = int(input(f"出すカードの番号を選んでください (0-{len(hand)-1}): "))
            if 0 <= choice < len(hand):
                card = hand.pop(choice)
                matched = False
                for fcard in field:
                    if fcard.month == card.month:
                        field.remove(fcard)
                        player_taken.append(card)
                        player_taken.append(fcard)
                        matched = True
                        break
                if not matched:
                    field.append(card)
                
                if deck:
                    new_card = deck.pop(0)
                    print(f"山から引いたカード: {new_card}")
                    matched = False
                    for fcard in field:
                        if fcard.month == new_card.month:
                            field.remove(fcard)
                            player_taken.append(new_card)
                            player_taken.append(fcard)
                            matched = True
                            break
                    if not matched:
                        field.append(new_card)
                break
            else:
                print("無効な選択です。もう一度選んでください。")
        except ValueError:
            print("無効な入力です。もう一度選んでください。")

def cpu_turn(hand, field, cpu_taken, deck):
    if hand:
        choice = random.choice(hand)
        hand.remove(choice)
        matched = False
        for fcard in field:
            if fcard.month == choice.month:
                field.remove(fcard)
                cpu_taken.append(choice)
                cpu_taken.append(fcard)
                matched = True
                break
        if not matched:
            field.append(choice)
    
        if deck:
            new_card = deck.pop(0)
            print(f"CPUが山から引いたカード: {new_card}")
            matched = False
            for fcard in field:
                if fcard.month == new_card.month:
                    field.remove(fcard)
                    cpu_taken.append(new_card)
                    cpu_taken.append(fcard)
                    matched = True
                    break
            if not matched:
                field.append(new_card)


deck = create_deck()
player_hand, cpu_hand, field, deck = deal_hands(deck)
player_taken = []
cpu_taken = []
player_turn_skip=0

def play_games():
    while player_hand or cpu_hand:
        if player_hand:
            player_turn(player_hand, field, player_taken, deck)
            player_score = check_yaku(player_taken)
            print("あなたの得点:", player_score)
            player_score_up=1
            if player_score >= player_score_up:  # 役が揃った場合
                print("役が揃いました！")
                if input("こいこいしますか？ﾊﾝｶｸ(y/n)：")=="y":
                    player_score_up=player_score+1
                break
            print("これまでにあなたが取った札:", player_taken)
            print("場のカード:", field)
        if cpu_hand:
            player_turn_skip=0
            cpu_turn(cpu_hand, field, cpu_taken, deck)
            cpu_score = check_yaku(cpu_taken)
            print("CPUの得点:", cpu_score)
            if cpu_score >= 1:  # 役が揃った場合
                print("CPUの役が揃いました！")
                break
            print("これまでにCPUが取った札:", cpu_taken)
            print("場のカード:", field)
    if cpu_score>=1 or not player_score_up>=player_score:

        player_score = check_yaku(player_taken)
        cpu_score = check_yaku(cpu_taken)

        print("ゲーム終了！")
        print("場のカード:", field)
        print("あなたが取った札:", player_taken)
        print("CPUが取った札:", cpu_taken)
        print("最終あなたの得点:", player_score)
        print("最終CPUの得点:", cpu_score)

        if player_score > cpu_score:
            print("あなたの勝ち！")
        elif player_score < cpu_score:
            print("CPUの勝ち！")
        else:
            print("引き分け！")
    else:
        player_turn_skip=1
        play_games()

play_games()
"""
    def create_deck(): cards = [ Card(1, '光', '松に鶴'), Card(1, '短冊', '松に赤短'), Card(1, 'カス', '松カス'), Card(1, 'カス', '松カス'), Card(2, 'タネ', '梅に鴬'), Card(2, '短冊', '梅に赤短'), Card(2, 'カス', '梅カス'), Card(2, 'カス', '梅カス'), Card(3, '光', '桜に幕'), Card(3, '短冊', '桜に赤短'), Card(3, 'カス', '桜カス'), Card(3, 'カス', '桜カス'), Card(4, 'タネ', '藤にホトトギス'), Card(4, '短冊', '藤に赤短'), Card(4, 'カス', '藤カス'), Card(4, 'カス', '藤カス'), Card(5, 'タネ', '菖蒲に八橋'), Card(5, '短冊', '菖蒲に青短'), Card(5, 'カス', '菖蒲カス'), Card(5, 'カス', '菖蒲カス'), Card(6, 'タネ', '牡丹に蝶'), Card(6, '短冊', '牡丹に青短'), Card(6, 'カス', '牡丹カス'), Card(6, 'カス', '牡丹カス'), Card(7, 'タネ', '萩に猪'), Card(7, '短冊', '萩に赤短'), Card(7, 'カス', '萩カス'), Card(7, 'カス', '萩カス'), Card(8, '光', '芒に月'), Card(8, 'タネ', '芒に雁'), Card(8, 'カス', '芒カス'), Card(8, 'カス', '芒カス'), Card(9, 'タネ', '菊に盃'), Card(9, '短冊', '菊に青短'), Card(9, 'カス', '菊カス'), Card(9, 'カス', '菊カス'), Card(10, 'タネ', '紅葉に鹿'), Card(10, '短冊', '紅葉に青短'), Card(10, 'カス', '紅葉カス'), Card(10, 'カス', '紅葉カス'), Card(11, '光', '柳に小野道風'), Card(11, 'タネ', '柳に燕'), Card(11, 'カス', '柳カス'), Card(11, 'カス', '柳カス'), Card(12, '光', '桐に鳳凰'), Card(12, 'カス', '桐カス'), Card(12, 'カス', '桐カス'), Card(12, 'カス', '桐カス') ] 
    random.shuffle(cards) 
    return cards
"""