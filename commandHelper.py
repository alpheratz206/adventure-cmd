class CommandHelper:
	def boolCheck(self, cmd, prop):
		try:
			isBool = cmd[prop]
			return isBool
		except KeyError:
			return False