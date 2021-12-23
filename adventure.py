import models

hello = models.Transition('hello', models.State('General Kenobi!'))
goodbye = models.Transition('goodbye', models.State('Have a nice day!', quit = True))

def command():
	userInput = input("Input: ")
	return parse(userInput)

def parse(userInput):
	if 'Hello' in userInput:
		return models.State('General Kenobi!')
	if 'Goodbye' in userInput:
		return goodbye.state

	return models.State("Sorry, I don't understand '{}'".format(userInput))

def main():
	state = models.State("")

	while not state.quit:
		state = command()
		print(state.text)

main()
