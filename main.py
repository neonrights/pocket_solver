import sys
import argparse

from iddfs import PocketIDDFS


test_state = [[['w', 'w'],
			   ['g', 'w']],
			  [['y', 'y'],
			   ['y', 'g']],
			  [['b', 'b'],
			   ['b', 'b']],
			  [['o', 'g'],
			   ['o', 'g']],
			  [['o', 'o'],
			   ['y', 'w']],
			  [['r', 'r'],
			   ['r', 'r']]]

solver = PocketIDDFS(test_state)
print solver.run()