from deck import Deck
from player import Player
def ai_decision(ai_player, deck):
    limit = 21 - ai_player.score
    if limit < 5:
        return False
    card_name, card_value = deck.draw_card()
    ai_player.add_card(card_name, card_value)
    return True
