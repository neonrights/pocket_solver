import copy
import numpy as np

from numpy.testing import assert_array_equal

"""
Representation

0Front	1Back	2Top	3Bottom	4Left	5Right
1 2		5 6		9  10	13 14	17 18	21 22
3 4		7 8		11 12	15 16	19 20	23 24

r w b g y o
"""

class PocketState:
	def __init__(self, state):
		self.state = np.array(state)
		assert self.state.shape == (6,2,2)
		self.operators = [self._abscissa, self._ordinate, self._applicate]

	# rotate on x axis, horizontal from front
	def _abscissa(self, action):
		child = copy.deepcopy(self)
		if action == 'c': # clockwise 90 degrees
			# front
			child.state[0,:,1] = self.state[3,:,1]
			
			# bottom
			child.state[3,0,1] = self.state[1,1,0]
			child.state[3,1,1] = self.state[1,0,0]

			# back
			child.state[1,0,0] = self.state[2,1,1]
			child.state[1,1,0] = self.state[2,0,1]

			# top
			child.state[2,:,1] = self.state[0,:,1]

			# rotate right
			child.state[5,0,0] = self.state[5,1,0]
			child.state[5,0,1] = self.state[5,0,0]
			child.state[5,1,0] = self.state[5,1,1]
			child.state[5,1,1] = self.state[5,0,1]
		elif action == 'cc': # counter-clockwise 90 degrees
			# front
			child.state[0,:,1] = self.state[2,:,1]
			
			# top
			child.state[2,0,1] = self.state[1,1,0]
			child.state[2,1,1] = self.state[1,0,0]

			# back
			child.state[1,0,0] = self.state[3,1,1]
			child.state[1,1,0] = self.state[3,0,1]

			# bottom
			child.state[3,:,1] = self.state[0,:,1]

			# rotate right
			child.state[5,0] = self.state[5,:,1]
			child.state[5,1] = self.state[5,:,0]
		elif action == 'f': # flip 180 degrees
			# front
			child.state[0,0,1] = self.state[1,1,0]
			child.state[0,1,1] = self.state[1,0,0]

			# back
			child.state[1,0,0] = self.state[0,1,1]
			child.state[1,1,0] = self.state[0,0,1]

			# top
			child.state[2,:,1] = self.state[3,:,1]

			# bottom
			child.state[3,:,1] = self.state[2,:,1]

			# rotate right
			child.state[5,0,0] = self.state[5,1,1]
			child.state[5,0,1] = self.state[5,1,0]
			child.state[5,1,0] = self.state[5,0,1]
			child.state[5,1,1] = self.state[5,0,0]
		else:
			raise ValueError('Invalid action')

		return child

	# rotate on y axis, towards/away from front
	def _ordinate(self, action):
		child = copy.deepcopy(self)
		if action == 'c': # clockwise 90 degrees
			# rotate front
			child.state[0,0,0] = self.state[0,1,0]
			child.state[0,0,1] = self.state[0,0,0]
			child.state[0,1,0] = self.state[0,1,1]
			child.state[0,1,1] = self.state[0,0,1]

			# top
			child.state[2,1,0] = self.state[4,1,1]
			child.state[2,1,1] = self.state[4,0,1]

			# left
			child.state[4,:,1] = self.state[3,1]

			# bottom
			child.state[3,0] = self.state[5,:,0]

			# right
			child.state[5,:,0] = self.state[2,1]
		elif action == 'cc': # counter-clockwise 90 degrees
			# rotate front
			child.state[0,0] = self.state[0,:,1]
			child.state[0,1] = self.state[0,:,0]
			
			# top
			child.state[2,1] = self.state[5,:,0]

			# right
			child.state[5,:,0] = self.state[3,0]

			# bottom
			child.state[3,0] = self.state[4,:,1]

			# left
			child.state[4,0,1] = self.state[2,1,1]
			child.state[4,1,1] = self.state[2,1,0]
		elif action == 'f': # flip 180 degrees
			# rotate front
			child.state[0,0,0] = self.state[0,1,1]
			child.state[0,0,1] = self.state[0,1,0]
			child.state[0,1,0] = self.state[0,0,1]
			child.state[0,1,1] = self.state[0,0,0]

			# top
			child.state[2,1,0] = self.state[3,0,1]
			child.state[2,1,1] = self.state[3,0,0]

			# bottom
			child.state[3,0,0] = self.state[2,1,1]
			child.state[3,0,1] = self.state[2,1,0]

			# left
			child.state[4,0,1] = self.state[5,1,0]
			child.state[4,1,1] = self.state[5,0,0]

			# right
			child.state[5,0,0] = self.state[4,1,1]
			child.state[5,1,0] = self.state[4,0,1]
		else:
			raise ValueError('Invalid action')

		return child

	# rotate on z axis, vertical from front
	def _applicate(self, action):
		child = copy.deepcopy(self)
		if action == 'c': # clockwise 90 degrees
			# front
			child.state[0,0] = self.state[5,0]

			# right
			child.state[5,0] = self.state[1,0]

			# back
			child.state[1,0] = self.state[4,0]

			# left
			child.state[4,0] = self.state[0,0]

			# rotate top
			child.state[2,0,0] = self.state[2,1,0]
			child.state[2,0,1] = self.state[2,0,0]
			child.state[2,1,0] = self.state[2,1,1]
			child.state[2,1,1] = self.state[2,0,1]
		elif action == 'cc': # counter-clockwise 90 degrees
			# front
			child.state[0,0] = self.state[4,0]

			# left
			child.state[4,0] = self.state[1,0]

			# back
			child.state[1,0] = self.state[5,0]

			# right
			child.state[5,0] = self.state[0,0]

			# rotate top
			child.state[2,0] = self.state[2,:,1]
			child.state[2,1] = self.state[2,:,0]
		elif action == 'f': # flip 180 degrees
			# front
			child.state[0,0] = self.state[1,0]

			# back
			child.state[1,0] = self.state[0,0]

			# left
			child.state[4,0] = self.state[5,0]

			# right
			child.state[5,0] = self.state[4,0]

			# rotate top
			child.state[2,0,0] = self.state[2,1,1]
			child.state[2,0,1] = self.state[2,1,0]
			child.state[2,1,0] = self.state[2,0,1]
			child.state[2,1,1] = self.state[2,0,0]
		else:
			raise ValueError('Invalid action')

		return child

	# return true if goal state has been reached
	def is_goal(self):
		return (self.state[:,0,0].reshape(6,1,1) == self.state).all()


def test_operators():
	print "Testing operators..."
	test_state = np.array([[['w', 'w'],
						    ['g', 'w']],
						   [['y', 'y'],
						    ['y', 'g']],
						   [['b', 'r'],
						    ['b', 'b']],
						   [['o', 'g'],
						    ['o', 'g']],
						   [['o', 'o'],
						    ['y', 'w']],
						   [['r', 'b'],
						    ['r', 'r']]])

	pocket = PocketState(test_state)
	names = ['abscissa', 'ordinate', 'applicate']
	for i in range(3):
		child_pocket = pocket.operators[i]('c')
		grandchild_pocket = child_pocket.operators[i]('cc')
		assert_array_equal(grandchild_pocket.state, test_state,
				'%s quarter turn\n%s' % (names[i], grandchild_pocket.state))

		child_pocket = pocket.operators[i]('f')
		grandchild_pocket = child_pocket.operators[i]('f')
		assert_array_equal(grandchild_pocket.state, test_state,
				'%s flip\n%s' % (names[i], grandchild_pocket.state))

	print "Operator unit tests passed"

def test_goal():
	print "Testing goal checker..."
	test_state1 = [[['w', 'w'],
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
				    ['r', 'r']]]
	test_state2 = [[['w', 'w'],
				    ['g', 'w']],
				   [['y', 'y'],
				    ['y', 'g']],
				   [['b', 'r'],
				    ['b', 'b']],
				   [['o', 'g'],
				    ['o', 'g']],
				   [['o', 'o'],
				    ['y', 'w']],
				   [['r', 'b'],
				    ['r', 'r']]]


	assert PocketState(test_state1).is_goal()
	assert not PocketState(test_state2).is_goal()
	print "Goal checker unit tests passed"


if __name__ == '__main__':
	test_operators()
	test_goal()
