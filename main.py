import sys
import argparse

from iddfs import PocketIDDFS

# parse arguments, state or file containing states, number of workers, max depth to search to
test_state = [[['r', 'w'],
			   ['y', 'g']],
			  [['o', 'g'],
			   ['b', 'o']],
			  [['r', 'y'],
			   ['y', 'b']],
			  [['b', 'r'],
			   ['g', 'w']],
			  [['y', 'b'],
			   ['w', 'o']],
			  [['r', 'g'],
			   ['w', 'o']]]

solver = PocketIDDFS(test_state)
print solver.run()