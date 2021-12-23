
class AdventureState:
	quit = False
	text = ""

	def __init__(self, text, quit = False):
		self.text = text
		self.quit = quit

class 

def command():
	userInput = input("Input: ")
	return parse(userInput)

def parse(userInput):
	if 'Hello' in userInput:
		return AdventureState('General Kenobi!')
	if 'Goodbye' in userInput:
		return AdventureState('Have a nice day!', True)

	return AdventureState("Sorry, I don't understand '{}'".format(userInput))

def main():
	state = AdventureState("")

	while not state.quit:
		state = command()
		print(state.text)

main()
