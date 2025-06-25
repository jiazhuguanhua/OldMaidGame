import random
from player import Player

class OldMaidGame:
    def __init__(self, player_names):
        self.players = [Player(name) for name in player_names]
        self.deck = self.create_deck()
        self.current_player_index = 0
        self.game_over = False

    def create_deck(self):
        suits = ['♠', '♥', '♣', '♦']
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        deck = [(rank, suit) for suit in suits for rank in ranks]
        deck.remove(('Q', '♠'))  # 移除一张Q
        random.shuffle(deck)
        return deck

    def deal_cards(self):
        while self.deck:
            for player in self.players:
                if self.deck:
                    player.hand.append(self.deck.pop())
        for player in self.players:
            player.remove_pairs()

    def get_active_players(self):
        return [p for p in self.players if len(p.hand) > 0]

    def play_turn(self, draw_index):
        current = self.players[self.current_player_index]
        next_player = self.players[draw_index]
        card = current.draw_from(next_player)
        current.remove_pairs()
        # 检查出局
        out_players = []
        for player in self.players:
            if len(player.hand) == 0 and not hasattr(player, 'out'):
                player.out = True
                out_players.append(player.name)
        # 检查是否只剩一人
        active_players = self.get_active_players()
        if len(active_players) == 1:
            self.game_over = True
            return card, out_players, active_players[0].name
        return card, out_players, None

    def next_player(self):
        n = len(self.players)
        idx = (self.current_player_index + 1) % n
        while not self.players[idx].hand:
            idx = (idx + 1) % n
        self.current_player_index = idx
        return idx