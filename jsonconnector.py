import json
import os

class JsonConnector:
	def __unique(self, stuff):
		seen = set()
		return not any(ele in seen or seen.add(ele) for ele in stuff)

	def __validateStates(self):
		ids = map(lambda state: state['Id'], self.states)
		if not self.__unique(ids):
			raise Exception("State IDs are not unique!")

	def __validateCommands(self):
		ids = map(lambda cmd: cmd['Id'], self.commands)
		if not self.__unique(ids):
			raise Exception("Command IDs are not unique!")


	def __loadFile(self, fileName):
		file = open(f'data/{fileName}')
		fileData = json.load(file)

		try:
			self.states = self.states + fileData['states']
		except KeyError:
			pass

		try:
			self.commands = self.commands + fileData['commands']
		except KeyError:
			pass

	def __loadAllFiles(self): 
		directory = './data'
		for fileName in os.listdir(directory):
			if fileName == '.DS_Store':
				continue
			self.__loadFile(fileName)

	def __init__(self):
		self.states = []
		self.commands = []

		self.__loadAllFiles()

		self.__validateStates()
		self.__validateCommands()

		self.states.sort(key = lambda state: state['Id'])
		self.commands.sort(key = lambda command: command['Id'])