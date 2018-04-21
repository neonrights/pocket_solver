from multiprocessing import Pool, Queue

from pocketstate import PocketState


class PocketIDDFS:
	axis_names = ['abscissa', 'ordinate', 'applicate']
	move_names = {'c': 'clockwise 90', 'cc': 'counter-clockwise 90', 'f': 'flip 180'}

	def __init__(self, state, min_depth=0, max_depth=11):
		self.init_state = PocketState(state)
		self.start_depth = min_depth
		self.max_depth = max_depth

	def run(self, workers=1):
		assert workers > 0
		if workers == 1:
			for iter_depth in range(self.start_depth, self.max_depth+1):
				print "depth %d" % iter_depth
				solution_path = self._dfs(self.init_state, None, iter_depth, [])
				if solution_path:
					return solution_path
		else:
			pool = Pool(workers)
			# set up Queue which workers will pop jobs off from
			# set up Queue which workers return to
			# parent will continuously check queue until path is found, then terminate all workers
			for iter_depth in range(self.start_depth, self.max_depth+1):
				print "depth %d" % iter_depth
				# split up search space


	def _dfs(self, state, last_axis, depth, path):
		if depth == 0: # if goal state is reached, return path to goal
			return path if state.is_goal() else None
		
		for axis in xrange(3):
			if axis != last_axis:
				for move in ['c', 'cc', 'f']:
					child = state.operators[axis](move)
					path.append("%s %s" % (self.axis_names[axis], self.move_names[move]))
					solution = self._dfs(child, axis, depth - 1, path)
					if solution:
						return path

					path.pop()

		return None # goal state not reached


def test_iddfs():
	print "Testing iddfs on simple states..."

	solved_state = PocketState([[['w', 'w'],
								 ['w', 'w']],
								[['y', 'y'],
								 ['y', 'y']],
								[['b', 'b'],
								 ['b', 'b']],
								[['g', 'g'],
								 ['g', 'g']],
								[['o', 'o'],
								 ['o', 'o']],
								[['r', 'r'],
								 ['r', 'r']]])
	single_rotation = solved_state._abscissa('c')
	double_rotation = single_rotation._ordinate('cc')
	triple_rotation = double_rotation._applicate('f')

	single_solver = PocketIDDFS(single_rotation.state)
	double_solver = PocketIDDFS(double_rotation.state)
	triple_solver = PocketIDDFS(triple_rotation.state)
	assert single_solver.run() == ['abscissa counter-clockwise 90']
	assert double_solver.run() == ['ordinate clockwise 90', 'abscissa counter-clockwise 90']
	assert triple_solver.run() == ['applicate flip 180', 'ordinate clockwise 90', 'abscissa counter-clockwise 90']

	print "iddfs unit tests passed"


if __name__ == '__main__':
	test_iddfs()