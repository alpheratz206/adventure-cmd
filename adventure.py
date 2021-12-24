from models import *
from helper import *

goodbye = Command('goodbye', State('Have a nice day!', quit = True))

helloState = State('General Kenobi!', [])
hello = Command('hello', helloState)

helloState.addCommand(hello)
helloState.addCommand(goodbye)

def getNewState(userInput, state):
	for command in state.commands:
		if command.text in userInput:
			return command.state

	return State("Sorry, I don't understand '{}'".format(userInput))

def parse(userInput, state):
	try:
		return getNewState(userInput, state)
	except AttributeError:
		print("error")

def command(state):
	userInput = input("Input: ")
	return parse(userInput, state)

state = State("")

state.addCommand(hello)
state.addCommand(goodbye)

while not state.quit:
	state = command(state)
	printBold(state.text)
