import random
class Card:
    def __init__(self, month, type, name):
        self.month = month
        self.type = type
        self.name = name

    def __repr__(self):
        return f"{self.month}月-{self.name}"
def create_deck(): 
    cards = [ Card(1, '光', '松に鶴'), Card(1, '短冊', '松に赤短'), Card(1, 'カス', '松カス'), Card(1, 'カス', '松カス'), Card(2, 'タネ', '梅に鴬'), Card(2, '短冊', '梅に赤短'), Card(2, 'カス', '梅カス'), Card(2, 'カス', '梅カス'), Card(3, '光', '桜に幕'), Card(3, '短冊', '桜に赤短'), Card(3, 'カス', '桜カス'), Card(3, 'カス', '桜カス'), Card(4, 'タネ', '藤にホトトギス'), Card(4, '短冊', '藤に赤短'), Card(4, 'カス', '藤カス'), Card(4, 'カス', '藤カス'), Card(5, 'タネ', '菖蒲に八橋'), Card(5, '短冊', '菖蒲に青短'), Card(5, 'カス', '菖蒲カス'), Card(5, 'カス', '菖蒲カス'), Card(6, 'タネ', '牡丹に蝶'), Card(6, '短冊', '牡丹に青短'), Card(6, 'カス', '牡丹カス'), Card(6, 'カス', '牡丹カス'), Card(7, 'タネ', '萩に猪'), Card(7, '短冊', '萩に赤短'), Card(7, 'カス', '萩カス'), Card(7, 'カス', '萩カス'), Card(8, '光', '芒に月'), Card(8, 'タネ', '芒に雁'), Card(8, 'カス', '芒カス'), Card(8, 'カス', '芒カス'), Card(9, 'タネ', '菊に盃'), Card(9, '短冊', '菊に青短'), Card(9, 'カス', '菊カス'), Card(9, 'カス', '菊カス'), Card(10, 'タネ', '紅葉に鹿'), Card(10, '短冊', '紅葉に青短'), Card(10, 'カス', '紅葉カス'), Card(10, 'カス', '紅葉カス'), Card(11, '光', '柳に小野道風'), Card(11, 'タネ', '柳に燕'), Card(11, 'カス', '柳カス'), Card(11, 'カス', '柳カス'), Card(12, '光', '桐に鳳凰'), Card(12, 'カス', '桐カス'), Card(12, 'カス', '桐カス'), Card(12, 'カス', '桐カス') ] 
    print("シャッフル前:", cards) 
    random.shuffle(cards) 
    print("シャッフル後:", cards) 
    return cards # デッキを生成してシャッフル 
deck = create_deck()