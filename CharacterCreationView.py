#PyGame
import pygame
from pygame.locals import *

#Events
import Events


#MenuView Class will contain all the necessary logic to render a menu screen inside the PyGame window
class CharacterCreationView ( ):
	def __init__ ( self , mediator , screen ):	
		self.screen = screen
		self.screen_width = self.screen.get_width ( )
		self.screen_height = self.screen.get_height ( )
		self.mediator = mediator
		self.mediator.addObserver ( self )
		self.background_of_creator = pygame.image.load("images/Create.png")
		self.background_of_creator_rect = self.background_of_creator.get_rect ( )
		self.currentCharacter = False 

	def draw ( self ):
		self.screen.blit ( self.background_of_creator, self.background_of_creator_rect )
		if self.currentCharacter != False:
			#self.screen.fill ( pygame.Color ( 0x0C , 0x5A , 0xA6 ) , pygame.Rect ( self.screen_width / 2 - 100 , self.screen_height / 2 - 100 , 200 , 100 ) )
			#font = pygame.font.Font ( None , 36 )
			#text = font.render ( "Character " + str(self.currentCharacter) + " out of 4", 1, ( 0xFF , 0xDE , 0x73 ) )
			#textpos = text.get_rect ( centerx=125 , centery=20 )
			#self.screen.blit ( text , textpos )
			
			font = pygame.font.Font ( None , 36 )
			text = font.render ( "Name: ", 1, ( 0xFF , 0xDE , 0x73 ) )
			textpos = text.get_rect ( centerx=50 , centery=50 )
			self.screen.blit ( text , textpos )

			font = pygame.font.Font ( None , 36 )
			text = font.render ( self.currentCharacter.getName ( ) , 1, ( 0xFF , 0xDE , 0x73 ) )
			textpos = text.get_rect ( centerx=150 , centery=50 )
			self.screen.blit ( text , textpos )

			font = pygame.font.Font ( None , 36 )
			text = font.render ( "Gender: ", 1, ( 0xFF , 0xDE , 0x73 ) )
			textpos = text.get_rect ( centerx=60 , centery=80 )
			self.screen.blit ( text , textpos )

			font = pygame.font.Font ( None , 36 )
			text = font.render ( "Traits: ", 1, ( 0xFF , 0xDE , 0x73 ) )
			textpos = text.get_rect ( centerx=50 , centery=110 )
			self.screen.blit ( text , textpos )

		#Draw MenuView
		pygame.display.flip ( ) 

	def setCharacter ( self , character ):
		self.currentCharacter = character

	def notify ( self , event ):
		if isinstance ( event , Events.TickEvent ):
			self.draw ( )
		elif isinstance ( event , Events.CharacterCreatorSetCharacterEvent ):
			self.setCharacter ( event.character )


