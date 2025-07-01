from typing import Iterator, NamedTuple, Sequence, Union


class Card(NamedTuple):
    rank: str
    suit: str


class CardDeck(Sequence):
    def __init__(self) -> None:
        """
        Creates a CardDeck instance

        >>> deck = CardDeck()
        >>> len(deck._ranks)
        13
        >>> len(deck._suits)
        4
        >>> len(deck._cards)
        52
        """
        self._ranks = [str(x) for x in range(2, 11)] + ["J", "K", "Q", "A"]
        self._suits = ["h", "d", "c", "s"]

        self._cards = [
            Card(rank, suit) for rank in self._ranks for suit in self._suits
        ]  # Can also use itertools.product

    def __len__(self) -> int:
        """Returns the length of the card deck

        Returns:
            Length of the card deck

        >>> deck = CardDeck()
        >>> len(deck)
        52
        """
        return len(self._cards)

    def __contains__(self, value: object) -> bool:
        """Checks if deck contains a card

        Args:
            x: Card to check

        Returns:
            True if the deck contains the card

        >>> deck = CardDeck()
        >>> Card('2', 's') in deck
        True
        >>> Card('2', 'a') in deck
        False
        """
        assert isinstance(value, Card), (
            f"value must be of type Card, is type {type(value)}"
        )
        return self._cards.__contains__(value)

    def __getitem__(self, index: Union[int, slice]) -> Union[Card, list[Card]]:
        """Get the card at the specified index

        >>> deck = CardDeck()
        >>> deck[3] == Card('2', 's')
        True
        >>> deck[1:3]
        [Card(rank='2', suit='d'), Card(rank='2', suit='c')]
        """
        return self._cards.__getitem__(index)

    def __iter__(self) -> Iterator[Card]:
        """Creates an iterator object

        >>> deck = CardDeck()
        >>> [x for x in deck[1:3]]
        [Card(rank='2', suit='d'), Card(rank='2', suit='c')]
        """
        return self._cards.__iter__()

    def __repr__(self) -> str:
        """String representation of CardDeck

        >>> deck = CardDeck()
        >>> deck[1:2]
        [Card(rank='2', suit='d')]
        """
        return self._cards.__repr__()
