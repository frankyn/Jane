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

	def draw ( self ):
		self.screen.fill ( pygame.Color ( 0x0C , 0x5A , 0xA6 ) , pygame.Rect ( self.screen_width / 2 - 100 , self.screen_height / 2 - 100 , 200 , 100 ) )
		font = pygame.font.Font ( None , 68 )
		text = font.render ( "Jane - Month 1", 1, ( 0xA6 , 0x36 , 0x00 ) )
		textpos = text.get_rect ( centerx=self.screen_width / 2 , centery=50)
		self.screen.blit ( text , textpos )

		font = pygame.font.Font ( None , 36 )
		text = font.render ( "Character", 1, ( 0xFF , 0xDE , 0x73 ) )
		textpos = text.get_rect ( centerx=self.screen_width / 2 , centery=self.screen_height / 2 - 50 )
		self.screen.blit ( text , textpos )
		
		#Draw MenuView
		pygame.display.flip ( ) 

	def notify ( self , event ):
		if isinstance ( event , Events.TickEvent ):
			self.draw ( )


