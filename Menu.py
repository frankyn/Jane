#Menu Class this will tell how the game should start off
#New Game - Clean Character Creation
#Continue - Continues a saved entry

#PyGame
import pygame
from pygame.locals import *

#Events
import Events
#Controllers

class Menu ( ):
	TURNEDON = 0
	TURNEDOFF = 1
	def __init__ ( self , mediator ):
		self.state = Menu.TURNEDON
		self.mediator = mediator
		self.mediator.addObserver ( self )

	def newGame ( self ):
		self.state = Menu.TURNEDOFF
		self.mediator.post ( Events.NewGameEvent ( ) )

	def dummyController ( self ):
		print ( "New Game" )
		self.newGame ( )

	def notify ( self , event ):
		if isinstance ( event , Events.TickEvent ):
			if self.state == Menu.TURNEDON:
				pass
		else:
			if isinstance ( event , list ) and self.state == Menu.TURNEDON:
				for ev in event: 
					if ev.type == MOUSEBUTTONDOWN:
						position = pygame.mouse.get_pos ( )
						#New Game Button
						if ( position [ 0 ] > 300 and position [ 1 ] > 200 and position [ 0 ] < 500 and position [ 1 ] < 300 ):
							self.newGame ( )
