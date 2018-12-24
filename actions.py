# UTILS AND FUNCTIONALITY
from data import  population, clubs
from components import Club, Person

my_name = "Ahmad"
my_age = 30
my_bio = "Arrogant little brat"
myself = Person(my_name, my_bio, my_age)

def introduction():
    print("Hello, %s. Welcome to our portal." % my_name)

def options():
    # your code goes here!
    selection = input("Would you like to: \n1) Create a new club.\n or: \n 2)Browse and join clubs. \n or: \n 3)View existing clubs. \n or: \n 4)Display members of a club. \n or: \n -1) Close Application. \n >>")
    print (selection)
    if selection == "1":
        create_club()
    elif selection == "2":
        view_clubs()  # to be modified
    elif selection == "3":
        only_view()
    elif selection ==  "4":
        view_club_members()
    elif selection ==  "-1":
    	print("You just exitted")   
    


def create_club():
    # your code goes here!
    thename= input("Pick a name for your good club: ")
    description= input("What is your club about? ")

    newclub = Club(thename, description)
    newclub.assign_president(myself)

    print("Enter the numbers respresenting the person that you want to recruit:(-1 to stop) \n --------------------------------------")
    
    counter = 1
    for eachperson in population:
      print("[" + str(counter) +"] " + eachperson.name)
      counter += 1

    selection= 0
    totalage= myself.age

    while (not selection == '-1') and (selection > -1 and selection < 16) :
    	selection = int(input("> "))
    	if( selection == -1):
    		break
    	newclub.recruit_member(population[selection-1])
    	totalage = totalage + population[selection-1].age
    
    avgage = totalage/ (len(newclub.members) +1 )
    print("Here's your club: \n " + thename + "\n" + description)
    newclub.print_member_list()
    
    print("Average age in this club: %f yr \n ----------------------------------" % avgage  )


def view_clubs():
    for eachclub in clubs:
      print("Name: "+ eachclub.name + "\n Description: " + eachclub.description + "\n Members: " + str(len(eachclub.members)))
    selection = input("Enter the name of the club that you would like to join: ")

    
    for eachclub in clubs:
        if selection == eachclub.name:
            eachclub.recruit_member(myself)
    
    print(myself.name+ " just joined " + selection)

def only_view():
    for eachclub in clubs:
      print("Name: "+ eachclub.name + "\n Description: " + eachclub.description + "\n Members: " + str(len(eachclub.members)))

def view_club_members():
    
    for eachclub in clubs:
      print("Name: "+ eachclub.name + "\n Description: " + eachclub.description + "\n Members: " + str(len(eachclub.members)))

    selection = input("Enter the name of the club whose members you would like to see: ")
    
    totalage = 0

    for eachclub in clubs:
      if selection == eachclub.name:
        for eachperson in eachclub.members:
            totalage = totalage + eachperson.age
        eachclub.print_member_list()
        avgage = totalage / len(eachclub.members)

    print("Average age in this club: %f yr \n ----------------------------------" % avgage  )


def join_clubs():
   pass 
    

def application():
    introduction()
    options()
   
    
