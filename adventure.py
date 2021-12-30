from jsonconnector import *
from inputParser import *
from helper import *
from commandHelper import *

class Adventure:
	quit = False

	def __introduceState(self):
		printBold(f"{self.state['Description']}\n")

	def __changeState(self, state):
		self.state = state
		self.__introduceState()

	def __processCommand(self, command, arguments = []):
		try:
			printBold(f"{command['ReplyText']}\n")
		except KeyError:
			pass

		try:
			direction = command['Direction']
			try:
				newStateID = self.state[direction]
				self.__changeState(list(filter(lambda state: state['Id'] == newStateID, self.data.states))[0])
			except KeyError:
				printBold("You cannot go that way.\n")
		except KeyError:
			pass

		try:
			action = command['UniqueAction']
			if action.lower() == "repeat":
				self.__introduceState()
			elif action.lower() == "quit":
				self.quit = True
		except KeyError:
			pass

	def __getAvailableCommands(self):
		default = list(filter(lambda cmd: self.commandHelper.boolCheck(cmd, 'Default'), self.data.commands))
		always = list(filter(lambda cmd: self.commandHelper.boolCheck(cmd, 'Always'), self.data.commands))

		try:
			whiteListIDs = self.state['CommandWhite']
		except KeyError:
			whiteListIDs = []

		whitelisted = list(filter(lambda cmd: cmd['Id'] in whiteListIDs, self.data.commands))

		return default + always + whitelisted

 
	def __getCommandFromInput(self, userInput):
		scoredCommands = self.inputParser.assignScoresAndSort(self.__getAvailableCommands(), userInput)
		return scoredCommands[0]


	def play(self):
		while not self.quit:
			userInput = input("Input: ")

			command = self.__getCommandFromInput(userInput)
			self.__processCommand(command)


	def __init__(self):
		self.data = JsonConnector()
		self.commandHelper = CommandHelper()
		self.inputParser = InputParser()
		self.__changeState(self.data.states[0])
		self.commands = self.data.commands


Adventure().play()