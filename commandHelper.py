class CommandHelper:
	def boolCheck(self, cmd, prop):
		try:
			isBool = cmd[prop]
			return isBool
		except KeyError:
			return False

	def tryParseAsMovement(self, cmd, success):
		try:
			direction = cmd['Direction']
			try:
				success(direction)
				# newStateID = state[direction]
				# changeState(list(filter(lambda state: state['Id'] == newStateID, self.data.states))[0])
			except KeyError:
				self.__printBoldWithLineBreak("You cannot go that way.")
		except KeyError:
			pass

	def __init__(self, data):
		self.data = data