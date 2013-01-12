#This is where all the objects are stored so we can create a new game from here.
#The idea is to start events from a single location and let the EventMediator manage all events posted.

#Models
from Character import Character
from Cluster import Cluster
from Attribute import Attribute

#Events
import Events

#Effects
from Weather import Weather

#Main Container for Jade
class JaneRunner ( ):
	PREPARING = 0
	RUNNING = 1

	#Pass in mediator 
	#JadeRunner will add in itself
	def __init__ ( self , mediator ):
		self.state = JaneRunner.PREPARING
		self.mediator = mediator;
		self.mediator.addObserver ( self )
		self.charactersCount = 3
		self.charactersCreated = 0
	
	#Preparation is done and start is called to start running the game
	def start ( self ):
		print ("JadeRunner - Started")
		self.state = JaneRunner.RUNNING

	#Prepare a cluster of characters and send them to a Cluster Observer
	def prepare ( self ):
		char = Character ( )
		ev = Events.NewCharacterEvent ( char )
		self.mediator.post ( ev )
		self.mediator.post ( ev )
		self.mediator.post ( ev )

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


	#Notify JaneRunner of an event posted
	def notify ( self , event ):
		if isinstance ( event , Events.TickEvent ):
			if self.state == JaneRunner.PREPARING:
				self.prepare ( )
			elif self.state == JaneRunner.RUNNING:
				self.weather ( )

		elif isinstance ( event , Events.ClusterCharacterAdded ):
			self.charactersCreated += 1
			if self.state == JaneRunner.PREPARING and self.charactersCreated == self.charactersCount:
				self.start ( )

