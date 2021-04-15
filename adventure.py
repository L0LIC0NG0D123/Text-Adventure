from time import sleep
from os import system, name

delay = 1
Health = 100
Inventory = ["Keys","Knife"]

#======================================================================================================
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux
    else:
        _ = system('clear')
#======================================================================================================
def houseInt():
	print ("End of the game for now...")
	quit()
#======================================================================================================  
def houseExt():
	print ("You are now at the exterior of the house. It's too dark to see anything but there seems to be a lantern...")
	print("\n\nWhat do you do?\n\n")
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

			lanternLit = True #If the matches are found, value set to true. Meaning lantern is now lit

		elif ("Matches") not in (Inventory):
			print ("You do not have a way to light the lantern!\n\n")

		else:
			print ("Invalid Response, Try Again...\n\n")

	elif choice == ("go inside"):
		if ("Rusty Key") in (Inventory):
			print("You use the rusty key to unlock the door. You go inside.\n\n")
			houseInt()

		elif ("Rusty Key") not in (Inventory):
			print ("The door is locked. Where is the key?\n\n")

		else:
			print ("Invalid Response, Try Again...\n\n")

	elif choice == ("search"):

		if lanternLit == True:
			print ("You search the area with the light of the lantern and find a rusty key on the steps of the porch\n\n")
			Inventory.append("Rusty Key")
			print ("Rusty Key Added to Inventory!\n\n")
			sleep(delay)		
			print ("Your Inventory now includes: "+ str(Inventory) +"\n\n")

	elif choice == ("leave"):
		print ("You go back up the side road...\n\n")
		levelOneA()

	elif choice == ("inventory"):
		print ("Your Inventory: "+ str(Inventory) +"\n\n")

	else:
		print ("Invalid Choice, Try Again...\n\n")
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

		elif choice == ("Wait"):
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

		elif choice == ("Wait"):
			print ("\nYou wait for some time.\n")
			sleep (1)
			print ("[Go Back] [Side Road] [Wait] [Inventory] [Health = "+ str(Health) +"]\n")

		elif choice == ("inventory"):
			print("\nYour inventory: " + str(Inventory))

		else:
			print ("\nInvalid Choice, Try Again...\n")

#============================================================================================================================
def start():

	while True:

		print ("=======================================================================================================================\n")
		print ("					~~Welcome To My Text-Based Adventure Game~~\n")
		print ("=======================================================================================================================\n")


		name = input ("What is your name: ")



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