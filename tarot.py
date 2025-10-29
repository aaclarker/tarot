#!/usr/bin/env python3
import sys
import random

TAROT_DECK = [
    # Major Arcana
    "The Fool",
    "The Magician",
    "The High Priestess",
    "The Empress",
    "The Emperor",
    "The Hierophant",
    "The Lovers",
    "The Chariot",
    "Strength",
    "The Hermit",
    "Wheel of Fortune",
    "Justice",
    "The Hanged Man",
    "Death",
    "Temperance",
    "The Devil",
    "The Tower",
    "The Star",
    "The Moon",
    "The Sun",
    "Judgement",
    "The World",
    # Cups Suit
    "Ace of Cups",
    "Two of Cups",
    "Three of Cups",
    "Four of Cups",
    "Five of Cups",
    "Six of Cups",
    "Seven of Cups",
    "Eight of Cups",
    "Nine of Cups",
    "Ten of Cups",
    "Page of Cups",
    "Knight of Cups",
    "Queen of Cups",
    "King of Cups",
    # Swords Suit
    "Ace of Swords",
    "Two of Swords",
    "Three of Swords",
    "Four of Swords",
    "Five of Swords",
    "Six of Swords",
    "Seven of Swords",
    "Eight of Swords",
    "Nine of Swords",
    "Ten of Swords",
    "Page of Swords",
    "Knight of Swords",
    "Queen of Swords",
    "King of Swords",
    # Wands Suit
    "Ace of Wands",
    "Two of Wands",
    "Three of Wands",
    "Four of Wands",
    "Five of Wands",
    "Six of Wands",
    "Seven of Wands",
    "Eight of Wands",
    "Nine of Wands",
    "Ten of Wands",
    "Page of Wands",
    "Knight of Wands",
    "Queen of Wands",
    "King of Wands",
    # Pentacles Suit
    "Ace of Pentacles",
    "Two of Pentacles",
    "Three of Pentacles",
    "Four of Pentacles",
    "Five of Pentacles",
    "Six of Pentacles",
    "Seven of Pentacles",
    "Eight of Pentacles",
    "Nine of Pentacles",
    "Ten of Pentacles",
    "Page of Pentacles",
    "Knight of Pentacles",
    "Queen of Pentacles",
    "King of Pentacles",
]


def draw_cards(num_cards):
    """Draw cards from the tarot deck using true RNG."""
    if num_cards < 1 or num_cards > len(TAROT_DECK):
        print(f"Error: Please request between 1 and {len(TAROT_DECK)} cards.")
        sys.exit(1)

    # Use SystemRandom for cryptographically strong random numbers
    rng = random.SystemRandom()

    # Select cards without replacement
    selected_cards = rng.sample(TAROT_DECK, num_cards)

    # Determine orientation (upright or reversed) for each card
    results = []
    for card in selected_cards:
        if rng.choice([True, False]):  # 50/50 chance
            results.append(card)
        else:
            results.append(f"{card} reversed")

    return results


def main():
    if len(sys.argv) != 2:
        print("Usage: tarot <number_of_cards>")
        sys.exit(1)

    try:
        num_cards = int(sys.argv[1])
    except ValueError:
        print("Error: Please provide a valid number.")
        sys.exit(1)

    cards = draw_cards(num_cards)
    print(", ".join(cards))


if __name__ == "__main__":
    main()
