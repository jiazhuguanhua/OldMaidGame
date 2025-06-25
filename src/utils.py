def create_deck():
    """Create a standard Old Maid deck with one 'Old Maid' card."""
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    deck = [f"{rank} of {suit}" for rank in ranks for suit in suits]
    deck.append("Old Maid")  # Add the Old Maid card
    return deck

def shuffle_deck(deck):
    """Shuffle the deck of cards."""
    import random
    random.shuffle(deck)
    return deck