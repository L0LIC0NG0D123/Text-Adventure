from time import sleep
from os import system, name

delay = 1
Health = 100
Inventory = ["Keys","Knife"]

if Health == 0:
	death()

else:
	pass

#======================================================================================================
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux
    else:
        _ = system('clear')
#======================================================================================================

def death():
		print ("\n\nYou Died\n\n")
		print ("Would you like to try again?\n\n")
		print ("-------------------")
		print ("[Yes] [No]")
		print ("-------------------\n\n")

		choice = input("Input: ")

		if choice == ("yes"):
			print ("\n\nYou hear a soft whisper saying 'It's not your time...'\n\n")
			sleep(4)
			clear()
			return(levelOne())

		else:
			print ("Thank You For Playing!")
			quit()

#======================================================================================================

def levelTwo():
	print ("Nothing yet...")


#======================================================================================================

def room2():
	print ("Nothing yet...")



#======================================================================================================

def basement():
	print ("Nothing yet...")



#=======================================================================================================

def levelChoose():
	clear()
	print ("\n\nWhat level did you leave off on?\n\n")
	sleep (2)
	print ("\n----------------------------------------------------")
	print ("[Car] [House Exterior] [House Interior]")
	print ("------------------------------------------------------\n\n")

	choice = input ("Input: ").lower()

	if choice == ("car"):
		clear()
		car()

	elif choice == ("house exterior"):
		clear()
		houseExtA()

	elif choice == ("house interior"):
		clear()
		houseInt()
#======================================================================================================
def houseInt():
	print ("After walking inside you notice the house is dark and very old. It appears as if nobody has lived here in decades.\n\n")
	sleep (4)
	print ("And yet... Oddly enough... It feels like someone is in the house with you.\n\n")
	sleep (3)
	print ("After shaking off the feeling that you aren't alone you use the lantern to see more of the house.\nYou notice a set of stairs, and some doors to other rooms. One of them is ajar...\n\n")
	return3()

def houseIntA():
	print ("You come back into the main area of the house you were in when you first walked in.")
	return(return2())

def return3():

	print ("\n----------------------------------------------------")
	print ("[Stairs] [Left Room] [Right Room (open)] [Search] [Leave] [Inventory] [Health ="+ str(Health)+ "]")
	print ("------------------------------------------------------\n\n")

	choice = input("Input: ")

	if choice == ("stairs"):
		print ("You go up the stairs slowly, letting the lantern light your way.\n\n")
		sleep (2)
		print ("A hallway comes into view at the top of the stairs....\n\n")
		clear()
		leveltwo()

	elif choice == ("left room","left"):

		if ("Small Key") in (Inventory):
			print ("You unlock the door")

		elif ("Small Key") not in (Inventory):
			print ("You walk up to the door to the room on your left and attempt to open it.\n\n")
			sleep (2)
			print ("It seems to be locked, maybe theres a key somewhere?")
			clear()
			sleep(delay)
			return(return3())

		else:
			return(return3())

	elif choice == ("right room","right"):
		print ("You walk up to the door of the room to your right and notice that its slightly ajar. Do you open it?\n\n")
		print ("\n------------")
		print ("[Yes] [No]")
		print ("-------------\n\n")

		choice = input("Input: ")

		if choice == ("yes"):
			clear()
			room2()
		elif choice == ("no"):
			return(return3())


	elif choice == ("search"):
		print ("You search the area but you dont really find anything except faint stains on the floor. Not sure what it was.\n\n")
		sleep(3)
		clear()
		return(return3())

	elif choice == ("leave"):
		print ("As you turn to leave, something comes out of nowhere and you hear a slicing noise. As fast as it appeared, it disappeared.\n\n")
		sleep (2)
		clear()
		death()

#======================================================================================================  

def houseExtA():
	print ("After lighting the lantern you can now see your surroundings. What do you do?\n\n")
	return1()

def return1():
	print ("\n----------------------------------------------------")
	print ("[Go Inside] [Search] [Leave] [Inventory] [Health ="+ str(Health)+ "]")
	print ("------------------------------------------------------\n\n")

	choice = input("Input: ")

	if choice == ("go inside"):
		if ("Rusty Key") in (Inventory):
			print("You use the rusty key to unlock the door. You go inside.\n\n")
			sleep(2)
			clear()
			houseInt()


		elif ("Rusty Key") not in (Inventory):
			print ("The door is locked. Where is the key?\n\n")
			return(return1())

		else:
			print ("Invalid Response, Try Again...\n\n")
			return(return1())

	elif choice == ("search"):

		if choice == ("search"):
			print ("You search the area with the light of the lantern and find a rusty key on the steps of the porch\n\n")
			Inventory.append("Rusty Key")
			print ("Rusty Key Added to Inventory!\n\n")
			sleep(delay)		
			print ("Your Inventory now includes: "+ str(Inventory) +"\n\n")
			return(return1())

		else:
			print ("Invalid Choice, Try Again...")
			return(return1())


	elif choice == ("leave"):
		print ("You go back up the side road...\n\n")
		levelOneA()

	elif choice == ("inventory"):
		print ("Your Inventory: "+ str(Inventory) +"\n\n")
		return(return1())

	else:
		print ("Invalid Choice, Try Again...\n\n")
		return(return1())

#=======================================================================================================

def houseExt():
	print ("You are now at the exterior of the house. It's too dark to see anything but there seems to be a lantern...")
	print("\n\nWhat do you do?\n\n")
	return2()


def return2():
	print ("\n----------------------------------------------------")
	print ("[Light Lantern] [Go Inside] [Search] [Leave] [Inventory] [Health ="+ str(Health)+ "]")
	print ("------------------------------------------------------\n\n")

	lanternLit = False #Lantern is not lit

	choice = input ("Input: ").lower()

	if choice == ("light lantern"):

		if ("Matches") in (Inventory):
			print ("You lit the lantern with your matches!\n\n")
			Inventory.append("Lantern")
			print ("Your Inventory now includes: "+ str(Inventory)+ "\n\n")
			houseExtA()

			lanternLit = True #If the matches are found, value set to true. Meaning lantern is now lit

		elif ("Matches") not in (Inventory):
			print ("You do not have a way to light the lantern!\n\n")
			return(return2())

		else:
			print ("Invalid Response, Try Again...\n\n")
			return(return2())

	elif choice == ("go inside"):
		if ("Rusty Key") in (Inventory):
			print("You use the rusty key to unlock the door. You go inside.\n\n")
			houseInt()

		elif ("Rusty Key") not in (Inventory):
			print ("The door is locked. Where is the key?\n\n")
			return(return2())

		else:
			print ("Invalid Response, Try Again...\n\n")
			return(return2())

	elif choice == ("search"):

		if choice == ("search"):
			print ("It's too dark to see anything. Perhaps if i had a source of light?")
			return(return2())

		else:
			print ("Invalid Choice, Try Again...")
			return(return2())


	elif choice == ("leave"):
		print ("You go back up the side road...\n\n")
		levelOneA()

	elif choice == ("inventory"):
		print ("Your Inventory: "+ str(Inventory) +"\n\n")
		return(return2())

	else:
		print ("Invalid Choice, Try Again...\n\n")
		return(return2())
#======================================================================================================
def car():
	print ("You are standing at your car. What do you do?")

	while True:

		print ("\n----------------------------------------------------")
		print ("[Search] [Leave] [Inventory] [Health ="+ str(Health)+ "]")
		print ("------------------------------------------------------\n\n")

		choice = input ("Input: ")

		if choice == ("search"):
			print ("After some searching you find basic supplies.\n\nAdded to inventory: 'First Aid Kit','Water Bottle','Matches'")
			Inventory.append("First Aid Kit")
			Inventory.append("Water Bottle")
			Inventory.append("Matches")
			print ("Your Inventory now includes: "+ str(Inventory))

		elif choice == ("leave"):
			print ("\nYou leave your car and wander back up the road...\n")
			levelOneA()

		elif choice == ("Inventory"):
			print ("Your Inventory: "+ str(Inventory)+"\n\n")

		else:
			print ("Invalid Response, Try Again...\n\n")
			sleep(2)

#==========================================================================================================
def tutorial():

	print ("=======================================================================================================================\n")
	print ("						~~TUTORIAL~~\n")
	print ("=======================================================================================================================\n")
	sleep(1.5)
	print ("\nThe rules are simple.")
	sleep(3)
	print ("Just read the story as it goes and type the options you see listed.\n\nExample: [Yes] [No] or [Left] [Right] [Up]")
	sleep(6)
	clear()
	levelOne()

#============================================================================================================
def levelOneA():

	print ("You find yourself back where you started before. It's dark but you can still see the outline of a side road.\n")
	sleep(delay)
	print ("There is still no sign of any cars coming soon. What do you do?\n\n")

	while True:
		sleep(3)
		print ("-----------------------------------------------------------------------")
		print ("[Go Back] [Side Road] [Wait] [Inventory] [Health = "+ str(Health) +"]")
		print ("-----------------------------------------------------------------------\n\n")

		choice = input("Input: ").lower()

		if choice == ("go back"):
			print ("\nYou go back to your car.\n")
			sleep(delay)
			car()

		elif choice == ("side road"):
			print ("\nYou walk down the dark side road towards the house...\n")
			sleep(1)
			houseExt()

		elif choice == ("wait"):
			print ("\nYou wait for some time.\n")
			sleep (1)
			print ("[Go Back] [Side Road] [Wait] [Inventory] [Health = "+ str(Health) +"]\n")

		elif choice == ("inventory"):
			print("\nYour inventory: " + str(Inventory))

		else:
			print ("\nInvalid Choice, Try Again...\n")

#====================================================================================================================

def levelOne():

	print ("You find yourself broken down on the side of the road in the middle of nowhere. You havent seen another car in hours.\n\n")
	sleep(3)
	print ("After walking for a mile or two it gets dark but you see a house at the end of a long side road.\nWhat do you do? Where do you go?\n")

	while True:
		sleep(3)
		print ("-----------------------------------------------------------------------")
		print ("[Go Back] [Side Road] [Wait] [Inventory] [Health = "+ str(Health) +"]")
		print ("-----------------------------------------------------------------------\n\n")

		choice = input("Input: ").lower()

		if choice == ("go back"):
			print ("\nYou go back to your car.\n")
			sleep(delay)
			car()

		elif choice == ("side road"):
			print ("\nYou walk down the dark side road towards the house...\n")
			sleep(1)
			houseExt()

		elif choice == ("wait"):
			print ("\nYou wait for some time.\n")
			sleep (1)
			print ("[Go Back] [Side Road] [Wait] [Inventory] [Health = "+ str(Health) +"]\n")

		elif choice == ("inventory"):
			print("\nYour inventory: " + str(Inventory))

		else:
			print ("\nInvalid Choice, Try Again...\n")

#============================================================================================================================
def start():


	clear()
	while True:

		print ("=======================================================================================================================\n")
		print ("					~~Welcome To My Text-Based Adventure Game~~\n")
		print ("=======================================================================================================================\n")


		name = input ("What is your name: ")
		print ("\n\nHave you played before?\n\n")
		print ("----------------")
		print ("[Yes] [No]")
		print ("----------------\n\n")

		choice = input ("Input: ")

		if choice == ("yes"):
			levelChoose()

		else:
			choice = input ("Would you like to start the game "+ str(name) +"?\n\n 	   [Yes] [No]\n\nInput: ").lower().strip()

			if choice == ("yes"):
				clear()
				tutorial()

			elif choice == ("no"):
				print ("Sorry to hear")
				quit()

			else:
				print ("\n~~Invalid Entry, Try Again~~\n")

start()