"""Utils file with all of the helper functions"""

from commons.constants import NUMBER_CARDS, INITIAL_OPERANDS, COLORS, EXTRA_OPERANDS, CHIPS, LOW, HIGH, ROUNDS
from utils.game_elements import Card, Deck, Player
from typing import List

def generate_players(players: int) -> List[Player]:
    return [Player() for _ in range(players)]

def deal_until_number(deck: Deck) -> Card:
    card = deck.deal()
    # first card given should always be a number card
    while card.value not in NUMBER_CARDS:
        deck.add_card(card)
        card = deck.deal()
    return card

def deal_cards(deck: Deck, player: Player) -> None:
    """Initial round to deal cards to all the players."""
    # 1st card must be a number
    player.add_card_to_hand(deal_until_number(deck))

    # 2nd + 3rd card
    for _ in range(2):
        card = deck.deal()
        player.add_card_to_hand(card)
        if card.value == "*":
            # TODO: replace this with user inputs
            if Card("-", None) in player.hand:
                player.discard_card_from_hand(Card("-", None))
            else:
                player.discard_card_from_hand(Card("+", None))
        if card.value == "*" or card.value == "sqrt":
            player.add_card_to_hand(deal_until_number(deck))


def generate_deck() -> Deck:
    """Generate the deck of cards."""
    return Deck()

def shuffle_deck(deck: Deck) -> Deck:
    """Shuffle the deck of cards."""
    return deck.shuffle()

def add_card_to_deck(deck: Deck, card: Card) -> None:
    """Add card to the bottom of the deck."""
    deck.add_card(card)

def discard_card_from_hands(player: Player, discard: Card) -> None:
    """Discard one card from a Player's hand"""
    player.discard_card_from_hand(discard)

