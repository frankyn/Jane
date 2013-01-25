#This is something like a controller for creating Characters for the game
#It should work with how you 

#PyGame
import pygame
from pygame.locals import *

#Events
import Events

#Models
from Character import Character

class CharacterCreation ( ):
	SELECTING = 0
	DONE = 1
	def __init__  ( self , mediator ):
		self.mediator = mediator
		self.mediator.addObserver ( self )
		self.state = CharacterCreation.SELECTING
		self.count = 0


	def completedSelection ( self ):
		print ("Selection completed.")
		self.state = CharacterCreation.DONE
		#Once Finished Creating Characters send event so we can proceed to the next step.
		ev = Events.FinishedCharactersEvent ( )
		self.mediator.post ( ev )
		#Once Finished we should remove CharacterCreation from Mediator
		self.mediator.removeObserver ( self )

	def dummyCharacters ( self ):
		print ("Dummy Characters")
		#A dummy character created
		#This can be switched out with user control of some kind
		#This works because the Jade Runner is waiting for CharacterCreationCompletedEvent ()
		
		#Send out Event that we are making a new Group called 0
		#This will be the main group on screen.
		ev = Events.NewGroupEvent ( 0 )
		self.mediator.post ( ev )
		#Dummy Character
		char = Character ( self.mediator )
		char.setName ( "Name" + str(self.count) )
		print (char.getName ( ))
		ev = Events.NewCharacterEvent ( char )
		self.mediator.post ( ev )
		self.mediator.post ( Events.ClusterAddCharacterEvent ( 0 , char.getName ( ) ) )
		self.count += 1
		#Dummy Character
		char = Character ( self.mediator )
		char.setName ( "Name" + str(self.count) )
		print (char.getName ( ))
		ev = Events.NewCharacterEvent ( char )
		self.mediator.post ( ev )
		self.mediator.post ( Events.ClusterAddCharacterEvent ( 0 , char.getName ( ) ) )
		self.count += 1
		self.completedSelection ( )
		

	def notify ( self , event ):
		if isinstance ( event , Events.TickEvent ):
			if self.state == CharacterCreation.SELECTING:
				pass
		else:
			if isinstance ( event , list ) and self.state == CharacterCreation.SELECTING:
				for ev in event: 
					if ev.type == MOUSEBUTTONDOWN:
						position = pygame.mouse.get_pos ( )
						#New Game Button
						if ( position [ 0 ] > 300 and position [ 1 ] > 200 and position [ 0 ] < 500 and position [ 1 ] < 300 ):
							self.dummyCharacters ( )

	def __str__ ( self ):
		pass