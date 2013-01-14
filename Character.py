#2013 Mindfuck Labs Thinga-muh-boober
#Events
import Events

class Character ( ):
    def __init__ ( self , mediator , group ):
        self.mediator = mediator
        self.mediator.addObserver ( self )
        self.group = group
        #Information
        self.name = "Blank"
        self.gender = "Both"

        #Flags
        self.status = "ALIVE"
        
        #Resources
        self.max_health = 100
        self.health = self.max_health

        self.max_morale = 100
        self.morale = self.max_morale

        self.max_hygiene = 100
        self.hygiene = self.max_hygiene

        self.max_fatigue = 100
        self.fatigue = self.max_fatigue

        self.max_hunger = 100
        self.hunger = self.max_hunger

        #Skills
        self.fight = 10
        self.sneak = 10
        self.medical = 10
        self.spot = 10
        self.speed = 10

    def notify ( self , event ):
        if not self.isAlive ( ):
            return
        if isinstance ( event , Events.CharacterUpdateEvent ):
            if event.id == self.getName ( ):
                if event.update.getAttribute ( "Health" ):
                    self.change_health ( event.update.getAttribute ( "Health" ).getValue ( ) )   
        if isinstance ( event , Events.ClusterWeatherEvent ):
            if event.group == self.group:
                weather = event.weather
                if weather.getAttribute ( "Health" ):
                    heatlh = weather.getAttribute ( "Health" ) . getValue ( )
                    self.change_health ( heatlh )
                if weather.getAttribute ( "Hygiene" ):
                    hygiene = weather.getAttribute ( "Hygiene" ) . getValue ( )
                    self.change_hygiene ( hygiene )
                if weather.getAttribute ( "Hunger" ):
                    hunger = weather.getAttribute ( "Hunger" ) . getValue ( )
                    self.change_hunger ( hunger )
                if weather.getAttribute ( "Fatigue" ):
                    fatigue = weather.getAttribute ( "Fatigue" ) . getValue ( )
                    self.change_fatigue ( fatigue )
                if weather.getAttribute ( "Morale" ):
                    morale = weather.getAttribute ( "Morale" ) . getValue ( )
                    self.change_morale ( morale )

    def isAlive ( self ):
        if self.health > 0:
            return True
        else:
            return False

    def setName ( self , name ):
        self.name = name

    def getName ( self ):
        return self.name

    def setGroup ( self , group ):
        self.group = group

    def getGroup ( self ):
        return self.group

    def change_health ( self , amount ):
        if (amount <= 0):
            if (amount + self.health <= 0):
                self.health = 0
                print (self.getName ( ) + " died.")
                self.mediator.post ( Events.CharacterDeadEvent ( self ) )
            else:
                self.health = self.health + amount
        else: #amount > 0
            if (amount + self.health >= self.max_health):
                self.health = self.max_health
            else:
                self.health = self.health + amount

    def change_morale ( self , amount ):
        if (amount <= 0):
            if (amount + self.morale <= 0):
                self.morale = 0
            else:
                self.morale = self.morale + amount
        else:
            if (amount + self.morale >= self.max_morale):
                self.morale = self.max_morale
            else:
                self.morale = self.morale + amount

    def change_hygiene ( self , amount ):
        if (amount <= 0):
            if (amount + self.hygiene <= 0):
                self.hygiene = 0
            else:
                self.hygiene = self.hygiene + amount
        else:
            if (amount + self.hygiene >= self.max_hygiene):
                self.hygiene = self.max_hygiene
            else:
                self.hygiene = self.hygiene + amount

    def change_fatigue ( self , amount ):
        if (amount <= 0):
            if (amount + self.fatigue <= 0):
                self.fatigue = 0
            else:
                self.fatigue = self.fatigue + amount
        else:
            if (amount + self.fatigue >= self.max_fatigue):
                self.fatigue = self.max_fatigue
            else:
                self.fatigue = self.fatigue + amount

    def change_hunger ( self , amount ):
        if (amount <= 0):
            if (amount + self.hunger <= 0):
                self.hunger = 0
            else:
                self.hunger = self.hunger + amount
        else:
            if (amount + self.hunger >= self.max_hunger):
                self.hunger = self.max_hunger
            else:
                self.hunger = self.hunger + amount

    def __str__ ( self ):
        print ("Character:")
        print ("--Name: " + self.name)
        print ("--Gender: " + self.gender)

        #Status
        print ("--Status: " + self.status )
        
        #Resources
        print ("--Health: " + str ( self.health ) )
        print ("--Morale: " + str ( self.morale ) )
        print ("--Hygiene: " + str ( self.hygiene ))
        print ("--Fatigue: " + str ( self.fatigue ))
        print ("--Hunger: " + str ( self.hunger ) )

        #Skills
        print ("--Fight: " + str ( self.fight ) )
        print ("--Sneak: " + str ( self.sneak ))
        print ("--Medical: " + str ( self.medical ))
        print ("--Spot: " + str ( self.spot ))
        print ("--Speed: " + str ( self.speed ) )

        return ""
