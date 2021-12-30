from jsonconnector import *

data = JsonConnector()

states = data.states
states.sort(reverse=True, key = lambda state: state['Id'])
print(f"highest state ID: {states[0]['Id']}")

commands = data.commands
commands.sort(reverse=True, key = lambda cmd: cmd['Id'])
print(f"highest command ID: {commands[0]['Id']}")
