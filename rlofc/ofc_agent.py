import numpy as np
from deuces import Card

street_to_row = {
    0: 'front',
    1: 'mid',
    2: 'back'
}

class OFCAgent(object):
    """An OFC decision maker."""

    def place_new_card(self, card, board):
        """Return 0, 1, 2 for front, mid, back."""
        pass


class OFCRandomAgent(OFCAgent):
    """Place cards at random!"""

    def place_new_card(self, card, board):
        roll = np.random.uniform(0, 1, 3) * board.get_free_streets()
        street = np.argmax(roll)
        return street


class OFCRLAgent(OFCAgent):
    """Insert neural network here."""
    pass

class OFCHumanAgent(OFCAgent):
    """Insert neural network here."""
    def __init__(self, name):
        self.name = name

    def place_new_card(self, card, board):
        free_streets = board.get_free_street_indices()
        if len(free_streets) == 0:
            return -1

        print 'Current card:', 
        Card.print_pretty_card(Card.new(card))

        print("Available streets:")
        for street in free_streets:
            print '%s: %s' % (street, street_to_row[street])

        print "%s, please enter the street (number) to play your card." % (self.name)
        street = input()
        while street not in free_streets:
            print("Please enter a valid street: " + str(free_streets))
            street = input()
        print('')
        return street

class OFCComputerAgent(OFCAgent):
    """Insert computer player with some strategy here."""
    pass