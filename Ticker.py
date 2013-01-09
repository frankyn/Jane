#This is the Ticker Class it will be the heart beat of the entire game.
import Events
import pygame 
from pygame.locals import *

class Ticker ( ):
	def __init__ ( self , mediator ):
		self.mediator = mediator
		self.mediator.addObserver ( self )
		self.keepGoing = 1

	def run ( self ):
		clock = pygame.time.Clock()
		elapsed_frames = 0
		while self.keepGoing:
			delay = clock.tick(100)
			if elapsed_frames % 100 == 1:
				pass

			event = Events.TickEvent()
			self.mediator.post(event)
			elapsed_frames += 1

	def notify ( self , event ):
		if isinstance ( event , Events.QuitGameEvent ):
			print "Ticker: Quit Game Event Called"
			#this will stop the while loop from running
			self.keepGoing = False