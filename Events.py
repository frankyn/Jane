#List of events that can be observered by a class.

class TickEvent ( ):
	def __init__ ( self ):
		self.name = "Tick Event"

class NewGameEvent ( ):
	def __init__ ( self ):
		self.name = "New Game Event"

class QuitGameEvent ( ):
	def __init__ ( self ):
		self.name = "Quit Game Event"

class NewCharacterEvent ( ):
	def __init__ ( self , character ):
		self.name = "New Character Event"
		self.character = character

class DeadCharacterEvent ( ):
	def __init__ ( self , character ):
		self.name = "Dead Character Event"
		self.character = character

class NewGroupEvent ( ):
	def __init__ ( self , group ):
		self.name = "New Character Group Event"
		self.group = group

class CharacterUpdateEvent ( ):
	def __init__ ( self , id , update ):
		self.name = "Character Update Event"
		self.id = id
		self.update = update

class FinishedCharactersEvent ( ):
	def __init__ ( self ):
		self.name = "Finished Characters Event"

class ClusterCharacterAdded ( ):
	def __init__ ( self ):
		self.name = "Cluster Done Event"

class ClusterWeatherEvent ( ):
	def __init__ ( self , weather ):
		self.name = "Cluster Weather Event"
		self.weather = weather

