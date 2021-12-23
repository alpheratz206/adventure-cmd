
class State:
	def __init__(self, text, transitions = [], quit = False):
		self.text = text
		self.transitions = transitions
		self.quit = quit

	def addTransition(transition):
		self.transitions.append(transition)

class Transition:
	def __init__(self, text, state):
		self.text = text
		self.state = state