import copy
import numpy as np

from multiprocessing import Pool

"""
0Front	1Back	2Top	3Bottom	4Left	5Right
1 2		5 6		9  10	13 14	17 18	21 22
3 4		7 8		11 12	15 16	19 20	23 24

r w b g y o
"""

state = np.array([[['w', 'w'],
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
				   ['r', 'r']]])

class PocketState:
	def __init__(self, state):
		assert state.shape == (6,2,2)
		self.state = np.array(state)

	def clone(self):
		return copy.deepcopy(self)

	# rotate on x axis, horizontal from front
	def abscissa_operator(self, action):
		if action == 'c': # clockwise 90 degrees
			# adjust front, top, back, and bottom
			temp_front = self.state[0,:,1]
			
			# front
			self.state[0,:,1] = self.state[4,:,1]
			
			# bottom
			self.state[3,0,1] = self.state[1,1,0]
			self.state[3,1,1] = self.state[1,0,0]

			# back
			self.state[1,0,0] = self.state[2,1,1]
			self.state[1,1,0] = self.state[2,0,1]

			# top
			self.state[2,:,1] = temp_front

			# rotate right
			temp_right = self.state[5]
			self.state[5,0] = temp_right[:,0]
			self.state[5,1] = temp_right[:,1]
		elif action == 'cc': # counter-clockwise 90 degrees
			# adjust front, top, back, and bottom
			temp_front = self.state[0,:,1]
			
			# front
			self.state[0,:,1] = self.state[3,:,1]
			
			# top
			self.state[2,0,1] = self.state[1,1,0]
			self.state[2,1,1] = self.state[1,0,0]

			# back
			self.state[1,0,0] = self.state[3,1,1]
			self.state[1,1,0] = self.state[3,0,1]

			# bottom
			self.state[3,:,1] = temp_front

			# rotate right
			temp_right = self.state[5]
			self.state[5,0] = temp_right[:,1]
			self.state[5,1] = temp_right[:,0]
		elif action == 'f': # flip 180 degrees
			# adjust front, top, back, and bottom
			temp_front = self.state[0,:,1]
			temp_top = self.state[2,:,1]
			
			# front
			
			# back

			# top

			# bottom

			# rotate right
			temp_right = self.state[5]
			self.state[5,0] = temp_right[1]
			self.state[5,1] = temp_right[0]
		else:
			raise ValueError('Invalid action')

	# rotate on y axis, towards/away from front
	def ordinate_operator(state, action):
		if action == 'c': # clockwise 90 degrees
			pass
		elif action == 'cc': # counter-clockwise 90 degrees
			pass
		elif action == 'f': # flip 180 degrees
			pass
		else:
			raise ValueError('Invalid action')

	# rotate on z axis, vertical from front
	def applicate_operator(state, action):
		if action == 'c': # clockwise 90 degrees
			pass
		elif action == 'cc': # counter-clockwise 90 degrees
			pass
		elif action == 'f': # flip 180 degrees
			pass
		else:
			raise ValueError('Invalid action')


def test_state():
	pass


if __name__ == '__main__':
	test_state()