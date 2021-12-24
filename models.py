class State:
	def __init__(self, text, commands = [], quit = False):
		self.text = text
		self.commands = commands
		self.quit = quit

	def addCommand(self, command):
		self.commands.append(command)

class Command:
	def __init__(self, text, state):
		self.text = text
		self.state = state