###DESCRIPTION###
"""
This is the cript that contains the functions needed to calculate the perfect strategy for
the sidebet 21 + 3
Guide:
    - Three flush -> 100
    - Straight flush -> 40
    - Three of a kind -> 30
    - Stright -> 10
    - Flush -> 5

"""

###IMPORTS###

import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from Global_Functions import shoe as shoe 

###FUNCTIONS###
# Given a deck, returns a coeficient representing the expected result of betting for 21 + 3
def calculate_probability(shoe):
    # Atributes
    coef = 0
    stacked_shoe = shoe.stacked_shoe
    total_cards = len(shoe.cards)
    # v-> value, s-> suit
    for v in range(len(stacked_shoe)):       
        for s in range(len(stacked_shoe[0])):
            three_flush = calculate_three_flush(stacked_shoe, v, s)
            straight_flush = calculate_straight_flush(stacked_shoe, v, s)
            three_kind = calculate_three_kind(stacked_shoe, v, s)
            # Straight and flush left

def calculate_three_flush(stacked_shoe, v, s):
    this_card = stacked_shoe[v][s]
    return this_card*max(0,this_card-1)*max(0,this_card-2)*100

def calculate_stright_flush(stacked_shoe, v, s):
    count = 0
    this_card = stacked_shoe[v][s]
    if v == 0:
        count += this_card*stacked_shoe[1][s]*stacked_shoe[2][s]
        count += this_card*stacked_shoe[11][s]*stacked_shoe[12][s]
    elif v == 1:
        count += this_card*stacked_shoe[0][s]*stacked_shoe[2][s]
        count += this_card*stacked_shoe[2][s]*stacked_shoe[3][s]
    elif v == 12:
        count += this_card*stacked_shoe[10][s]*stacked_shoe[11][s]
        count += this_card*stacked_shoe[11][s]*stacked_shoe[0][s]
    else:    
        # For cards other than Ace, Two or King
        count += this_card*stacked_shoe[v-2][s]*stacked_shoe[v-1][s]*40
        count += this_card*stacked_shoe[v-1][s]*stacked_shoe[v+1][s]*40
        count += this_card*stacked_shoe[v+1][s]*stacked_shoe[v+2][s]*40
    return count

def calculate_three_kind(stacked_shoe, v, s):
        this_card = stacked_shoe[v][s]
        same_value = sum_shoe[v]
        return this_card*(same_value-1)*(same_value-1)


