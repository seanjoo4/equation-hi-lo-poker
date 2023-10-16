"""Implementing necessary Classes."""
import random

from collections import deque
from commons.constants import NUMBER_CARDS, INITIAL_OPERANDS, COLORS, EXTRA_OPERANDS, CHIPS, LOW, HIGH, ROUNDS
from typing import Any, Optional, Union

class Card:
    def __init__(self, value: Union[int, str], color: Optional[str]) -> None:
        self.value = value
        self.color = color

    def __eq__(self, other) -> bool:
        if isinstance(other, Card):
            return self.value == other.value and self.color == other.color
        return False
    
    def __str__(self) -> str:
        if self.color:
            return f"{self.value} of {self.color}"
        return str(self.value)

class Deck:
    def __init__(self) -> None:
        self.cards = deque(
                        [Card(card, color) for card in NUMBER_CARDS for color in COLORS] +
                        [Card(op, None) for op in EXTRA_OPERANDS]
                    )

    def shuffle(self) -> None:
        """Shuffle the deck of cards."""
        random.shuffle(self.cards)
        return self

    def add_card(self, card: str) -> None:
        """Add card to the bottom of the deck."""
        self.cards.append(card)

    def deal(self) -> Any:
        """Pop the top card on the deck."""
        return self.cards.popleft()
    
    def __str__(self) -> str:
        return f'Deck has {len(self.cards)} cards\n{", ".join(map(str, self.cards))}'

class Player:
    def __init__(self) -> None:
        self.hand = [Card(op, None) for op in INITIAL_OPERANDS]
        self.chips = CHIPS
    
    def add_card_to_hand(self, card: Card) -> None:
        self.hand.append(card)
    
    def discard_card_from_hand(self, discard: Card) -> None:
        if discard in self.hand:
            self.hand.remove(discard)

    def reset_hand(self) -> None:
        self.hand = INITIAL_OPERANDS
    
    def change_chip_count(self, amount: int, win: bool) -> None:
        if win:
            self.chips += amount
        else:
            self.chips -= amount

    def __str__(self) -> str:
        return f"Player's hand {len(self.hand)}:  {', '.join(map(str, self.hand))}"

