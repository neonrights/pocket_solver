import argparse

from iddfs import PocketIDDFS

parser = argparse.ArgumentParser(description='Pocket Cube solver.')
parser.add_argument('-s', '--state', nargs=24, help='starting state of pocket cube', required=True)
parser.add_argument('-w', '--workers', type=int, help='number of workers for multiprocessing, default single process')
args = parser.parse_args()


"""
Representation

Front	Back	Top		Bottom	Left	Right
1 2		5 6		9  10	13 14	17 18	21 22
3 4		7 8		11 12	15 16	19 20	23 24

Colors
r(ed) w(hite) b(lue) g(reen) y(ellow) o(range)
"""


solver = PocketIDDFS(args.state)
solution = solver.run(args.workers)
print solution if solution else 'failed to find solution, impossible to solve'
