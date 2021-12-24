import mariadb
from models import *

class SqlConnector:
	def __init__(self):
		self.conn = mariadb.connect(
    	host="localhost",
    	database="Adventure")

		self.cur = self.conn.cursor() 

	def getAvailableCommands(self, stateID):
		self.cur.execute(
			f"SELECT " \
			f"	C.CommandID," \
			f"	C.Text,"  \
			f"	C.StateID "  \
			f"FROM Command C " \
			f"JOIN AvailableCommand AC ON AC.CommandID = C.CommandID " \
			f"WHERE AC.StateID = {stateID}; "
		)

		commands = []
		for commandID, text, stateID in self.cur:
			commands.append(Command(text, stateID))

		return commands

	def getState(self, stateID):
		self.cur.execute(
			f"SELECT " \
			f"	S.StateID," \
			f"	S.Description,"  \
			f"	S.Quit "  \
			f"FROM State S " \
			f"WHERE S.StateID = {stateID}; "
		)

		for StateID, Description, Quit in self.cur:
			return State(
				Description,
				self.getAvailableCommands(stateID),
				Quit)

	
