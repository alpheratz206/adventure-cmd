from jsonconnector import *
from helper import *

class Adventure:
	quit = False

	def __changeState(self, state):
		self.state = state
		printBold(f"{self.state['Description']}\n")

	def __processCommand(self, command):
		try:
			self.quit = command['Quit']
		except KeyError:
			pass

		try:
			printBold(command['ReplyText'])
		except KeyError:
			pass

	def __filterCommands(self, command, userInput):
		try:
			for matchText in command['MatchText']:
				if matchText in userInput:
					return True
		except KeyError:
			pass

		try:
			return command['MatchText'] in userInput
		except KeyError:
			pass

		try:
			default = command['Default']
			if default:
				return True
		except KeyError:
			pass

	def __matchRank(self, cmd):
		try:
			matchLength = len(cmd['MatchText'])
		except KeyError:
			return -1

		try:
			isDefault

	def __getCommandFromInput(self, userInput):
		matchingCommands = filter(lambda command: self.__filterCommands(command, userInput), self.data.commands)
		listMatchingCommands = list(matchingCommands)

		listMatchingCommands.sort(reverse=True, key = lambda command: self.__matchRank(command))

		# try:
			
		# 	for cmd in listMatchingCommands:
		# 		print(cmd['MatchText'])
		# except KeyError:
		# 	pass

		return listMatchingCommands[0]


	def play(self):
		while not self.quit:
			userInput = input("Input: ")

			command = self.__getCommandFromInput(userInput)
			self.__processCommand(command)


	def __init__(self):
		self.data = JsonConnector()
		self.__changeState(self.data.states[0])
		self.commands = self.data.commands # all commands available


Adventure().play()