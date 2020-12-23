# This is a test for the Global_Functions package

###IMPORTS###
from time import time
import sys
import os

PACKAGE_PARENT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from Global_Functions import shoe as shoe 


###CLASS CARD###
"""
test_card = shoe.Card(12,hearts)
print(test_card.black_suit())
test_card.show()
"""
###CLASS DECK###

"""
deck = shoe.Deck()
deck.show()
"""
###CLASS SHOE###
# Function shuffle and show
"""
test_shoe = shoe.Shoe(4)
test_shoe.shuffle()
test_shoe.show()
print(len(test_shoe.cards))
"""
# Function stack vs create a stacked_cards attribute
"""
test_shoe = shoe.Shoe(4)
test_shoe.shuffle()
print(test_shoe.stack_cards())
print(len(test_shoe.stack_cards()))
print(len(test_shoe.stack_cards()[0]))
test_shoe = shoe.Shoe(8)
test_shoe.shuffle()
start_time = time()
print(test_shoe.stack_cards())
elapsed_time = time() - start_time
print("Elapsed time: %0.10f seconds." % elapsed_time)
"""
# Function use_card
"""
test_shoe = shoe.Shoe(8)
test_shoe.shuffle()
print(test_shoe.use_card().show())
print(test_shoe.stack_cards())
"""
