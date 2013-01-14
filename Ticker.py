#This is the Ticker Class it will be the heart beat of the entire game.
import Events
import pygame 
from pygame.locals import *

class Ticker ( ):
	def __init__ ( self , mediator ):
		self.mediator = mediator
		self.mediator.addObserver ( self )
		self.keepGoing = 1
		self.elapsedTime = 0

	def run ( self ):
		clock = pygame.time.Clock()
		elapsed_frames = 0
		while self.keepGoing:
			self.elapsedTime += clock.tick(100)
			#Second Passed Post GameTimeEvent ( ) 
			#1 Second = 5 min game time
			if self.elapsedTime >= 1000:
				self.elapsedTime = 0
				self.mediator.post ( Events.GameTimeEvent ( ) )
			event = Events.TickEvent()
			self.mediator.post(event)
			elapsed_frames += 1

	def notify ( self , event ):
		if isinstance ( event , Events.QuitGameEvent ):
			print ("Ticker: Quit Game Event Called")
			#this will stop the while loop from running
			self.keepGoing = False
