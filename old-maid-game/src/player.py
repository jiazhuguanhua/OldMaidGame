import random

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def remove_pairs(self):
        # 移除配对
        counts = {}
        for card in self.hand:
            key = card[0]
            counts.setdefault(key, []).append(card)
        new_hand = []
        for cards in counts.values():
            if len(cards) % 2 == 1:
                new_hand.append(cards[0])
        self.hand = new_hand

    def draw_from(self, other):
        if not other.hand:
            return None
        card = random.choice(other.hand)
        other.hand.remove(card)
        self.hand.append(card)
        return card