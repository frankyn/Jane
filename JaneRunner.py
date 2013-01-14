#This is where all the objects are stored so we can create a new game from here.
#The idea is to start events from a single location and let the EventMediator manage all events posted.

#Models
from Character import Character
from Cluster import Cluster
from Attribute import Attribute
#Controllers
from Menu import Menu
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
	def __init__ ( self , mediator ):
		self.state = JaneRunner.PREPARING
		self.characters = []
		self.mediator = mediator
		self.mediator.addObserver ( self )
		self.killerID = 0
	
	#Preparation is done and start is called to start running the game
	def start ( self ):
		print ("JadeRunner - Started")
		self.state = JaneRunner.RUNNING

	#Create a Menu Controller to start the type of game
	def prepare ( self ):
		self.state = JaneRunner.WAITING
		self.menu = Menu ( self.mediator )

	#When a Character is created we add them into main cluster
	def addCharacter ( self , character ):
		#Group 0 is the main screen cluster
		if character.group == 0:
			self.characters.append ( character )

	#Weather the cluster with a few a few attacks
	def weather ( self ):
		#Create Weather Class as a container to what will happen during time
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
		health.setValue ( -1 )
		time.addAttribute ( health )

		#Post as a Cluster Weather Event
		ev = Events.ClusterWeatherEvent ( time )
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
		elif isinstance ( event , Events.GameTimeEvent ):
			if self.state == JaneRunner.RUNNING:
				self.dummyMethod_killACharacter ( )
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

