#Attributes should be appended to models not used directly.

class Attribute ( ):
	def __init__ ( self, name ):
		self.name = name
		self.value = False

	def getName ( self ):
		return self.name

	def setValue ( self , value ):
		self.value = value

	def getValue ( self ):
		return self.value

	def __str__ ( self ):
		print ("Attribute:")
		print ("--Name: " + self.name)
		for hashKey in self.values: #self.values does not seem to be defined?
			print ("--" + str ( hashKey ) + ": " + str ( self.values [ hashKey ] ))

  		#return ""

