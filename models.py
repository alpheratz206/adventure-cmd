class State:
	reply = ""

	def __init__(self, text, commands = [], quit = False):
		self.text = text
		self.commands = commands
		self.quit = quit

	def addCommand(self, command):
		self.commands.append(command)

	def getPrintText(self):
		if self.reply == "":
			return self.text
		else:
			return self.reply

class Command:
	def __init__(self, text, state, commandType, replyText, quit = False):
		self.text = text
		self.state = state
		self.commandType = commandType
		self.replyText = replyText
		self.quit = quit