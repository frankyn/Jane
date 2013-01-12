#Message Mediator Class
from EventMediator import EventMediator
from JaneRunner import JaneRunner
from Ticker import Ticker
from Cluster import Cluster
from CharacterCreation import CharacterCreation
#Main Runner
def main ( ):
	print ("Jane - Month one")

	evtRouter = EventMediator ( )
	game = JaneRunner ( evtRouter )
	tick = Ticker ( evtRouter )
	group = Cluster ( evtRouter )
	creation = CharacterCreation ( evtRouter )
	
	tick.run ( )

	return

#Main Runner
main ( )
