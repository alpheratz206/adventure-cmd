import json
import os

class JsonConnector:
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

		self.states.sort(reverse=False, key = lambda state: state['Id'])
		self.commands.sort(reverse=True, key = lambda command: command['Id'])