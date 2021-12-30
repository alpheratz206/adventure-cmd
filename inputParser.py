from commandHelper import *

class InputParser:
	def __generateMultiScore(self, cmd, userInput):
		multiScore = 1000
		for matchText in cmd['MultiMatchText']:
			if matchText in userInput:
				multiScore = min(multiScore, abs(len(matchText) - len(userInput)))
		return multiScore

	def __generateSingleScore(self, cmd, userInput):
		if cmd['MatchText'] in userInput:
			return abs(len(cmd['MatchText']) - len(userInput))
		else:
			return 1000

	def __generateScore(self, cmd, userInput):
		multiScore = 1000
		singleScore = 1000
		try:
			multiScore = self.__generateMultiScore(cmd, userInput)
		except KeyError:
			try:
				singleScore = self.__generateSingleScore(cmd, userInput)
			except KeyError:
				pass

		if singleScore == 1000 and multiScore == 1000:
			score = -1
		else:
			score = min(multiScore, singleScore)

		# print(f"Debug: {cmd['Id']}, score: {score}")

		return score

	def __generateScoreWithEdgeCases(self, cmd, userInput):
		if self.commandHelper.boolCheck(cmd, 'Default'):
			return 1000

		return self.__generateScore(cmd, userInput)

	def assignScores(self, commands, userInput):
		for cmd in commands:
			cmd['Score'] = self.__generateScoreWithEdgeCases(cmd, userInput)

		return list(filter(lambda cmd: cmd['Score'] >= 0, commands))

	def assignScoresAndSort(self, commands, userInput):
		scored = self.assignScores(commands, userInput)
		scored.sort(key = lambda command: command['Score'])
		return scored


	def __init__(self):
		self.commandHelper = CommandHelper()