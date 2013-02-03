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

class GameTimeEvent ( ):
	def __init__ ( self ):
		self.name = "GameTimeEvent"

class NewCharacterEvent ( ):
	def __init__ ( self , character ):
		self.name = "New Character Event"
		self.character = character

class CharacterDeadEvent ( ):
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

class ClusterAddCharacterEvent ( ):
	def __init__ ( self , group , characterID ):
		self.name = "Cluster Add Character Event"
		self.group = group
		self.characterID = characterID

class ClusterRemoveCharacterEvent ( ):
	def __init__ ( self , characterID ):
		self.name = "Cluster Remove Character Event"
		self.characterID = characterID

class ClusterCharacterAdded ( ):
	def __init__ ( self ):
		self.name = "Cluster Done Event"

class ClusterWeatherEvent ( ):
	def __init__ ( self , group , weather ):
		self.name = "Cluster Weather Event"
		self.group = group
		self.weather = weather

class ClusterDeadEvent ( ):
	def __init__ ( self , group ):
		self.name = "Cluster Dead Event"
		self.group = group

class CharacterCreatorSetCharacterEvent ( ):
	def __init__ ( self , id , character ):
		self.name = "Character Creator Set Character"
		self.id = id
		self.character = character
