# This is a tester for the file pairs.py
###IMPORTS###
import sys
import os

PACKAGE_PARENT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from Sidebets import pairs as pairs
from Global_Functions import shoe as shoe

###TESTS###
# Test calculate_probability
test_shoe = shoe.Shoe(8)
print(pairs.calculate_probability(test_shoe))
"""
test_shoe = shoe.Shoe(8)
stacked_shoe = test_shoe.stacked_shoe
total_cards = len(test_shoe.cards)
print(range(len(stacked_shoe)))       
print(range(len(stacked_shoe[0])))
for _ in range(1000):
    test_shoe = shoe.Shoe(8)
    test_shoe.shuffle()
    print(pairs.calculate_probability(test_shoe))
card1 = shoe.Card(10,1)
card2 = shoe.Card(10,1)
card3 = shoe.Card(10,2)
card4 = shoe.Card(10,3)
card5 = shoe.Card(9,3)
print(pairs.bet(1, card1, card2)) # Expected -> 25
print(pairs.bet(1, card1, card4)) # 12
print(pairs.bet(1, card1, card3)) # 6
print(pairs.bet(1, card1, card5)) # -1

"""

