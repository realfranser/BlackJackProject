# This is the test for the simulator script
import sys
import os
import time

PACKAGE_PARENT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from Sidebets import simulator as sim
###ATRIBUTES###
iterations = 10000
decks = 8
end_game = 0.66
money = 10000
min_bet = 5
plot=True
###TESTS###
# Tests for function pairs_sim
# sim.pairs_sim(iterations, decks, end_game, money, min_bet, plot)
start_time = time.time()
print(sim.simple_pairs_sim(iterations, decks, end_game, money, min_bet))
print("--- %s seconds ---" % (time.time() - start_time))

