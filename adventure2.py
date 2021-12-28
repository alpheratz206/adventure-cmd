from jsonconnector import *
from helper import *

class Adventure:
	quit = False

	def __processCommand(self, command):
		try:
			self.quit = command['Quit']
		except:
			pass

		try:
			printBold(command['ReplyText'])
		except:
			pass

	def __filterCommands(self, command, userInput):
		try:
			for matchText in command['MatchText']:
				if(userInput in matchText):
					return True
		except:
			pass

		try:
			return userInput in command['MatchText']
		except:
			return False

	def __getCommandFromInput(self, userInput):
		matchingCommands = filter(lambda command: self.__filterCommands(command, userInput), self.data.commands)
		return list(matchingCommands)[0]


	def play(self):
		while not self.quit:
			printBold(f"{self.state['Description']}\n")
			userInput = input("Input: ")

			try:
				command = self.__getCommandFromInput(userInput)
				self.__processCommand(command)
			except:
				pass


	def __init__(self):
		self.data = JsonConnector()
		self.state = self.data.states[0]
		self.commands = self.data.commands # all commands available


Adventure().play()