import json

class JsonConnector:
	def __loadFile(self, fileName):
		file = open(f'data/{fileName}.json')
		return json.load(file)[fileName]

	def __loadStates(self):
		self.states = self.__loadFile('states')

	def __loadCommands(self):
		self.commands = self.__loadFile('commands')

	def __init__(self):
		self.__loadStates()
		self.__loadCommands()