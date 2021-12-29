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

		try:
			direction = command['Direction']
			try:
				newStateID = self.state[direction]
				self.__changeState(list(filter(lambda state: state['Id'] == newStateID, self.data.states))[0])
			except KeyError:
				printBold("You cannot go that way.")
		except KeyError:
			pass

	def __matchRank(self, cmd, userInput):
		try:
			isDefault = cmd['Default']
			if isDefault:
				return 1000
		except KeyError:
			pass

		multiScore = 1000
		singleScore = 1000
		try:
			for matchText in cmd['MultiMatchText']:
				if matchText in userInput:
					multiScore = min(multiScore, abs(len(matchText) - len(userInput)))
		except KeyError:
			try:
				if cmd['MatchText'] in userInput:
					singleScore = abs(len(cmd['MatchText']) - len(userInput))
			except KeyError:
				pass

		if singleScore == 1000 and multiScore == 1000:
			score = -1
		else:
			score = min(multiScore, singleScore)

		return score

	def __getCommandFromInput(self, userInput):
		commands = self.data.commands

		for cmd in commands:
			cmd['MatchRank'] = self.__matchRank(cmd, userInput)

		matchingCommands = filter(lambda command: command['MatchRank'] >= 0, commands)
		listMatchingCommands = list(matchingCommands)

		listMatchingCommands.sort(key = lambda command: command['MatchRank'])

		# for cmd in listMatchingCommands:
		# 	print(f"{cmd['Id']}, score: {cmd['MatchRank']}")

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