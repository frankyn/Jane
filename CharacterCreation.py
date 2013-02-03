#This is something like a controller for creating Characters for the game
#It should work with how you 

# Character Counter 1 - 4
# Names: Jane , Janet , Juan , Jenifer
# 

#PyGame
import pygame
from pygame.locals import *

#Events
import Events

#Models
from Character import Character

class CharacterCreation ( ):
	STARTING = 0
	SELECTING = 1
	DONE = 2
	def __init__  ( self , mediator ):
		self.mediator = mediator
		self.mediator.addObserver ( self )
		self.state = CharacterCreation.STARTING
		self.count = 0
		self.characters = []


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
		
	def characterUpdate ( self ):
		pass

	def characterSetup ( self ):
		tmpCharacter = Character ( self.mediator )
		tmpCharacter.setName ( "Juan" )
		self.characters.append ( tmpCharacter )

		tmpCharacter = Character ( self.mediator )
		tmpCharacter.setName ( "Jane" )
		self.characters.append ( tmpCharacter )

		tmpCharacter = Character ( self.mediator )
		tmpCharacter.setName ( "Janet" )
		self.characters.append ( tmpCharacter )

		tmpCharacter = Character ( self.mediator )
		tmpCharacter.setName ( "Jenifer" )
		self.characters.append ( tmpCharacter )

		self.mediator.post ( Events.CharacterCreatorSetCharacterEvent ( 1 , self.characters[0] ) )

	def notify ( self , event ):
		if isinstance ( event , Events.TickEvent ):
			if self.state == CharacterCreation.STARTING:
				self.state = CharacterCreation.SELECTING
				self.characterSetup ( )
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