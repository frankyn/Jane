#Models
from Character import Character
from Cluster import Cluster
from Attribute import Attribute

#Main Runner
def main ( ):
	print "Jane - Month one"
	
	print "Creating a Cluster Model"
	testGroup = Cluster ( )
	
	print "Adding Position Attribute"
	positionAttribute = Attribute ( "position" )
	#Add Values with setValue ( id , value ) they can be extracted with getValue ( id )
	positionAttribute.setValue ( "x" , 0 )
	positionAttribute.setValue ( "y" , 0 )
	testGroup.setAttribute ( positionAttribute )

	print "Creating three Character Models"
	for x in range ( 0 , 3 ):
		tempCharacter = Character ( ) 
    	testGroup.addCharacter ( tempCharacter )
	
	print "Printing out Cluster Model"
	print testGroup

	return

#Main Runner
main ( )