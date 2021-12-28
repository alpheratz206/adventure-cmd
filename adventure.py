from models import *
from helper import *
from adventureEnum import *
from sqlconnector import SqlConnector

sql = SqlConnector()

def getNewState(userInput, state):
	for command in state.commands:
		if command.text.lower() in userInput.lower():
			if command.commandType == CommandType['BASIC']:
				return sql.getState(command.state)
			elif command.commandType == CommandType['REPLY']:
				state.reply = command.replyText
				state.quit = command.quit
				return state
			elif command.commandType == CommandType['MOVE']:
				state.reply = 'An error occurred'
				return state

	state.reply = ""
	return state

def parse(userInput, state):
	try:
		return getNewState(userInput, state)
	except AttributeError:
		print("error")

def command(state):
	userInput = input("Input: ")
	return parse(userInput, state)

def getFirstState():
	return sql.getState(3)



state = getFirstState()
printBold(f"{state.text}\n")

while not state.quit:
	state = command(state)
	printBold(f"{state.getPrintText()}\n")
