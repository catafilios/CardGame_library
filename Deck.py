# -*- coding=utf-8 -*-

values = ( 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K' )
families = ( 'H', 'S', 'D', 'C' )

class Card:
    def __init__(self,value,family):
        self.value = value
        self.family = family

class Deck:
    def __init__(self):
        self.cards = []
        for family in families:
            for value in values:
                self.cards.append( Card( value,family ) )

    def shuffle:





