from deck import Deck
from player import Player
from game_logic import ai_decision
from utlis import delay_effect


def main():
    deck = Deck()
    player = Player("Oyuncu 1")
    ai = Player("Yapay Zeka")

    # İlk kart çekimleri
    for _ in range(2):
        card_name, card_value = deck.draw_card()
        player.add_card(card_name, card_value)

        card_name, card_value = deck.draw_card()
        ai.add_card(card_name, card_value)

    # Oyunun başlangıcı
    print(f"{player.name} kartları: {player.hand} (Skor: {player.score})")
    print(f"{ai.name} kartları: [Gizli]")

    # Oyun döngüsü
    while True:
        delay_effect()
        if ai_decision(ai, deck):
            print(f"{ai.name} bir kart çekti.")
        else:
            print(f"{ai.name} pas geçti.")
        print(f"{player.name} Skor: {player.score}")
        choice = input("Devam mı (d) yoksa tamam mı (t)? ").lower()
        if choice == "d":
            card_name, card_value = deck.draw_card()
            player.add_card(card_name, card_value)
            print(f"Yeni kart: {card_name} (Skor: {player.score})")

            if player.score > 21:
                print("21'i geçtiniz! Kaybettiniz!")
                break
        elif choice == "t":
            print(f"{player.name} pas geçti. Skor: {player.score}")
            while True:
                delay_effect()
                if ai_decision(ai, deck):
                    print(f"{ai.name} bir kart çekti.")
                else:
                    print(f"{ai.name} pas geçti.")
                    break
            break

    # Kazananı belirleme
    print(f"{ai.name} kartları: {ai.hand} (Skor: {ai.score})")
    print(f"{player.name} Skor: {player.score}")
    print(f"{ai.name} Skor: {ai.score}")
    if player.score > 21:
        print("Kaybettiniz!")
    elif ai.score > 21 or player.score > ai.score:
        print("Kazandınız!")
    elif player.score == ai.score:
        print("Berabere!")
    else:
        print("Kaybettiniz!")


if __name__ == "__main__":
    main()
