from jsonconnector import *
from inputParser import *
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

		try:
			direction = command['Direction']
			try:
				newStateID = self.state[direction]
				self.__changeState(list(filter(lambda state: state['Id'] == newStateID, self.data.states))[0])
			except KeyError:
				printBold("You cannot go that way.")
		except KeyError:
			pass

	def __getCommandFromInput(self, userInput):
		scoredCommands = self.inputParser.assignScoresAndSort(self.data.commands, userInput)

		# for cmd in listMatchingCommands:
		# 	print(f"{cmd['Id']}, score: {cmd['Score']}")

		return scoredCommands[0]


	def play(self):
		while not self.quit:
			userInput = input("Input: ")

			command = self.__getCommandFromInput(userInput)
			self.__processCommand(command)


	def __init__(self):
		self.data = JsonConnector()
		self.inputParser = InputParser()
		self.__changeState(self.data.states[0])
		self.commands = self.data.commands


Adventure().play()