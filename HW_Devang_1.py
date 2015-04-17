'''Author: - Devang A Joshi
   Version 1.0
   Description: This program is a mini guessing game where User need to think a value between 1 to 100
				an Array of 100 is created, Initial vales were set. then sorting is made by midpoint selection 
	Guided By : - Gula Nurmatova
	'''


print("----------------------------------------")
print("----|  | |--- |    |      ----  --------")
print("----|--| |__  |    |     |    | --------")
print("----|  | |___ |___ |___  |____| --------")
print("----------------------------------------")

name = input("PLEASE ENTER YOUR NAME \n")                           #Getting the name of the User
print( "\t" + name + " well come to Guessing number game\n")		#Printing the name of the User

print("\tGuess any Number between 1 to 100\n")

a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25, #Defining an array of 100 values from 1 to 100
	26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,
	48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,
	70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,
	92,93,94,95,96,97,98,99,100]
play="yes"															#let the initial state of the game be yes.
while(play=="yes"):
	Vmid=(a[99]+a[0])//2											#Getting the first MID value from the array which is 50 
	Vmax=a[99]														#Defining the Max value in array 
	Vmin=a[0]														#Defining the Min value in array
	tries = 0														#Initial number of tries be 0

	guess=input("\tIs the number " + str(Vmid) + " ? (yes/no) \n Ans.") #Guessing the Number and getting input from user is it correct or not
	tries=tries+1													#Incrementing the tries by 1
	if (guess=='yes'):						#If the input value from the user is "yes" then following lines will be executed 
			print("\tPERFECT I am Genius")
			print("\tI got your number in " + str(tries) +" try")
	else:							        #Else the input value from the user is "no" then following lines will be executed
			Nguess=input("\tIs the number Greater than " + str(Vmid) + " (Yes/No)?\n Ans.")

			while (guess=='no' and (Nguess=='yes' or Nguess=='no')):			   #While loop will run till the value of guess is no and either value of Nguess 	
					while (Nguess=="yes"):										   #While the value of Nguess is "yes" following will be executed 
						Vmin=Vmid+1												   #Changing the Min value by adding 1 to the Mid value 
						Vmid=((Vmax+Vmin)//2)									   #Recalculating the Mid value
						guess=input("\tIs the number " + str(Vmid) + "? (Yes/No)\n Ans.")
						if (guess=='no'):
							tries=tries+1
							Nguess=input("\tIs the number Greater than " + str(Vmid) + "?(Yes/No)\n Ans.")
						elif(guess=='yes'):
							tries=tries+1
							print("\tI guessed it in " + str(tries) + " tries.")
							break

					while (Nguess=="no"):											#While the value of Nguess is "no" following will be executed
						Vmax=Vmid-1													#Changing the Max value by subtracting 1 to the Mid value
						Vmid=((Vmax+Vmin)//2)										#Recalculating the Mid value
						guess=input("\tIs the number " + str(Vmid) + "? (Yes/No) \n Ans.")
						if (guess=='no'):
							tries=tries+1
							Nguess=input("\tIs the number Greater than " + str(Vmid) + "?(Yes/No)\n Ans.")
						elif(guess=='yes'):
							tries=tries+1
							print("\tI guessed it in " + str(tries) + " tries.")
							break
	play=input("Lets Play again !!!!! (yes/no)")   									#taking input from the user to play again