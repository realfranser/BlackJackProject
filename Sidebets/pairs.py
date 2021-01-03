import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from Global_Functions import shoe as shoe 
import math
import numpy as np

###FUNCTIONS###
# Given a deck, returns a coeficient representing the expected result of betting for pairs
def calculate_probability(shoe):
    count = 0
    stacked_shoe = shoe.stacked_shoe
    total_cards = len(shoe.cards)

    for v in range(len(stacked_shoe)):       
        for s in range(len(stacked_shoe[0])):
            # Chance of finding card v,s
            # card_chance = stacked_shoe[v][s]/total_cards
            card_count = stacked_shoe[v][s]

            # Total gains on same value and suit 
            # same_card = card_chance* max(0, stacked_shoe[v][s]-1)/(total_cards-1) *25
            same_card = card_count* max(0, card_count-1)* 25

            # Total gains on same value and color
            # same_color = card_chance* (stacked_shoe[v][(s+2)%4])/(total_cards-1) *12
            same_color = card_count* stacked_shoe[v][(s+2)%4] *12

            # Total gains on same value different color
            # same_value = card_chance* (stacked_shoe[v][(s+1)%4]/(total_cards-1) + stacked_shoe[v][(s+3)%4]/(total_cards-1)) *6
            same_value = card_count* (stacked_shoe[v][(s+1)%4] + stacked_shoe[v][(s+3)%4]) *6

            # Different card
            # diff_card = card_chance* (total_cards-sum(stacked_shoe[v])) / (total_cards-1)
            diff_card = card_count* (total_cards-sum(stacked_shoe[v]))
            # Adding up all results...
            count += (same_card + same_color + same_value - diff_card)

    return count/total_cards/ (total_cards-1)
    
def bet(money, card1, card2):
    multiplier = 0
    if card1.value == card2.value:
        if card1.suit == card2.suit:
            multiplier = 25
        elif (card1.suit % 2) == (card2.suit % 2):
            multiplier = 12
        else:
            multiplier = 6
    else:
        multiplier = -1
    return money*multiplier 
