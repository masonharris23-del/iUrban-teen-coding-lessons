#### Midterm 141
#Name:
#Instructions: start in the main guard on line 99, and fill in the functions as needed.
# If you start with A1 and B1 and work your way down, you'll be going from easiest to hardest
#  (but you can skip around as needed)
# you'll find under each function (TODOs B through F) some pseudocode to help you
# Each function (TODOs B through F) is worth 15 points
# Each of the 12 A TODOs are worth 2 points
# Everyone gets 1 free point for putting their name on their file :-)


#TODO B1
#write the function that matches this doc string
'''
list_as_string takes a list and makes a string from the values
#and their labels
parameters: a list of 3 items: food, water, and happy
return: a string formatted like this: "food: 1 water: 1 happy: 1"
#where the numbers match the values in the list
'''
def list_as_string(the_list):
    
    list_as_string = ""
    list_as_string = "food: " + str(the_list[0]) + " water: " + str(the_list[1]) + " happy: " + str(the_list[2])
    
    return(list_as_string)

#TODO C1
'''
day_passes represents a day passing in the turtle's life and it getting
#hungrier, thirstier, and sadder
parameters: the turtle's state list
return: none
'''
def day_passes(state):
    
    #TODO C2
    #for each of the turtle's states, reduce the value by a random number
    #between 2 and 5
    for i in range(3):
        reduction = random.randint(2,5)
        state[i] -= reduction
 
    
    #TODO C3
    #print "turtle is now...food: 2 water: 4 happy: 3" (but with the currently correct numbers) (hint: use list_as_string!) 
    print_out = "turtle is now..." + list_as_string(state)
    print(print_out)
    
#TODO D1
'''
turtle_care represents taking care of the turtle by giving it food or water. 
parameters:
    the index integer of what you're updating (0 for food and 1 for water),
    the turtle's state list
    the supply list
return: how many food or water were given in total
'''
def turtle_care(what_updating, state, supplies):
    
    count_given = 0
    #TODO D2
    #until the turtle's food/water(whatever is at the passed in index) reaches 10 AND
    #you still have some food/water in your supplies
    #increase the turtle's food/water by 1 and reduce the supply food/water by 1
    while state[what_updating] < 10 and supplies[what_updating] > 0:
        
        supplies[what_updating] -=1
        state[what_updating] += 1
        count_given +=1
        
        
    #TODO D3
    #return the total number of food or water which was given to the turtle
    return(count_given)

#TODO E1
'''
walk_turtle takes a turtle on a walk.
    The turtle likes walking down stairs! Turtle will draw a staircase going down and to the right.
    
parameters: a turtle object facing right
return: none
''' 
def walk_turtle(t):
    #print("in turtle")
    #TODO E2
    #have the turtle walk down one stair of side and height 21
    t.forward(21)
    t.right(90)
    t.forward(21)
    t.left(90)
    #print("first step")
    #TODO E3
    #Have it walk down a random number of stairs (between 2 stairs and 10 stairs)
    for i in range(random.randint(2,10)):
        #print(i)
        t.forward(21)
        t.right(90)
        t.forward(21)
        t.left(90)
  
  
    #TODO E4
    #for extra credit, use a nested loop to do the above


#TODO F1
'''
forage represents foraging for supplies and finding a random amount

parameters: a supply list
return: none
'''
def forage(supplies):
   
   #TODO F2 print "foraging..."
    print("foraging...")
  
   
   #TODO F3 
   #choose a random index position in the supply list and add a random value
    #between 4 and 10 (inclusive)
    supplies[random.randint(0,2)] = random.randint(4,10)

'''
main is called by the main guard and runs a loop asking the user what task they want to do and then doing that.
After each task, the loop runs again, allowing the user to pick another task to execute.
Some user tasks will require function calls, which should happen inside the main loop, and then the loop will continue. 

parameters: a supply list and a turtle state list
return: none
'''

def main(supplies_list, turtle_state):
       
    #TODO A5
    #Put this input statement inside a while loop that'll run
    #until the user types 'q'
    user_choice = ""
    while user_choice != "q":
        user_choice = input("type 't' to talk to the turtle, 's' to check supply levels, 'n' for next day, 'c' to care for the turtle, 'w' to walk the turtle, 'f' to forage for supplies, and 'q' to quit ") #provided, don't change
        
        
        #TODO A6
        #if user types t, then send the turtle's state list to list_as_string() (TODO B1) and print the return
        if user_choice == "t":
            print(list_as_string(turtle_state))
        
        #TODO A7
        #if user types s, then send the turtle's supply list to list_as_string() (TODO B1) and print the return
        elif user_choice == "s":
            print(list_as_string(supplies_list))
        
        #TODO A8
        #if the user types n, then call day_passes() (TODO C1) and pass in the turtle state list
        elif user_choice == "n":
            day_passes(turtle_state)
        
        #TODO A9
        elif user_choice == "c":
            num_given = turtle_care(0, turtle_state, supplies_list)
            print("fed :" , num_given)
            num_given =turtle_care(1, turtle_state, supplies_list)
            print("watered :" , num_given)
            
        #if the user types c, then first give the turtle food and then water.
            #use turtle_care (TODO D1) to give the food and water
            #and print out : "fed : 3 times" where the number is how many times you fed it (return value from turtle_care)
            #and print out : "watered : 3 times" where the number is how many times you watered it (return value from turtle_care)
  
        
        #TODO A10
        #if the user types w, then the turtle takes a walk and becomes happy
        elif user_choice == "w":
            #TODO A10.1
            #create a turtle
            kelly = turtle.Turtle()
            
            #TODO A10.2
            #send the turtle on a walk using walk_turtle() (TODO E1)
            walk_turtle(kelly)
         
            #TODO A10.3
            #add 5 to the turtle's happy value (index position 2 on the turtle state list)
            turtle_state[2] += 5
      
            #TODO A10.4
            # comment out the line below to run turtle.exitonclick() so the window closes when you click
            turtle.exitonclick()
          
        
        #TODO A11
        #if the user types f, then go foraging
        elif user_choice == "f":
    
            #TODO A11.1
            #go foraging using forage() (TODO F1)
            forage(supplies_list)
    
            #TODO A11.2
            #then have a day pass using day_passes()
            day_passes(turtle_state)
            
            #TODO A11.3       
            #then print out the new supply list using list_as_string()
            print(list_as_string(supplies_list))
            
        #TODO A12
        #if the user types q then print goodbye
        elif user_choice == "q":
            print("Goodbye")
        
         
        #TODO A13
        #if the user prints anything else, print "I didn't understand. Please try again" . Please print this exactly (copy & paste the string).
        else:
            print("I didn't understand. Please try again" )
    pass

"""
Summary: we use the main guard to separate the functions from the running of the functions.
This makes importing & testing easier!

"""
if __name__ == "__main__":
    
    #TODO A1 we'll be using turtles and random. Use the right import statements here in the main guard.
    import random
    import turtle
    
    #TODO A2
    #make a list to store the turtle's state, which will have 3 values
    #to store how much food, water, and happy the turtle has.
    #start the turtle with 5 of each
    turtle_stats = [5,5,5] #food, water, happy
    
    #TODO A3
    #make a list to store your suppplies, which will have 3 values to
    #store how much food, water, and happy brand treats you have.
    #start the list with 4 of each.
    supplies = [4,4,4] #food, water, treats
    
    #TODO A4 Call the main function and pass in the turtle state list
    #and the supplies list
    main(supplies, turtle_stats)
    
    pass
    
