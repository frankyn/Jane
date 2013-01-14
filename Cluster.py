#Manage Several Characters and maintain certain variables

#Cluster Model manages Character Models so we don't interact with them directly but we need to create the Cluster Model during model that should be the only time we interact with the Character Models
import EventMediator
import Events

class Cluster ( ):
  #initiliaze cluster attributes
  def __init__ ( self , mediator ):
    self.mediator = mediator
    self.mediator.addObserver ( self )
    self.groups = {} #List
    self.attributes = {} #Hash Map

	#add a Group to groups hashmap
  def addGroup ( self, group ):
    self.groups[group] = []

  #increase group size
  def increaseGroup ( self , group , characterID ):
    self.groups[group].append ( characterID )

  #decrease group size
  def decreaseGroup ( self , characterID ):
    parentGroup = ''
    for group in self.groups:
      i=0
      for ID in self.groups[group]:
        if characterID == ID:
          parentGroup = group
          self.groups[group].pop ( i )
          break
        i+=1
      if not parentGroup=='':
        break 
    if len ( self.groups[parentGroup] ) <= 0:
      #All Characters Dead
      self.mediator.post ( Events.ClusterDeadEvent ( parentGroup ) )

	#add an Attribute to attributes Hash Map
  def setAttribute ( self, attributeData ):
    self.attributes [ attributeData.getName ( ) ] = attributeData

	#get an Attribute based on Hash Map Key = Attribute Name
  def getAttribute ( self, attributeName ):
    return self.attributes [ attributeName ]

  #notify method to be called when an observable event happens
  def notify ( self , event ):
    if isinstance ( event , Events.NewGroupEvent ):
      self.addGroup ( event.group )

    elif isinstance ( event , Events.ClusterAddCharacterEvent ):
      self.increaseGroup ( event.group , event.characterID )

    elif isinstance ( event , Events.ClusterRemoveCharacterEvent ):
      self.decreaseGroup ( event.characterID )

    elif isinstance ( event , Events.ClusterWeatherEvent ):
      for characterID in self.groups[event.group]:
        self.mediator.post ( Events.CharacterUpdateEvent ( characterID , event.weather ) )
        
	#Print out cluster information for attributes and characters
  def __str__ ( self ):
    print ("Cluster")
    print ("--Attributes")
    for hashKey in self.attributes:
      print (self.attributes [ hashKey ])
		
    print ("--Characters")
    for character in self.characters:
      print (character)
    return ""

