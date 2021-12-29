class CommandHelper:
	def isDefault(self, cmd):
		try:
			isDefault = cmd['Default']
			return isDefault
		except KeyError:
			return False