"""Utils file with all of the helper functions"""

from commons.constants import NUMBER_CARDS, INITIAL_OPERANDS, COLORS, EXTRA_OPERANDS, CHIPS, LOW, HIGH, ROUNDS
from utils.game_elements import Card, Deck, Player
from typing import List

def generate_players(players: int) -> List[Player]:
    return [Player() for _ in range(players)]

def deal_cards(deck: Deck, players: Player) ->List[Player]:
    """Initial round to deal cards to all the players."""
    card = deck.deal()
    # first card given should always be a number card
    while card.value not in NUMBER_CARDS:
        deck.add_card(deck, card)
        card = deck.deal()
    Player().hand.append(card)
    def draw_special(deck: Deck, player: Player) -> Card:
        card = deck.deal()
        if card.value in NUMBER_CARDS:
            return card
        if card == "*":
            """Player needs to discard either +, -, or not take the * card"""
            player.discard_card_from_hand(Card("+"))
        if card == "*" or card == "sqr":
            while card.value not in NUMBER_CARDS:
                card = deck.deal()
        return card

def generate_deck() -> Deck:
    """Generate the deck of cards."""
    return Deck()

def shuffle_deck(deck: Deck) -> Deck:
    """Shuffle the deck of cards."""
    return deck.shuffle()

def add_card_to_deck(deck: Deck, card: Card) -> None:
    """Add card to the bottom of the deck."""
    deck.add(card)

def deal_card(deck: Deck) -> Card:
    """Pop the top card on the deck."""
    return deck.deal()

def discard_card_from_hands(player: Player, discard: Card) -> None:
    """Discard one card from a Player's hand"""
    player.discard_card_from_hand(discard)