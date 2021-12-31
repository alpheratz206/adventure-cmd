from jsonconnector import *
from inputParser import *
from helper import *
from commandHelper import *

class Adventure:
	quit = False

	def __printBoldWithLineBreak(self, text):
		printBold(f"{text}\n")

	def __introduceState(self):
		self.__printBoldWithLineBreak(self.state['Description'])

	def __changeState(self, state):
		self.state = state
		self.__introduceState()

	def __isItemGiven(self, item):
		try:
			return item['Given']
		except KeyError:
			return False

	def __processCommand(self, command, arguments = []):
		try:
			self.__printBoldWithLineBreak(command['ReplyText'])
		except KeyError:
			pass

		try:
			direction = command['Direction']
			try:
				newStateID = self.state[direction]
				self.__changeState(list(filter(lambda state: state['Id'] == newStateID, self.data.states))[0])
			except KeyError:
				self.__printBoldWithLineBreak("You cannot go that way.")
		except KeyError:
			pass

		try:
			grantedItemID = command['GrantItem']
			grantedItem = list(filter(lambda item: item['Id'] == grantedItemID, self.data.items))[0]
			grantedItem['Given'] = True
		except KeyError:
			pass

		try:
			action = command['UniqueAction']
			if action.lower() == "repeat":
				self.__introduceState()
			elif action.lower() == "quit":
				self.quit = True
			elif action.lower() == "inventory":
				allItems = list(filter(lambda item: self.__isItemGiven(item), self.data.items))
				if len(allItems) > 0:
					# itemDescriptions = ', '.join(map(lambda item: item['Description'], allItems))
					printBold("Inventory:")
					for item in allItems:
						printBold(item['Description'])
					print(" ")
				else:
					self.__printBoldWithLineBreak("You have no items.")
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