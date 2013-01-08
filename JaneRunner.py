#This is where all the objects are stored so we can create a new game from here.
#The idea is to start events from a single location and let the EventMediator manage all events posted.

#Models
from Character import Character
from Cluster import Cluster
from Attribute import Attribute

#Events
import Events

class JaneRunner ( ):
	PREPARING = 0
	RUNNING = 1

	def __init__ ( self , mediator):
		self.state = JaneRunner.PREPARING
		self.mediator = mediator;
		self.mediator.addObserver ( self )
	
	def start ( self ):
		print "JadeRunner - Started"
		self.state = JaneRunner.RUNNING
		ev = Events.QuitGameEvent ( )
		self.mediator.post ( ev )

	def notify ( self , event ):
		if isinstance ( event, Events.TickEvent):
			if self.state == JaneRunner.PREPARING:
				self.start ( )
