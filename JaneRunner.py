#This is where all the objects are stored so we can create a new game from here.
#The idea is to start events from a single location and let the EventMediator manage all events posted.

#PyGame
import os, sys
import pygame
from pygame.locals import *

#Models
from Character import Character
from Cluster import Cluster
from Attribute import Attribute

#Controllers
from Menu import Menu
from CharacterCreation import CharacterCreation
from Game import Game

#Views
from MenuView import MenuView
from CharacterCreationView import CharacterCreationView
from GameView import GameView

#Events
import Events

#Effects
from Weather import Weather

#Main Container for Jade
class JaneRunner ( ):
	PREPARING = 0
	WAITING = 1
	RUNNING = 2

	#Pass in mediator 
	#JadeRunner will add in itself
	def __init__ ( self , mediator , width=800 , height=600 ):
		#PyGame INIT
		pygame.init ( )

		#Set the window Size
		self.width = width
		self.height = height
		
		#Create the Window
		pygame.display.set_caption ( "Jane - Month 1" ) 
		self.window = pygame.display.set_mode ( [ self.width , self.height ] )
		self.screen = pygame.display.get_surface ( ) 

		#JadeRunner INIT
		self.state = JaneRunner.PREPARING
		self.controller = False
		self.view = False
		self.characters = []
		self.mediator = mediator
		self.mediator.addObserver ( self )
		self.killerID = 0
	
	#Preparation is done and start is called to start running the game
	def start ( self ):
		print ("JadeRunner - Started")
		self.state = JaneRunner.RUNNING
		self.clearCV ( )
		self.controller = Game ( self.mediator )
		self.view = GameView ( self.mediator , self.screen )

	#Remove observers controller and view from current mediator
	def clearCV ( self ):
		if self.controller:
			self.mediator.removeObserver ( self.controller )
		if self.view:
			self.mediator.removeObserver ( self.view )

	#Create a Menu Controller to start the type of game
	def prepare ( self ):
		self.state = JaneRunner.WAITING
		self.clearCV ( )
		self.controller = Menu ( self.mediator )
		self.view = MenuView ( self.mediator , self.screen )

	#Called when a new game is started
	def newGame ( self ):
		self.clearCV ( )
 		self.controller = CharacterCreation ( self.mediator )
 		self.view = CharacterCreationView ( self.mediator , self.screen )

	#When a Character is created we add them into main cluster
	def addCharacter ( self , character ):
		self.characters.append ( character )

	#Weather the cluster with a few a few attacks
	def weather ( self ):
		#Create Weather Class as a container to what will happen during time
		#THIS NEEDS TO BE SET TO PRACTICAL DEGENERATIVE PARAMETERS
		time = Weather ( )
		#Add Attributes this Weather will help
		morale = Attribute ( "Morale" )
		morale.setValue ( -1 )
		time.addAttribute ( morale )

		hygiene = Attribute ( "Hygiene" )
		hygiene.setValue ( -1 )
		time.addAttribute ( hygiene )

		hunger = Attribute ( "Hunger" )
		hunger.setValue ( -1 )
		time.addAttribute ( hunger )

		fatigue = Attribute ( "Fatigue" )
		fatigue.setValue ( -1 )
		time.addAttribute ( fatigue )

		health = Attribute ( "Health" )
		health.setValue ( -100 )
		time.addAttribute ( health )

		#Post as a Cluster Weather Event
		ev = Events.ClusterWeatherEvent ( 0 , time )
		self.mediator.post ( ev )

	def dummyMethod_killACharacter ( self ):
		degenerate = Weather ( )
		health = Attribute ( "Health" )
		health.setValue ( -1 )
		degenerate.addAttribute ( health )
		ev = Events.CharacterUpdateEvent ( self.characters[self.killerID].getName ( ) , degenerate )
		self.mediator.post ( ev )	

	#Notify JaneRunner of an event posted
	def notify ( self , event ):
		if isinstance ( event , Events.TickEvent ):
			if self.state == JaneRunner.PREPARING:
				self.prepare ( )
			else:
				self.mediator.post ( pygame.event.get() )
		elif isinstance ( event , Events.NewGameEvent ):
			if self.state == JaneRunner.WAITING:
				self.newGame ( )
		elif isinstance ( event , Events.GameTimeEvent ):
			if self.state == JaneRunner.RUNNING:
				#self.weather ( )
				pass
		elif isinstance ( event , Events.ClusterCharacterAdded ):
			if self.state == JaneRunner.WAITING:
				pass
		elif isinstance ( event , Events.NewCharacterEvent ):
			if self.state == JaneRunner.WAITING:
				self.addCharacter ( event.character )
		elif isinstance ( event , Events.FinishedCharactersEvent ):
			if self.state == JaneRunner.WAITING:
				self.start ( )
		elif isinstance ( event , Events.CharacterDeadEvent ):
			if self.state == JaneRunner.RUNNING:
				self.killerID += 1
		elif isinstance ( event , Events.ClusterDeadEvent ):
			if self.state == JaneRunner.RUNNING and event.group == 0:
				#Add a character count check to make sure all characters are dead.
				#kill game if all characters dead
				print ('All Characters Dead.')
				ev = Events.QuitGameEvent ( )
				self.mediator.post ( ev )
		else:
			if isinstance ( event , list ):
				for ev in event: 
				    if ev.type == QUIT: 
				        sys.exit(0) 
