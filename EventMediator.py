#This will be the heart of the whole game. 
#Different Event Messages will be handled here and direct calls to objects will be affected by a message not direct access.



class EventMediator ( ):
	def __init__ ( self ):
		self.observers = []

	def post ( self , event ):
		for observer in self.observers:
			observer.notify ( event )

	def addObserver ( self , observer ):
		self.observers.insert ( 0 , observer )

	def removeObserver ( self , observer ):
		i = 0
		for o in self.observers:
			if o == observer:
				self.observers.pop ( i )
			i+=1
		
		
