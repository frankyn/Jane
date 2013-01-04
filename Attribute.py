#Attributes should be appended to models not used directly.

class Attribute ( ):
	def __init__ ( self, name ):
		self.name = name
		self.values = {}

	def getName ( self ):
		return self.name

	def setValue ( self, name, value ):
		self.values [ name ] = value

	def getValue ( self, name ):
		return self.values [ name ]

	def __str__ ( self ):
		print "Attribute:"
		print "--Name: " + self.name
		for hashKey in self.values:
			print "--" + str ( hashKey ) + ": " + str ( self.values [ hashKey ] )

  		return ""

