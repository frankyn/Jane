#Weather example 
#
class Weather ():
	def __init__ ( self ):
		#init all effect this Weather will have on a cluster/group
		#make it easy to add effects and get
		self.attributes = {}

	def addAttribute ( self , attribute ):
		self.attributes [ attribute.getName ( ) ] = attribute

	def getAttribute ( self , name ):
		return self.attributes [ name ]

	def __str__ ( self ):
		output = ""
		return output