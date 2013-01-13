#Menu Class this will tell how the game should start off
#New Game - Clean Character Creation
#Continue - Continues a saved entry

#Events
import Events
#Controllers
from CharacterCreation import CharacterCreation

class Menu ( ):
	TURNEDON = 0
	TURNEDOFF = 1
	def __init__ ( self , mediator ):
		self.state = Menu.TURNEDON
		self.mediator = mediator
		self.mediator.addObserver ( self )

	def newGame ( self ):
		self.state = Menu.TURNEDOFF
 		self.characterCreation = CharacterCreation ( self.mediator )
		self.mediator.post ( Events.NewGameEvent ( ) )

	def dummyController ( self ):
		print ( "New Game" )
		self.newGame ( )

	def notify ( self , event ):
		if isinstance ( event , Events.TickEvent ):
			if self.state == Menu.TURNEDON:
				self.dummyController ( )