#Manage Several Characters and maintain certain variables

#Cluster Model manages Character Models so we don't interact with them directly but we need to create the Cluster Model during model that should be the only time we interact with the Character Models

class Cluster ( ):
	#initiliaze cluster attributes
	def __init__ ( self ):
		self.characters = [] #List
		self.attributes = {} #Hash Map

	#add a Character Model to characters list
	def addCharacter ( self, characterModel ):
  		self.characters.insert ( 0, characterModel )

  	#add an Attribute to attributes Hash Map
  	def setAttribute ( self, attributeData ):
  		self.attributes [ attributeData.getName ( ) ] = attributeData

  	#get an Attribute based on Hash Map Key = Attribute Name
  	def getAttribute ( self, attributeName ):
  		return self.attributes [ attributeName ]

  	#Print out cluster information for attributes and characters
  	def __str__ ( self ):
  		print "Cluster"
  		
  		print "--Attributes"
  		for hashKey in self.attributes:
  			print self.attributes [ hashKey ]
  		
  		print "--Characters"
  		for character in self.characters:
  			print character
  		return ""

