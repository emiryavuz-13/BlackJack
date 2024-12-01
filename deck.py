import random
class Deck:
    def __init__(self):
        self.cards = {
            "maca_as": 1, "maca_2": 2, "maca_3": 3, "maca_4": 4, "maca_5": 5, "maca_6": 6, "maca_7": 7,
            "maca_8": 8, "maca_9": 9, "maca_10": 10, "maca_kız": 10, "maca_papaz": 10, "maca_joker": 10,
            "kupa_as": 1, "kupa_2": 2, "kupa_3": 3, "kupa_4": 4, "kupa_5": 5, "kupa_6": 6, "kupa_7": 7,
            "kupa_8": 8, "kupa_9": 9, "kupa_10": 10, "kupa_kız": 10, "kupa_papaz": 10, "kupa_joker": 10,
            "karo_as": 1, "karo_2": 2, "karo_3": 3, "karo_4": 4, "karo_5": 5, "karo_6": 6, "karo_7": 7,
            "karo_8": 8, "karo_9": 9, "karo_10": 10, "karo_kız": 10, "karo_papaz": 10, "karo_joker": 10,
            "sinek_as": 1, "sinek_2": 2, "sinek_3": 3, "sinek_4": 4, "sinek_5": 5, "sinek_6": 6, "sinek_7": 7,
            "sinek_8": 8, "sinek_9": 9, "sinek_10": 10, "sinek_kız": 10, "sinek_papaz": 10, "sinek_joker": 10,
        }
        self.card_names = list(self.cards.keys())

    def draw_card(self):
        card = random.choice(self.card_names)
        self.card_names.remove(card)
        return card, self.cards[card]
