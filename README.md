# Tarot Card Deck

A minimal command-line tarot card application that draws cards from a traditional 78-card deck using random number generation.

This is intended to provide true RNG to an LLM agent and provides no interpretations by itself.

## Usage

```bash
python tarot.py <number_of_cards>
```

### Examples

Draw a single card:

```bash
$ python tarot.py 1
The Hermit reversed
```

Draw three cards (classic past-present-future spread):

```bash
$ python tarot.py 3
Two of Pentacles reversed, The Empress, Five of Swords reversed
```

## The Deck

The application uses a complete tarot deck:

- 22 Major Arcana cards
- 56 Minor Arcana cards (Cups, Swords, Wands, Pentacles)

Each card has a 50/50 chance of appearing upright or reversed. Cards are drawn without replacement.

## Installation

No dependencies required - uses only Python standard library.

Make the script executable (optional):

```bash
chmod +x tarot.py
./tarot.py 3
```

Create a system-wide command (optional):

```bash
ln -s $(pwd)/tarot.py /usr/local/bin/tarot
tarot 3
```
