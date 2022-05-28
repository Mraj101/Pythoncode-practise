SUITE='H D S C'.split()
RANKS='2 3 4 5 6 7 8 9 10 J Q K A'

# mycards = [(s,r) for s SUITE for r in RANKS]

class Deck:
    def __init__(self):
        print("Creating New Ordered Deck")
        self.allcards=