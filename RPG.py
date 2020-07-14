#  File: RPG.py
#  Description: Homework #2
#  Student's Name: Sarah Teng
#  Student's UT EID: st29653
#  Course Name: CS 313E 
#  Unique Number: 50739
#
#  Date Created: February 10, 2019
#  Date Last Modified: February 14, 2019

#import package needed for formatting str output
import textwrap


#create a character super class with basic methods
class RPGCharacter:

    #initialize the object with a name
    def __init__(self,name): 
        self.name = name

    #define the wield method to possess a weapon
    def wield(self,weapon):

        self.weapon = weapon
        print(self.name,"is now wielding a(n)",weapon)

    #define the unwield method to unwield a weapon
    def unwield(self):

        self.weapon = "none"
        print(self.name,"is no longer wielding anything.")

    #define the putOnArmor method to put armor on the character
    def putOnArmor(self,armor):

        self.armor = armor
        print(self.name,"is now wearing",armor)

    #define the takeOffArmor method to take armor off the character
    def takeOffArmor(self):

        self.armor = "none"
        print(self.name,"is no longer wearing anything.")

    #define the fight method that takes a character-opponent argument 
    def fight(self,opponent):

        damage = self.weapon.damage

        print(self.name,"attacks",opponent.name,"with a(n)",self.weapon)

        opponent.health = opponent.health - damage

        print(self.name,"does",damage,"damage to",opponent.name)
        print(opponent.name,"is now down to",opponent.health,"health.")

        #check to see if character has been defeated
        opponent.checkForDefeat()

    #check character health to determine whether he has been defeated
    def checkForDefeat(self):

        if self.health <= 0:
            print(self.name,"has been defeated!")
        else:
            pass

    #define a str method to output character stats
    def __str__(self):
        print("")
        return textwrap.dedent(f"""\
                                {self.name}
                                    Current Health: {self.health}
                                    Current Spell Points: {self.points}
                                    Wielding: {self.weapon}
                                    Wearing: {self.armor}
                                    Armor Class: {self.armor.AC}\n""")        
        
            
        
#define a fighter subclass that inherits from the RPGCharacter superclass
class Fighter(RPGCharacter):

    def __init__(self,name):

        self.maxHealth = 40

        #declare default/initial stats for new character instance
        self.name = name
        self.armor = Armor()
        self.weapon = Weapon()
        self.health = 40
        self.points = 0
        

#define a wizard subclass that inherits from the RPGCharacter superclass
class Wizard(RPGCharacter):


    def __init__(self,name):

        self.maxHealth = 16
        
        #declare default/initial stats for new character instance
        self.name = name
        self.armor = Armor()
        self.weapon = Weapon()
        self.health = 16
        self.points = 20
        self.AC = 10

    #define another wield method for the wizard class
    def wield(self,weapon):

        #wizards can wield all weapons except for sword and axe
        if self.weapon == "sword" or self.weapon == "axe":
            print("Weapon not allowed for this character class.")
        else:
            self.weapon = weapon
            print(self.name,"is now wielding a(n)",weapon)

    #define another putOnArmor method for the wizard class
    def putOnArmor(self,armor):

        #wizards cannot wear armor
        self.armor = "none"
        print("Armor not allowed for this character class.")

    #define the castSpell method for wizards only
    def castSpell(self,spell,target):

        self.spell = spell
        self.target = target

        #deduct the costs and effects from respective characters based on
        #what spell the wizard uses
        if self.spell == "Fireball":
            cost = 3
            effect = 5
            target.health = target.health - effect
            print(self.name,"casts",spell,"at",target.name)
        elif self.spell == "Lightning Bolt":
            cost = 10
            effect = 10
            target.health = target.health - effect
            print(self.name,"casts",spell,"at",target.name)
        elif self.spell == "Heal":
            cost = 6
            effect = -6
            print(self.name,"casts",spell,"at",target.name)
            target.health = target.health - effect
        else:
            print("Unknown spell name. Spell Failed.\n")

        #check for sufficient spell points
        if self.points < cost:
            print("Insufficient spell points")
        #health cannot exceed max health levels if "heal" spell is used
        elif target.health - effect > target.maxHealth:
            target.health = target.maxHealth
        else:
            self.points = self.points - cost

        #print the effects of the heal spell if heal is used
        if self.spell == "Heal":
            self.points = self.points - cost
            print(self.name,"heals",target.name,"for",abs(effect),"health points")
            print(self.name,"is now at",self.health,"health")
        else:
            print(self.name,"does",abs(effect),"damage to",target.name)
            print(target.name,"is now down to",str(target.health),"health")

        #check to see if character has been defeated
        target.checkForDefeat()


#define the weapon class and assign weapons with damage values 
class Weapon:

    def __init__(self,weapon="none"):
        
        self.weapon = weapon

        if self.weapon == "dagger":
            self.damage = 4
        elif self.weapon == "axe":
            self.damage = 6
        elif self.weapon == "staff":
            self.damage = 6
        elif self.weapon == "sword":
            self.damage = 10
        elif self.weapon == "none":
            self.damage = 1
        else:
            raise ValueError("not a valid weapon type")

    #define the str method to be able to print the weapon object
    def __str__(self):
        
        return str(self.weapon)

    
#define the armor class and assign armors with AC values
class Armor:

    def __init__(self, armor="none"):

        self.armor = armor

        if self.armor == "plate":
            self.AC = 2
        elif self.armor == "chain":
            self.AC = 5
        elif self.armor == "leather":
            self.AC = 8
        elif self.armor == "none":
            self.AC = 10
        else:
            raise ValueError("not a valid armor type")

    #define the str method to be able to print the armor object
    def __str__(self):

        return str(self.armor)

        
        
#define and execute the main method
def main():

    plateMail = Armor("plate")
    chainMail = Armor("chain")
    sword = Weapon("sword")
    staff = Weapon("staff")
    axe = Weapon("axe")

    gandalf = Wizard("Gandalf the Grey")
    gandalf.wield(staff)
    
    aragorn = Fighter("Aragorn")
    aragorn.putOnArmor(plateMail)
    aragorn.wield(axe)
    
    print(gandalf)
    print(aragorn)

    gandalf.castSpell("Fireball",aragorn)
    aragorn.fight(gandalf)

    print(gandalf)
    print(aragorn)
    
    gandalf.castSpell("Lightning Bolt",aragorn)
    aragorn.wield(sword)

    print(gandalf)
    print(aragorn)

    gandalf.castSpell("Heal",gandalf)
    aragorn.fight(gandalf)

    gandalf.fight(aragorn)
    aragorn.fight(gandalf)

    print(gandalf)
    print(aragorn)


main()
