#Menu Class this will tell how the game should start off
#New Game - Clean Character Creation
#Continue - Continues a saved entry

#PyGame
import pygame
from pygame.locals import *

#Events
import Events
#Controllers

class Game ( ):
	TURNEDON = 0
	TURNEDOFF = 1
	def __init__ ( self , mediator ):
		self.state = Game.TURNEDON
		self.mediator = mediator
		self.mediator.addObserver ( self )

	def dummyController ( self ):
		print ( "Something" )

	def notify ( self , event ):
		if isinstance ( event , Events.TickEvent ):
			if self.state == Game.TURNEDON:
				pass
		else:
			if isinstance ( event , list ) and self.state == Game.TURNEDON:
				for ev in event: 
					if ev.type == MOUSEBUTTONDOWN:
						position = pygame.mouse.get_pos ( )
						#New Game Button
						if ( position [ 0 ] > 300 and position [ 1 ] > 200 and position [ 0 ] < 500 and position [ 1 ] < 300 ):
							self.dummyController ( )
