class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0
    def add_card(self, card_name, card_value):
        self.hand.append(card_name)
        self.score += card_value
