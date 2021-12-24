from models import *
from helper import *
from sqlconnector import SqlConnector

sql = SqlConnector()

def getNewState(userInput, state):
	for command in state.commands:
		if command.text.lower() in userInput.lower():
			return sql.getState(command.state)

	return State("Sorry, I don't understand '{}'".format(userInput))

def parse(userInput, state):
	try:
		return getNewState(userInput, state)
	except AttributeError:
		print("error")

def command(state):
	userInput = input("Input: ")
	return parse(userInput, state)

def getFirstState():
	state = State("You awake in a dark room. There is an exit North. \nWhat would you like to do?")
	commands = sql.getAvailableCommands(1)

	for c in commands:
		state.addCommand(c)

	return state


state = getFirstState()
printBold(f"{state.text}\n")

while not state.quit:
	state = command(state)
	printBold(f"{state.text}\n")
