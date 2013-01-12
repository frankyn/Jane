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
		print ("Dummy Characters")
		self.state = CharacterCreation.DONE
		#A dummy character created
		#This can be switched out with user control of some kind
		#This works because the Jade Runner is waiting for CharacterCreationCompletedEvent ()
		
		#Send out Event that we are making a new Group called 0
		#This will be the main group on screen.
		ev = Events.NewGroupEvent ( 0 )
		self.mediator.post ( ev )
		#Dummy Character
		char = Character ( self.mediator , 0 )
		char.setName ( "Name" + str(self.count) )
		print (char.getName ( ))
		ev = Events.NewCharacterEvent ( char )
		self.mediator.post ( ev )
		self.count += 1
		#Dummy Character
		char = Character ( self.mediator , 0 )
		char.setName ( "Name" + str(self.count) )
		print (char.getName ( ))
		ev = Events.NewCharacterEvent ( char )
		self.mediator.post ( ev )
		self.count += 1
		#Once Finished Creating Characters send event so we can proceed to the next step.
		ev = Events.FinishedCharactersEvent ( )
		self.mediator.post ( ev )
		#Once Finished we should remove CharacterCreation from Mediator
		self.mediator.removeObserver ( self )

	def notify ( self , event ):
		if isinstance ( event , Events.NewGameEvent ):
			if self.state == CharacterCreation.PREPARING:
				self.dummyCharacters ( )

	def __str__ ( self ):
		pass