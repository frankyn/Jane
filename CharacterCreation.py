#This is something like a controller for creating Characters for the game
#It should work with how you 

#Events
import Events

#Models
from Character import Character

class CharacterCreation ( ):
	PREPARING = 0
	DONE = 1
	def __init__  ( self , mediator ):
		self.mediator = mediator
		self.mediator.addObserver ( self )
		self.state = CharacterCreation.PREPARING
		self.count = 0

	def dummyCharacters ( self ):
		print "Dummy Characters"
		self.state = CharacterCreation.DONE
		#A dummy character created
		#This can be switched out with user control of some kind
		#This works because the Jade Runner is waiting for CharacterCreationCompletedEvent ()
		
		ev = Events.NewGroupEvent ( 0 )
		self.mediator.post ( ev )
		
		char = Character ( self.mediator , 0 )
		char.setName ( "Name" + str(self.count) )
		ev = Events.NewCharacterEvent ( char )
		self.mediator.post ( ev )
		self.count += 1

		ev = Events.FinishedCharactersEvent ( )
		self.mediator.post ( ev )

	def notify ( self , event ):
		if isinstance ( event , Events.NewGameEvent ):
			if self.state == CharacterCreation.PREPARING:
				self.dummyCharacters ( )

	def __str__ ( self ):
		pass