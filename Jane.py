#Message Mediator Class
from EventMediator import EventMediator
from JaneRunner import JaneRunner
from Ticker import Ticker

#Main Runner
def main ( ):
	print "Jane - Month one"				
	evtRouter = EventMediator ( )
	game = JaneRunner ( evtRouter )
	tick = Ticker ( evtRouter )

	tick.run ( )

	return

#Main Runner
main ( )