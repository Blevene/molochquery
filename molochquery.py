# Moloch Search Query Generator 
# Author: Blevene
# No Distribution without author's consent
# Version = 0.1

# To Do:
# [x] Add support for more than 2 terms
# [] Clean up/condense the if/elif/else logic
# [] Put each element/option of a query into a list, ex:['ip', 'ip.src'...] 
# [] Functionify different base queries

from sys import exit

# Define menu options, a list of all menu entries and what is being asked by each entry
def menu(list, question):
	for entry in list:
		print " %d) %s" % (list.index(entry) + 1, entry) 
# This makes it so that the number starts at 1 instead of 0, but doesn't modify the list structure	
	return input(question) - 1

# Write all the questions here: "What do you want to search by, etc"
# I'm not sure how to call this
def query():
# List of different params that make up a moloch query
	molparams = ['IP', 'Port', 'Country', 'Moloch ID']
	 
	for line in molparams:
		print line

#List of IP and Port direction modifiers
def direction(): 
	direc = ['src', 'dst']
	print direc[0]
	print direc[1]

# List of menu options
items = ["Single Term Query", "Two Term Query", "Three Term Query", "Cry for mercy(yell for Ben)", "Quit"]


print "Welcome to the Moloch query generator!"

# Keep it running until there's a valid option selected
loop = 1 

while loop == 1:
	choice = menu(items, "Please select an option from the menu: ")

	if choice == 0:
# Call the query function
		questions = query()

		ask = raw_input("Please select an option from list provided: ")

		if ask == 'IP' or ask == 'ip' or ask == 0:
			ip = raw_input("Enter an IP address > ")
			modify = raw_input("Do you care about directionality? > (Y/N)")
			
			if modify == "Y" or modify == "y":
				src_or_dst = direction()
				direc = raw_input("Is this IP the source or destination? > (src/dst)").lower()
				if direc == "src" or direc == "source":
					print "Ok, your final query is:\n ip.src == %s" % ip
					exit(0)
				if direc == "dst" or direc == "destination" or direc == "dest":
					print "Ok, your final query is:\n ip.dst == %s" % ip
					exit(0)
				else:
					print "Sorry, I didn't understand your input."

			else:
				print "Your final query is: ip == %s" % ip
				exit(0)
		elif ask == 'Port' or ask == 'port':
			pass
		elif ask == 'Country' or ask == 'country':
			pass
		elif ask == 'Moloch ID' or ask == 'Moloch id' or ask == 'moloch id':
			pass
		else:
			pass



	elif choice == 1:
		pass
	elif choice == 2:
		pass
	elif choice == 3:
		pass
	elif choice == 4:
		exit(0)
	else:
		print "Please select a valid option!"
